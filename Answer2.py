def is_valid(s):
    if len(s) % 2 == 0:
        return False
    middle_index = len(s) // 2
    return s[0] == s[middle_index] == s[-1]

def main():
    valid_count = 0
    invalid_count = 0
    
    for _ in range(23):
        s = input("Enter a string: ")
        if is_valid(s):
            valid_count += 1
        else:
            invalid_count += 1
    
    print(f"Number of valid strings: {valid_count}")
    print(f"Number of invalid strings: {invalid_count}")

if __name__ == "__main__":
    main()
