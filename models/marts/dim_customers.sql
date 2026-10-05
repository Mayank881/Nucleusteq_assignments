{{ config(materialized='table') }}

select
    customer_id,
    first_name,
    last_name,
    email,
    signup_date,
    updated_at 
from {{ ref('stg_customers') }}       