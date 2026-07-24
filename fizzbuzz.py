#FizzBuzz with a twist.
print("Welcome to FizzBuzz!")
def fizzbuzz(num):
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 7 == 0:
        result += "Buzz"
    if result == "":
        if "3" in str(num):
            result = "Almost Fizz"
        else:
            result = str(num)
    return result
limit= int(input("Enter a number: "))
for i in range(1, limit + 1):
    print(fizzbuzz(i))
