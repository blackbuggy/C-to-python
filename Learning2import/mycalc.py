def calc_add(a,b):
    c = a+b
    return c
def calc_mul(a,b):
    c = a*b
    return c

def calc_div(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by zero!")

if __name__ == "__main__":
     print("Hello wrold from mycalc.py")