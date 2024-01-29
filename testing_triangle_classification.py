
def classify_triangle(a, b, c): #Sides are taken as a, b, c
    if a<=0 or b<=0 or c<=0 or (a + b <= c) or (b + c <= a) or (c + a <= b):
        return ("Given sides cannot for a triangle")
    if a == b == c:
        return ("This is an equilateral triangle")
    if a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
           return("This is an isosceles right triangle")
        return("This is an isosceles triangle")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
           return("This is a scalene right triangle")
    return("This is a scalene triangle")
def main():#taking user input
    a = float(input("Please enter the length of the first side: "))
    b = float(input("Please enter the length of the second side: "))
    c = float(input("Please enter the length of the third side: "))
    result = classify_triangle(a, b, c)
#diplaying result
    print(result)

if __name__ == "__main__":
    main()
