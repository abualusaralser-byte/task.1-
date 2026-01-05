def types_of_number(num):
    if num % 2 == 0:
        return "Even"
    else:
          return "Odd"
def main():
    number = int(input("Enter a number: "))
    result = types_of_number(number)
    print(f"The number {number} is {result}.")
if __name__ == "__main__":
    main()
