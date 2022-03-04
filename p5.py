#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
lt100 = list()
num_int = 1
while num_int != 0:
 num_str = input("Input an integer (0 terminates):")
 num_int = int(num_str)
 if num_int < 100:
    lt100.append(num_int)
 else:
    lt100.append("Over")
print(lt100)
