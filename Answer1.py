def main():
    numbers = []
    while True:
        num = int(input("Enter an integer: "))
        if 100 <= abs(num) <= 999:
            break
        numbers.append(num)
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    print(f"The largest number entered: {max_num}")
    print(f"The smallest number entered: {min_num}")

if __name__ == "__main__":
    main()
