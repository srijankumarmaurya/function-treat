print("--------------------------------------")
print("--------------------------------------")
print("Welcome to the Data Analyzer Program ")
print("--------------------------------------")
print("--------------------------------------")
print()

# =====================================================================
# SAMPLE DATA & STORAGE
# =====================================================================
sample_data_1darray = [910, 20, 30, 40, 50, 60, 20, 1863, 12, 123, 50]
sample_data_2darray = [[200, 123, 120], [150, 260, 52], [300, 500, 422]]  # Fixed formatting to be an actual 2D array matrix
active_data1 = sample_data_1darray.copy()
active_data2 = sample_data_2darray.copy()

array_data = []


def input_data():
    """This function allows the user to input data into the program.

    It provides options for creating a 1D array, a 2D array, or using preloaded
    sample data. The function uses global variable 'array_data' to store the
    input data.
    """
    global array_data
    print("1. Create a 1d array")
    print("2. Create a 2d arryay")
    print("3. Use a sample data ")

    raw_subchoice = input("Select your choice from 1-3: ")

    if not raw_subchoice.isdigit():
        print("Invalid choice input! please select choice from 1 to 3 only!")
        return
    sub_choice = int(raw_subchoice)

    if sub_choice == 1:
        array_data = [
            int(x) for x in input("Enter data (separated by spaces): ").split()]
        print(array_data)

    if sub_choice == 2:
        row = int(input("Enter the number of row : "))
        column = int(input("Enter the number of column : "))
        dataset = []
        for x in range(row):
            l = []
            for y in range(column):
                num = int(input("Enter the values of 2d array: "))
                l.append(num)
            dataset.append(l)
        array_data = dataset
        print(array_data)

    if sub_choice == 3:
        print("1. Use sample 1d array")
        print("2. Use sample 2d array")
        raw_subchoice = input("Select your choice from 1-2: ")
        if not raw_subchoice.isdigit():
            print(
                "Invalid choice input! please select choice from 1 to 2 only!")
            return
       
        sub_choice = int(raw_subchoice)
        if sub_choice == 1:
            array_data = active_data1
            print("Data has been set to sample 1d array: ", array_data)
        if sub_choice == 2:
            array_data = active_data2
            print("Data has been set to sample 2d array: ", array_data)


def summary(data):
    """This function provides a summary of the data stored in the global
    variable 'array_data' It automatically flattens both 1D and 2D layouts
    gracefully to count totals."""
    sample_2d = conv(data)
    
    if len(sample_2d) == 0:
        print("No data available! Please input data first.")
        return
    else:
        print("Summary of the data entered : ")
        print("Total: ", sum(sample_2d))
        print("Maximum: ", max(sample_2d))
        print("Minimum: ", min(sample_2d))
        print("Average: ", (sum(sample_2d) / len(sample_2d)))


def factorial(n):
    """This function calculates and returns the factorial of a given number n
    using the recursive method."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_calculation():
    """This function manages user console inputs to calculate factorials safely
    using integer items."""
    num = int(input("Enter a number to calculate its factorial: "))
    if num <=1:
        print("Factorial is not defined for negative numbers.")
        return
    output = factorial(num)
    print(f"The factorial of {num} is: {output}")


def filter_data(data):
    """This function filters the data entered by the user based on a threshold
    value.

    It uses a Lambda function to filter the data and returns a list of values
    greater than the threshold.
    """
    if len(data) == 0:
        print("No data available! Please input data first.")
        return []
    else:
        threshold = int(input("Enter the threshold value: "))
        working_data = conv(data)

        final_result = list(filter(lambda x: x > threshold, working_data))
        print(
            f"Filtered data (values greater than {threshold}): {final_result}"
        )
        print()


def sort_data(data):
    """This function sorts the data entered by the user in both ascending and
    descending order.

    It handles both 1D and 2D data layouts gracefully and returns two lists:
    one sorted in ascending order and the other sorted in descending order.
    """
    print("1. Ascending data")
    print("2. Decending data")
    choice = int(input("Select your choice from 1-2: "))
    
    working_data = conv(data)
    if choice not in [1, 2]:
        print("Invalid choice input! please select choice from 1 to 2 only!")
        return [], []   
    if choice == 1:
     print("Sorting data in ascending order...")
     sorted_data = sorted(working_data)

    elif choice == 2:
     print("Sorting data in descending order...")
     reverse_sorted_data = sorted(working_data, reverse=True)
     print(reverse_sorted_data)


def conv(data):
    """Helper function to flatten multi-dimensional datasets into a simple 1D
    list."""
    if len(data) > 0 and isinstance(data[0], list):
        l = []
        for x in data:
            l.extend(x)
        return l
    else:
        return data


def display_statistics(data):
    """This function automatically flattens data to calculate and return the
    sum, max, min, and average as a tuple."""
    working_data = conv(data)
    if len(working_data) == 0:
        print("No data available! Please input data first.")
        return 0, 0, 0, 0

    total = sum(working_data)
    maximum = max(working_data)
    minimum = min(working_data)
    avg = total / len(working_data)

    return total, maximum, minimum, avg

def keyw(**hat):
    for x,y in hat.items():
        print(x,y)




while True:
    print("Main Menu: ")
    print("1. Input data")
    print("2. Display data summary (Build-in functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter data by threshold (lambda function)")
    print("5. Sort data")
    print("6. Display dataset statistics (return multiple values)")
    print(
        "7. Thank you for using Welcome to the Data Analyzer Program. Goodbye!"
    )
    print()
    choice_input = input("Enter your choice from 1 to 7: ")
    if not choice_input.isdigit():
        print("Invalid choice input! please select choice from 1 to 7 only!")
        continue
    choice = int(choice_input)

    if choice == 1:
        print("--- Function Documentation ---")
        print()
        print(input_data.__doc__)
        print("-------------------------------")
        print()
        input_data()
        print()

    if choice == 2:
        print("--- Function Documentation ---")
        print()
        print(summary.__doc__)
        print("-------------------------------")
        print()
        summary(array_data)
        print()

    if choice == 3:
        print("--- Function Documentation ---")
        print()
        print(factorial_calculation.__doc__)
        print("-------------------------------")
        print()
        factorial_calculation()
        print()

    if choice == 4:
        print("--- Function Documentation ---")
        print()
        print(filter_data.__doc__)
        print("-------------------------------")
        print()
        filter_data(array_data)
        print()

    if choice == 5:
        print("--- Function Documentation ---")
        print()
        print(sort_data.__doc__)
        print("-------------------------------")
        print()
        sort_data(array_data)
        print()

    elif choice == 6:
        print("--- Function Documentation ---")
        print()
        print(display_statistics.__doc__)
        print("-------------------------------")
        print()
        
        if len(array_data) == 0:
            print("No data available! Please input data first.")
        else:
            # 1. Run the function ONCE and capture its multiple return values
            total, maximum, minimum, avg = display_statistics(array_data)
            
            # 2. Pass the captured variables into your keyword print function
            print("--- Dataset Statistics ---")
            keyw(Total=total, Maximum=maximum, Minimum=minimum, Average=avg)
        print()

    if choice == 7:
        print(
            "Thank you for using Welcome to the Data Analyzer Program. Goodbye!")
        break
