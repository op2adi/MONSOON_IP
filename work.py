import psycopg2

db_params = {
    'dbname': 'Library_test',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    print("Connected to the database")

    # Insert a new member
    insert_member_query = """
        INSERT INTO Members (name, email, phone, address, membership_start, membership_end)
        VALUES (%s, %s, %s, %s, CURRENT_DATE, CURRENT_DATE + INTERVAL '1 year')
    """
    member_data = ('Alice Smith', 'alice@example.com', '9876543210', '456 Oak St')
    cursor.execute(insert_member_query, member_data)
    connection.commit()
    print("Member added successfully")

    # Fetch all members
    select_members_query = "SELECT * FROM Members"
    cursor.execute(select_members_query)
    members = cursor.fetchall()
    for member in members:
        print(member)

except Exception as error:
    print("Error:", error)
    if connection:
        connection.rollback()

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Database connection closed")
