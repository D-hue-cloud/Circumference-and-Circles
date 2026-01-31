import math
d=int(input("Enter diameter of circle:   "))
r=(d//2)
def pi_d(D):
    return math.pi * d
def area(R):
    return math.pi * (r**2)
print("Which would you like?")
print("a) Circumference of said circle")
print("b) Area of said circle")

choice=input("Enter your choice: a / b  \n")

if choice=="a":
    print("The circumference of this circle is", pi_d(d), "...")
elif choice=="b":
    print("The area of this circle is", area(r), "...")
elif choice=="A":
    print("The circumference of this circle is", pi_d(d), "...")
elif choice=="B":
    print("The area of this circle is", area(r), "...")
else:
    print("This is an invalid choice")

print("Thank you so much for using our simple little calculator today!!")
print("We really appreciate it!")
star=input("Please give us a rating out of 5: ( 1 / 2 / 3 / 4 / 5)   \n")
print("Thank you. Your feedback is appreciated!")