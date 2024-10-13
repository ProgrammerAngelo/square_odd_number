integer_list = [13, 7, 35, 19, 43]
#add a method to compute the square of odd numbers
squared = [integer ** 2 for integer in integer_list if integer % 2 != 0]
#add a method for displaying the answer
print(squared)