# Concurrent Python Programs

## 1. Concurrent User Data Generation and Upload

### Objective:
Generate and upload user data into a JSON file concurrently using Python threads.

### Learnings:
1. **Threading:** A technique to execute multiple tasks simultaneously, enhancing program performance and responsiveness.
2. **Thread Management:** Creating, starting, and stopping threads using appropriate syntax.
3. **Usage of '__name__' Method:** Understanding the role of '__name__' method in managing threads.

### Program Flow:
1. `generate_user_data()`: The function generates random user data based on given attributes and returns a dictionary.
2. `file_JSON()`: Function takes user data and a target JSON file, opens the file and appends the JSON objects.
3. `generate_and_write_data()`: Creates threads, where the target function is `file_JSON()`, with arguments as `generate_user_data()` and the target file.
4. The main function calls and stores 100 randomly generated user data in a JSON file named 'user_data.JSON' in the folder.

---

## 2. Concurrent JSON to MySQL Database Insertion

### Objective:
Read data from a JSON file and insert it into a MySQL database concurrently using Python threads.

### Learnings:
1. **MySQL Connection Setup:** Establishing connections to MySQL, utilizing the `cursor()` command.
2. **Multithreading:** Creating and running threads concurrently to insert chunks of data.
3. **List Comprehension:** Writing commands efficiently using list comprehension.

### Program Flow:
1. `read_JSON_file()`: Reads data from a given JSON file and stores it in an array for easier processing.
2. `insert_into_mysql()`: Establishes a connection with the database and executes insert queries in a loop based on provided data.
3. `main()`: Divides data into chunks based on the number of threads, creating a thread for each chunk for concurrent execution.

---

## 3. Concurrent MySQL Data Retrieval by Username and Department

### Objective:
Read data from a MySQL database and return data based on inputted username and department attributes concurrently using Python threads.

### Learnings:
1. **try_except with finally:** Understanding the try_except structure, incorporating the 'finally' block.
2. **Zip() Method:** Utilizing the `zip()` method to combine lists into a tuple, is beneficial for handling usernames and departments.

### Program Flow:
1. `get_user_data()`: Takes inputted username and department as arguments, connects with the database, reads data, and prints the matching output.
2. `main()`: Prompts for username and department, creates threads to concurrently read and match data from the database, returning the output.

---

## References:
1. [GeeksForGeeks](https://www.geeksforgeeks.org/)
2. [PythonTutorial](https://docs.python.org/3/tutorial/)
3. [ChatGPT](https://beta.openai.com/)
4. [BlackBox](https://www.blackbox.com/)
