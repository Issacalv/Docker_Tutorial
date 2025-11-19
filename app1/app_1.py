import math
import sys 

if len(sys.argv) == 2:
    userinput = sys.argv[1]
    n = float(userinput)


    try:
        print(f"{n} to the power of 2 = {pow(n,2)}")
    except:
        print("Not a correct input")

else:
    print("Number not provided")
