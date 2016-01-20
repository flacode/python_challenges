#function to print a diamond and display it on the screen
def diamond(level):
    for i in range(0, level):
        print ' '*(level-i)+ "*"*i + "*"*(i-1)
    for i in range(level,0, -1):
        print ' '*(level-i)+ "*"*i + "*"*(i-1)

a=input("Number:")
diamond(a)
