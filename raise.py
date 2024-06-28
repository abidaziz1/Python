def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numeric')
    elif x<0:
        raise ValueError('x must be positive')
    else:
        return x**0.5
def main():
    try:
        x=int(input("Tell me the value of x: "))
        result=sqrt(x)
        print(f"The square root of {x} is {result}")
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)
main()

