#Create a list of colors from comma-separated color names entered by user.
#Display first and last colors.
color = "y"
color_list = ["Red","Green","White" ,"Black"]
while color!= "x":
 color = input("Enter a color : x Terminates.. ")
 if color != "x":
    color_list.append(color)
print( "%s %s"%(color_list[0],color_list[-1]))
print((color_list[0],color_list[-1]))