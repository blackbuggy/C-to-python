import sys
import mycalc

if __name__ == "__main__":


    x = int(sys.argv[1])
    y = sys.argv[2]
    z = int(sys.argv[3])

    if y == "+":
        print(mycalc.calc_add(x, z)) 
    elif y == "*":
        print(mycalc.calc_mul(x, z))
    elif y == "/":
        print(mycalc.calc_div(x, z))
    else:
        print("Invalid operator")
