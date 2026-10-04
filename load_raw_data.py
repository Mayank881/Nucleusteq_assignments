import duckdb
from pathlib import Path




DB_PATH = Path("dev.duckdb")




def create_raw_tables():
    conn = duckdb.connect(str(DB_PATH))


    # ---------------------------------------------------------
    # RAW CUSTOMERS
    # ---------------------------------------------------------
    conn.execute("""
        CREATE OR REPLACE TABLE raw_customers (
            customer_id INTEGER,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR,
            signup_date DATE,
            updated_at TIMESTAMP,
            loaded_at TIMESTAMP
        )
    """)


    conn.execute("""
        INSERT INTO raw_customers VALUES
            (1, 'Mayank', 'Sharma', 'mayank@example.com',
             '2026-01-10', '2026-01-10 10:00:00', CURRENT_TIMESTAMP),


            (2, 'Rahul', 'Verma', 'rahul@example.com',
             '2026-01-12', '2026-01-12 11:30:00', CURRENT_TIMESTAMP),


            (3, 'Priya', 'Patel', 'priya@example.com',
             '2026-01-15', '2026-01-15 09:45:00', CURRENT_TIMESTAMP),


            (4, 'Aman', 'Gupta', 'aman@example.com',
             '2026-01-20', '2026-01-20 14:20:00', CURRENT_TIMESTAMP),


            (5, 'Neha', 'Singh', 'neha@example.com',
             '2026-01-25', '2026-01-25 16:10:00', CURRENT_TIMESTAMP)
    """)


    # ---------------------------------------------------------
    # RAW ORDERS
    # ---------------------------------------------------------
    conn.execute("""
        CREATE OR REPLACE TABLE raw_orders (
            order_id INTEGER,
            customer_id INTEGER,
            order_date TIMESTAMP,
            status VARCHAR,
            total_amount_cents INTEGER,
            updated_at TIMESTAMP,
            loaded_at TIMESTAMP
        )
    """)


    conn.execute("""
        INSERT INTO raw_orders VALUES
            (1001, 1, '2026-09-01 10:00:00', 'completed',
             2500, '2026-09-01 10:05:00', CURRENT_TIMESTAMP),


            (1002, 2, '2026-09-02 11:30:00', 'completed',
             4500, '2026-09-02 11:35:00', CURRENT_TIMESTAMP),


            (1003, 3, '2026-09-03 14:15:00', 'pending',
             3200, '2026-09-03 14:20:00', CURRENT_TIMESTAMP),


            (1004, 1, '2026-09-04 16:45:00', 'completed',
             1800, '2026-09-04 16:50:00', CURRENT_TIMESTAMP),


            (1005, 4, '2026-09-05 09:20:00', 'cancelled',
             5000, '2026-09-05 09:25:00', CURRENT_TIMESTAMP),


            (1006, 5, '2026-09-06 13:10:00', 'completed',
             2750, '2026-09-06 13:15:00', CURRENT_TIMESTAMP)
    """)


    # ---------------------------------------------------------
    # RAW PAYMENTS
    # ---------------------------------------------------------
    conn.execute("""
        CREATE OR REPLACE TABLE raw_payments (
            payment_id INTEGER,
            order_id INTEGER,
            payment_method VARCHAR,
            amount_cents INTEGER,
            payment_status VARCHAR,
            payment_date TIMESTAMP,
            updated_at TIMESTAMP,
            loaded_at TIMESTAMP
        )
    """)


    conn.execute("""
        INSERT INTO raw_payments VALUES
            (5001, 1001, 'credit_card', 2500, 'paid',
             '2026-09-01 10:10:00', '2026-09-01 10:10:00', CURRENT_TIMESTAMP),


            (5002, 1002, 'upi', 4500, 'paid',
             '2026-09-02 11:40:00', '2026-09-02 11:40:00', CURRENT_TIMESTAMP),


            (5003, 1003, 'credit_card', 3200, 'pending',
             '2026-09-03 14:30:00', '2026-09-03 14:30:00', CURRENT_TIMESTAMP),


            (5004, 1004, 'debit_card', 1800, 'paid',
             '2026-09-04 17:00:00', '2026-09-04 17:00:00', CURRENT_TIMESTAMP),


            (5005, 1005, 'upi', 5000, 'refunded',
             '2026-09-05 09:30:00', '2026-09-05 09:30:00', CURRENT_TIMESTAMP),


            (5006, 1006, 'credit_card', 2750, 'paid',
             '2026-09-06 13:25:00', '2026-09-06 13:25:00', CURRENT_TIMESTAMP)
    """)


    print("Raw tables created successfully.")


    print("\nRAW CUSTOMERS:")
    print(conn.execute("SELECT * FROM raw_customers").fetchall())


    print("\nRAW ORDERS:")
    print(conn.execute("SELECT * FROM raw_orders").fetchall())


    print("\nRAW PAYMENTS:")
    print(conn.execute("SELECT * FROM raw_payments").fetchall())


    conn.close()




if __name__ == "__main__":
    create_raw_tables()
