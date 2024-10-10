int1 = input(("Enter the first number: "))
int2 = input(("Enter the second number: "))
answer = (int(int1) * int(int2))

print(answer)

if int(answer) > 0:
    print("The result is positive")
elif int(answer) < 0:
    print("The result is negative")
elif int(answer) == 0:
    print("The result is both positive and negative")
