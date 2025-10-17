import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔹 Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection properly
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
