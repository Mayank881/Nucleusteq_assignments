{% macro grant_read_access(relation) %}


    {% if target.type == 'duckdb' %}
        select 1
    {% else %}
        grant select on {{ relation }} to analytics_read_only
    {% endif %}


{% endmacro %}
