import os
import time

import psycopg2

# Database connection parameters
# Connection parameters
db_params = {
    'dbname': 'Library_test',
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': 'localhost',
    'port': '5432'
}

# Define queries
queries = {
    "search_member": "SELECT * FROM Members WHERE name ILIKE '%John%'",
    "search_book": "SELECT * FROM Books WHERE title ILIKE '%Gatsby%'",
    "find_loans": """
        SELECT Members.name, Books.title, Loans.issue_date, Loans.due_date, Loans.return_date
        FROM Loans
        JOIN Members ON Loans.member_id = Members.member_id
        JOIN Books ON Loans.book_id = Books.book_id
        WHERE Loans.return_date IS NULL
    """,
    "list_fines": """
        SELECT Members.name, Loans.loan_id, Fines.fine_amount, Fines.fine_status
        FROM Fines
        JOIN Loans ON Fines.loan_id = Loans.loan_id
        JOIN Members ON Loans.member_id = Members.member_id
    """,
}

# Execute the queries and measure time
try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Execute each query and record the execution time
    for query_name, query in queries.items():
        start_time = time.time()
        cursor.execute(query)
        result = cursor.fetchall()
        execution_time = time.time() - start_time
        print(f"Query: {query_name}, Time: {execution_time:.4f} seconds")
        print(result)

    # Close the connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
