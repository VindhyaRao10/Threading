import json
import threading
import mysql.connector


# Creating database on MYSQL:
"""
1. CREATE DATABASE assignment_db;
2. USE assignment_db;
3. CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, middlename VARCHAR(255), username VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL, phonenumber VARCHAR(15),userId VARCHAR(255) UNIQUE NOT NULL, department VARCHAR(255));
"""


# Function to read JSON file
def read_json_file(filename):
    data = [] # the following is done as the user data in the JSON file is stored as separate objects, and storing them in an array can make it easier to read as a dictionary.
    with open(filename, 'r') as f:
        for line in f:
            user_data = json.loads(line.strip()) # line.stripo is used as the JSON objects in the file are separated by new line. 
            data.append(user_data)
    return data


# Function to insert records into MySQL database
def insert_into_mysql(data): 
    connection = mysql.connector.connect(
        user = 'root',
        host = 'localhost',
        password = 'Vindhya29!',
        database = 'assignment',
        port = 3306
    )

    cursor = connection.cursor()
    
    for record in data:
        # print(record)
        query = "INSERT INTO users (firstname, lastname, middlename, username, password, phonenumber, userId, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute( query, 
                (record['firstname'],
                record['lastname'],
                record['middlename'],
                record['username'],
                record['password'],
                record['phonenumber'],
                record['userId'],
                record['department'])
            )

    connection.commit()
    connection.close()


# Main function
def main():
    
    json_filename = 'user_data.json'
    data = read_json_file(json_filename)

    num_threads = 4
    chunk_size = len(data) // num_threads
    
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)] # creates chunks of data and slices the data based on the numer of threads that is given.

    threads = []
    
    for chunk in data_chunks:
        thread = threading.Thread(target=insert_into_mysql, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        

if __name__ == "__main__":
    main()