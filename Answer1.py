 def main():
    numbers = []
    while True:
        num = int(input("הכנס מספר שלם: "))
        numbers.append(num)
        if 100 <= abs(num) <= 999:
            break
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    print(f"המספר הגדול ביותר שנקלט: {max_num}")
    print(f"המספר הקטן ביותר שנקלט: {min_num}")

if __name__ == "__main__":
    main()
