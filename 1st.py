# # print statement
print(2) 

# # floating number 
print(3.5)
# # calculation

print(20*24*60)

# # string concatenations
print("20 days are " + str(50) + " minutes")
# # formatting in string using fstring

print(f"20 days are {50}")
# variable in python 
calculation_second = 24*60*60

print(f"the result is :{calculation_second}")
# # function to calculate
def days_to_units():
    print (f"the new result is :{calculation_second}")

days_to_units()

#input parameters

calculation_to_units = 24
name_of_units = "hours"
custom_message = "status : ok"

def days_to_units(num_of_days):
    print(f"the revised result is {num_of_days} days are :{20 * calculation_second } {name_of_units}")
    print(custom_message)

days_to_units(40)

# scopes : global scopes , local scopes
def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_units)
    print(num_of_days) # can't access scope cause variable defined inside a function
    print(my_var)

scope_check(10)

## user input
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
user_input = input("number of days\n")
print(user_input)

# function with returned value
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"

my_variable = days_to_units(20)
print(my_variable)

# if else statement


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")


user_input = input("number of days\n")
print(user_input)
if user_input > '20':
    print("status is ok")
else:
    print(f"user_input is < {20}")


# try catch
user_input = input("number of days\n")
def days_to_days(user_input):
    print(user_input)
try:
    if int(user_input) > 20:
        print("status is ok")
    elif int(user_input) == 0:
        print("value error : Please provide a valid value")
    else:
        print(f"user_input is < {user_input}")
except ValueError:
    print(f"{user_input} is not valid")

# while loop
def validate_and_execute():
    try:
        user_input_number = int(num_of_days)
        if user_input_number >  0:
            # calculated_value = days_to_units(user_input_number)
            calculated_value = 2+2

            print(calculated_value)
        elif user_input_number == 0:
            print("number is 0 provided")
    except ValueError:
        print("input is strange")

user_input = ""
while user_input != "exit":
    ## list in python and for loop
    user_input = input("what would be your input? \n")
    for num_of_days in user_input.split(","):
        print(user_input.split(","))
        print(num_of_days)
        validate_and_execute()
