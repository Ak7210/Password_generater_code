# Common imports
import random
import string
import csv
import datetime

# Function to generate password
def codegenerater():
    password = ""
    pass_length = random.randint(8,20)
    mlsc = random.randint(2,4)
    ml_digits = random.randint(2,4)
    for i in range(pass_length):
        if i < mlsc:
            special_chars = "!@#$%^&*"
            password = password + random.choice(special_chars)
        elif i < mlsc + ml_digits:
            password = password + random.choice(string.digits)
        else:
            password = password + random.choice(string.ascii_letters)

    # shuffling the passoword
    password = ''.join(random.sample(password,len(password)))
    return password

# Function to check password
def checkpassword(password):
    if len(password) >= 8 and len(password) <= 32:
        if sum(1 for c in password if c.isupper()) >= 2:
            if sum(1 for c in password if c.islower()) >= 2:
                if sum(1 for c in password if c.isdigit()) >= 1:
                    if sum(1 for c in password if c in string.punctuation) >= 1:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# Main function
# we need to generate the passowrds for given number of users given by the user


#  function for generating number_passwords
def number_passwords():
    number_users = int(input("Enter the number of passwords to be generated: "))
    i = 0
    list_passwords = []
    while i < number_users:
        if(checkpassword(codegenerater())):
            list_passwords.append(codegenerater())
            i += 1
    return list_passwords

# print(number_passwords())

# we have to put the passowords in the csv file and then download it

def csv_file():
    list_passwords = number_passwords()
    current_month = datetime.datetime.now().strftime("%Y-%m")
    filename = f"passwords_{current_month}.csv"
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Password"])
        for i in range(len(list_passwords)):
            writer.writerow([i+1, list_passwords[i]])
    return "CSV file created"

print(csv_file())



# 5


# print("Password: " + checkpassword(codegenerater()))