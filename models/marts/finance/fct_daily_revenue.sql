{{
    config(
        materialized='incremental',
        unique_key='order_id',
        incremental_strategy='merge',
        on_schema_change='sync_all_columns'
    )
}}


        -- sync_all_columns is deliberate: if the upstream model gains,
        -- removes, or changes columns, the incremental target should stay
        -- synchronized with the model schema.

with revenue_data as (


    select
        order_id,
        customer_id,
        order_date,
        status,
        revenue_usd,
        latest_payment_date,
        updated_at


    from {{ ref('int_orders_joined_payments') }}


    {% if is_incremental() %}


        /*
        Process orders from the latest loaded order date
        plus a 3-day lookback window.


        The lookback is required to capture late-arriving
        payments for recently processed orders.
        */


        where order_date >= (
            select
                max(order_date) - interval '3 days'
            from {{ this }}
        )


    {% endif %}


)


select
    order_id,
    customer_id,
    order_date,
    status,
    revenue_usd,
    latest_payment_date,
    updated_at


from revenue_data
