select
    cast(payment_id as integer) as payment_id,
    cast(order_id as integer) as order_id,
    cast(payment_method as varchar) as payment_method,
    cast(amount_cents as integer) as amount_cents,
    cast(payment_status as varchar) as payment_status,
    cast(payment_date as timestamp) as payment_date,
    cast(updated_at as timestamp) as updated_at,
    cast(loaded_at as timestamp) as loaded_at


from {{ source('ecommerce', 'raw_payments') }}
