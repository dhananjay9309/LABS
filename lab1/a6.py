def cal(x): 
    try: 
        result = str(5/x) 
        print("You have choose correct value and your ans is "+result) 
    except ZeroDivisionError: 
        print("You haven't choose correct value")

a=int(input("Enter the value: "))
cal(a)

  