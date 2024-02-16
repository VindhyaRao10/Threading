import json
import random
import string
import threading


def generate_user_data():
    departments = ["IT", "Engineering", "Finance"]
    
    first_name = ''
    for i in range(5):
            first_name += random.choice(string.ascii_uppercase)

    last_name = ''
    for i in range(3):
        last_name += random.choice(string.ascii_uppercase)

    phone_number = "+91 "
    for i in range(10):
        phone_number += random.choice('0123456789')
        
    return {
        "firstname": first_name,
        "lastname": last_name,
        "middlename": random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "username": f"{first_name.lower()}{last_name.lower()}",
        "password": f"{first_name.lower()}{last_name.upper()}{random.choice('@!%&')}{random.randint(1, 100)}",
        "phonenumber": phone_number,
        "userId": f"{first_name}{last_name}@assignment.com",
        "department": random.choice(departments)
    }


# Function to store data in JSON file
def file_JSON(user_data, file_name):
    # a - append mode, this adds data to an existing file and if the file isnt created then it will create the file. Here it is the user_data.json file. Using the append mode as the data is eing added to the file whereas with the use of 'w' mode the data would have been overwritten in the file each time a thread is created, this mode was used and chose the append mode accordingly.
    with open(file_name, 'a') as file:        
        json.dump(user_data, file)
        file.write('\n')   
    
        
# Main Function that calls the other functions and stores data concureently in the user_data.json file. 
def generate_and_write_data():
    threads = [] # a list where all the thread objects are saved 
        
    for i in range(100):   #loops for 100 counts to create that many user_data
        user_data = generate_user_data()
        thread = threading.Thread(target=file_JSON, args=(user_data, 'user_data.json')) # creates a new thread which concurrently runs the file_JSON function with the arguement user_data and this being stored in the user_data.json as in the 'file_JSON' function arguement.
        thread.start() # starts the threading 
        threads.append(thread) # adds the new threads concureently to the thread list 
        
    for j in threads:
        thread.join() # for every thread that is created is stopped by the '.join()', this ensures all the threads are executed before it continues with the program.


#'__name__' method is used as it will run the code-block inside it when this program is executed but when the program is imported elsewhere the code-block in the following will not be executed, this ensures code reusability, testing and debugging. This method was suggested by ChatGPT.
if __name__ == '__main__':
    generate_and_write_data()