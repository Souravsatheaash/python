#From a list of integers, create a list removing even numbers.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)
