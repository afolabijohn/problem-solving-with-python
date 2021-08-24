import random
import sys
question = str(input("DO you want to input the numbers yourself?: "))
if question == 'yes':
    iterator = 0
    while iterator < 5:
        print("ENTER A NUMBER: ")
        iterator += 1
        if iterator == 1:
            element_1 = int(input())
        elif iterator == 2:
            element_2 = int(input())
        elif iterator == 3:
            element_3 = int(input())
        elif iterator == 4:
            element_4 = int(input())
        else:
            element_5 = int(input())
    array_1 = [element_1, element_2, element_3, element_4, element_5]
    print("Array: ", array_1)
elif question == 'no':
    print("we will help you print random numbers")
    array_1 = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]
    print("Array: ", array_1)
else:
    print("Please input either Yes or No ")


def return_list(array_prompt):
    new_element_1 = (array_prompt[4]*array_prompt[3]*array_prompt[2]*array_prompt[1])
    new_element_2 = (array_prompt[4]*array_prompt[3]*array_prompt[2]*array_prompt[0])
    new_element_3 = (array_prompt[4] * array_prompt[3] * array_prompt[1] * array_prompt[0])
    new_element_4 = (array_prompt[4] * array_prompt[1] * array_prompt[2] * array_prompt[0])
    new_element_5 = (array_prompt[1] * array_prompt[3] * array_prompt[2] * array_prompt[0])
    new_list = [new_element_1, new_element_2, new_element_3, new_element_4, new_element_5]
    print("new array is :", new_list)
    sys.exit()


return_list(array_1)