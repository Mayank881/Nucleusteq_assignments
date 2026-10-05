{{ config(materialized='ephemeral') }}


with orders as (


    select
        order_id,
        customer_id,
        order_date,
        status,
        total_amount_cents,
        updated_at
    from {{ ref('stg_orders') }}


),


payments as (


    select
        order_id,
        sum(amount_cents) as total_payment_cents,
        max(payment_date) as latest_payment_date
    from {{ ref('stg_payments') }}
    where payment_status = 'paid'
    group by order_id


),


joined as (


    select
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status,
        o.updated_at,
        {{ cents_to_dollars('p.total_payment_cents') }} as revenue_usd,
        p.latest_payment_date
    from orders o
    left join payments p
        on o.order_id = p.order_id


)


select *
from joined
