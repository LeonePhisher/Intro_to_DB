import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close connection and cursor if they were opened
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
