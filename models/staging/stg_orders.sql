-- slim ci validation change
select
    cast(order_id as integer) as order_id,
    cast(customer_id as integer) as customer_id,
    cast(order_date as timestamp) as order_date,
    cast(status as varchar) as status,
    cast(total_amount_cents as integer) as total_amount_cents,
    cast(updated_at as timestamp) as updated_at,
    cast(loaded_at as timestamp) as loaded_at


from {{ source('ecommerce', 'raw_orders') }}
