import os

from psycopg2 import sql

# Connection parameters
db_params = {
    'dbname': 'Library_test',
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': 'localhost',
    'port': '5432'
}

# Sample data to insert
members_data = [
    ('John Doe', 'john.doe@example.com', '1234567890', '123 Elm Street, Springfield', '2024-01-01', '2024-12-31'),
    ('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Oak Street, Springfield', '2024-02-01', '2024-12-31')
]

books_data = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', '1925-04-10', '9780743273565', 5),
    ('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', '1960-07-11', '9780061120084', 3)
]

loans_data = [
    (1, 1, '2024-09-01', None, '2024-09-15', False),
    (2, 2, '2024-09-01', '2024-09-10', '2024-09-15', True)
]

complaints_data = [
    (1, '2024-09-02', 'Book was damaged when received.', 'Resolved'),
    (2, '2024-09-03', 'Late fee was charged incorrectly.', 'Pending')
]

fines_data = [
    (2, 5.00, '2024-09-11', 'Paid'),
    (1, 10.00, '2024-09-16', 'Unpaid')
]

try:
    # Connect to the PostgreSQL database
    connection = sql.connect(**db_params)
    cursor = connection.cursor()

    # Insert data into Members table
    insert_query = """
        INSERT INTO Members (name, email, phone, address, membership_start, membership_end)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, members_data)

    # Insert data into Books table
    insert_query = """
        INSERT INTO Books (title, author, publisher, published_date, isbn, copies)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, books_data)

    # Insert data into Loans table
    insert_query = """
        INSERT INTO Loans (member_id, book_id, issue_date, return_date, due_date, fine_paid)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, loans_data)

    # Insert data into Complaints table
    insert_query = """
        INSERT INTO Complaints (member_id, complaint_date, description, status)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query, complaints_data)

    # Insert data into Fines table
    insert_query = """
        INSERT INTO Fines (loan_id, fine_amount, fine_date, fine_status)
        VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query, fines_data)

    # Commit the transaction
    connection.commit()

except sql.Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
