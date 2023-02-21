a=3
b=4
#Arithmetic operator 
print("the value of 3+4 is ", 3+4)
print("the value of 3+4 is ", 3-4)
print("the value of 3+4 is ", 3*4)
print("the value of 3+4 is ", 3/4)

#Assignment operator
a=34 
a +=12 #34+12=46
a *=12 #46*12=552
a /=12 #552/12=46.0
print(a)

#comparison operator(true or false return)
# a=(14<7)
# a=(14>7)
# a=(14<=7)
# a=(14>=7)
# a=(14==7)
a=(14!=7)
print(a)

#Logical operator
bool1=True
bool2=False
print("The value of bool1 and bool2 is ",(bool1 and bool2))
'''bool1 and bool2 true then return true.but bool1 true and bool2 false so return false'''
print("The value of bool1 or bool2 is ",(bool1 or bool2))
'''bool1 and bool2 any one true then return true'''
print("The value of not bool2 is ",(not bool2))
'''return true. bcz return false= true and true = false'''