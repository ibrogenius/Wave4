# user_input_numlist
user_list = []
list_sum = 0

for i in range(10):
    try:
        userInput = eval(input("Enter any 2-digit number: "))
        # check to see if number is even and if yes, add to list_sum
        # print incorrect value warning  when ValueError exception occurs
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number

    except ValueError:
        print("Incorrect value warning when ValueError exception occurs")


print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))