select
    cast(customer_id as integer) as customer_id,
    cast(first_name as varchar) as first_name,
    cast(last_name as varchar) as last_name,
    cast(email as varchar) as email,
    cast(signup_date as date) as signup_date,
    cast(updated_at as timestamp) as updated_at,
    cast(loaded_at as timestamp) as loaded_at


from {{ source('ecommerce', 'raw_customers') }}
