# Test Coverage Summary


Generic tests such as unique and not_null validate common structural data-quality rules across the models. Accepted_values ensures that status columns contain only valid business-defined values. Relationships tests verify that foreign-key values correctly reference their parent records. The singular positive-revenue test checks a specific finance business rule that revenue must be greater than zero. The custom non_negative generic test provides a reusable rule that can be applied to numeric columns across multiple models. Warning-level tests are useful for conditions that should be monitored without blocking the entire pipeline. Together, these tests provide structural, referential, business-rule, and reusable data-quality protection.
