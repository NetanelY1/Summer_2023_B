def is_balanced(lst):
    positive_count = 0
    negative_count = 0
    
    for num in lst:
        if num == 0:
            return False
        elif num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    
    return positive_count == negative_count

def main():
    # קולט את המספרים מהמשתמש כמחרוזת אחת
    input_string = input("Enter a list of integers separated by spaces: ")
    
    # מפצל את המחרוזת לרשימה של מחרוזות
    str_list = input_string.split()
    
    # ממיר כל מחרוזת למספר שלם ומכניס לרשימה חדשה
    int_list = []
    for s in str_list:
        int_list.append(int(s))
    
    # בודק אם הרשימה מאוזנת
    if is_balanced(int_list):
        # מדפיס את הרשימה מהתחלה לסוף
        for num in int_list:
            print(num, end=' ')
    else:
        # מדפיס את הרשימה מהסוף להתחלה
        for num in reversed(int_list):
            print(num, end=' ')
    
    print()  # להוסיף שורה ריקה בסוף

if __name__ == "__main__":
    main()
