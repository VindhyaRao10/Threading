import mysql.connector
import threading

# Function to get data from the database created.
def get_user_data(username, department):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vindhya29!",
            database="assignment",
            port=3306
        )

        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = %s AND department = %s"
        cursor.execute(query, (username, department))

        # fetchone() method - returns the data from the result row 
        result = cursor.fetchone()
        if result:
            print(f"Data for {username} in {department}: {result}")
        else:
            print(f"No data found for {username} in {department}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def main():
    usernames = input("Enter usernames: ").split(", ")               # takes multiple inputs and separates each using the ","
    departments = input("Enter departments: ").split(", ")
    
    if len(usernames) != len(departments):
        print("Enter the right Inputs")
        

    threads = []

    # Thread created to fetch the username and department for multiple inputs from the database
    for username, department in zip(usernames, departments):      # 'zip' this method pairs two list as one tuple, here it is (user,department)
        thread = threading.Thread(target=get_user_data, args=(username, department))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()