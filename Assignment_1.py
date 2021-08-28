
# task 2
def print_data_string():
    print("My name is " + name + " and my age is " + str(age))

# task 3


def print_any_data(d1, d2):
    print("data 1 value " + d1 + " and data 2 value is " + d2)

# task 4


def Number_of_decades(age):
    """Calculate the integer part of the age received.

    Arguments: 
        :param age: The age for which decades should be calculated.

    Returns an integer the number of decades lived.
    """
    return age//10


name = input("Enter your name: ")
age = input("Enter your age: ")

print_data_string()
print_any_data(d1=name, d2=age)

# print_any_data(d1=21,d2=53)

number_decades = Number_of_decades(int(age))
print("Number of decades lived ", number_decades)
