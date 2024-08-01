# הגדרת מחלקת Client עם כל הפעולות
class Client:
    def __init__(self, address, persons, current, prev):
        self.address = address
        self.persons = persons
        self.current = current
        self.prev = prev

    def update_current(self, new_current):
        self.prev = self.current
        self.current = new_current

    def payment(self, rate1, rate2):
        consumption = self.current - self.prev
        discounted_consumption = min(consumption, self.persons * 7)
        regular_consumption = max(consumption - discounted_consumption, 0)
        total_payment = (discounted_consumption * rate1) + (regular_consumption * rate2)
        return total_payment

# פעולה חיצונית לבדוק תשלומים גבוהים מהממוצע
def proposal(arr, num, rate1, rate2):
    total_payment = 0
    count = 0
    payments = []
    
    for client in arr:
        if client.persons == num:
            payment = client.payment(rate1, rate2)
            payments.append((client.address, payment))
            total_payment += payment
            count += 1
    
    if count == 0:
        return  # אין לקוחות עם מספר הנפשות הנדרש
    
    average_payment = total_payment / count
    print(f"Average payment for {num} persons: {average_payment:.2f}")
    
    for address, payment in payments:
        if payment > average_payment:
            print(address)

# יצירת אובייקטים לדוגמה
client1 = Client("123 Main St", 4, 50, 15)  # צריכה של 35 מ"ק, 4 נפשות
client2 = Client("456 Oak St", 4, 60, 25)  # צריכה של 35 מ"ק, 4 נפשות
client3 = Client("789 Pine St", 4, 70, 50)  # צריכה של 20 מ"ק, 4 נפשות
client4 = Client("321 Elm St", 3, 45, 10)  # צריכה של 35 מ"ק, 3 נפשות
client5 = Client("101 Maple St", 4, 100, 70)  # צריכה של 30 מ"ק, 4 נפשות
client6 = Client("202 Birch St", 4, 110, 90)  # צריכה של 20 מ"ק, 4 נפשות
client7 = Client("303 Cedar St", 4, 80, 55)  # צריכה של 25 מ"ק, 4 נפשות
client8 = Client("404 Spruce St", 4, 65, 40)  # צריכה של 25 מ"ק, 4 נפשות

# רשימת הלקוחות
clients = [client1, client2, client3, client4, client5, client6, client7, client8]

# תעריפים לדוגמה
rate1 = 10  # תעריף מוזל
rate2 = 20  # תעריף גבוה

# בדיקה של פעולה חיצונית
proposal(clients, 4, rate1, rate2)
