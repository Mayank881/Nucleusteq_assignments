Paste:
{% set customer_id = 1 %}
{% set as_of_date = '2026-10-01 12:00:00' %}


select
    customer_id,
    email,
    dbt_valid_from,
    dbt_valid_to
from {{ ref('snap_customers') }}
where customer_id = {{ customer_id }}
  and dbt_valid_from <= cast('{{ as_of_date }}' as timestamp)
  and (
      dbt_valid_to > cast('{{ as_of_date }}' as timestamp)
      or dbt_valid_to is null
  )


