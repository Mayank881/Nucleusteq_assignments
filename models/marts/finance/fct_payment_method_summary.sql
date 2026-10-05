{{ config(materialized='table') }}


select
    order_id,


    {{ pivot_payment_methods(var('payment_methods')) }}


from {{ ref('stg_payments') }}


where payment_status = 'paid'


group by order_id


