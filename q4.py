def func():
    #local Var
    x = 10
    print("Inside func():", x)
#global
x = 20
func()
print("Outside func():", x)