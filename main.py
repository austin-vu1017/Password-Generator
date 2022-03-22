import random as rd

# global variable that stores all char values
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'.>/?"

def generate_password(length, amount):
    passwords = []

    for i in range(0, amount):
        pw = ""
        for j in range(0, length):
            pw += rd.choice(char)

        passwords.append(pw)

    return passwords

def main():
    print("Password Generator\n")

    # ask users length of each password and how many unique passwords to generate
    pw_length = int(input('Enter the length of each password: '))
    num_of_pw = int(input('Enter how many unique passwords to generate: '))

    # call generate_password function
    collection_of_pw = generate_password(pw_length, num_of_pw)

    for i in range(0, num_of_pw):
        print(collection_of_pw[i])

main()