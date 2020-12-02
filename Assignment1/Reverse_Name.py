# Reverse Name

def reverse_name(first_name, last_name):
    rev_first = first_name[-1::-1]
    rev_last = last_name[-1::-1]
    print(rev_first+" "+rev_last)


first_name = input("Enter the First Name: \n")
last_name = input("Enter the Last Name: \n")
reverse_name(first_name, last_name)
