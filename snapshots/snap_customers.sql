{% snapshot snap_customers %}


{{
    config(
        target_schema='main',
        unique_key='customer_id',
        strategy='timestamp',
        updated_at='updated_at',
        invalidate_hard_deletes=true
    )
}}


select
    customer_id,
    first_name,
    last_name,
    email,
    signup_date,
    updated_at
from {{ source('ecommerce', 'raw_customers') }}


{% endsnapshot %}
