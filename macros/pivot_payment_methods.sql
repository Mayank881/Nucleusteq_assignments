{% macro pivot_payment_methods(payment_methods) %}


{% for method in payment_methods %}


    sum(
        case
            when payment_method = '{{ method }}'
            then amount_cents
            else 0
        end
    ) as {{ method }}_payment_cents


    {% if not loop.last %},{% endif %}


{% endfor %}


{% endmacro %}
