import mysql.connector
def connect_to_database():
    # Replace the placeholders with your MySQL database credentials
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '12345678',
        'database': 'students',
        'raise_on_warnings': True
    }

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to the MySQL database")
            return connection

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def query_all_rows(connection,table_name):
    try:
        cursor = connection.cursor()

        # Execute a simple query to fetch all rows from the specified table
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        print(f"\nAll rows from {table_name} table:")
        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        print("Connection closed.")

connection=connect_to_database()
while(True):
    print("====MENU====")
    print("1: show all rows")
    print("2: insert a new row")
    print("3: update specific row")
    print("4: delete specific row")
    print("5: exit")
    choice=input("Please choose: ")

    if int(choice)==1:
        if connection:
            query_all_rows(connection,"std_info")
    elif int(choice)==2:
            print("insert")
    elif int(choice)==3:
            print("update")      
    elif int(choice)==4:
            print("delete")  
    elif int(choice)==5:
            print("Bye Bye")
            break

connection.close()
