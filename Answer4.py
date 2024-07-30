class FlowerPackage:
    def __init__(self, type, price, num=2000, time=12):
        self.type = type
        self.num = num
        self.time = time
        self.price = price

def compensation(arr, flyTime):
    total_losses = 0
    for package in arr:
        if package.time < flyTime:
            loss = package.num * package.price
            print(f"Package of {package.type} with {package.num} flowers won't survive the flight.")
            print(f"Loss: {loss}")
            total_losses += loss
    print(f"Total losses: {total_losses}")


# יצירת חבילות פרחים
package1 = FlowerPackage("Roses", 1.5)
package2 = FlowerPackage("Tulips", 2.0)
package3 = FlowerPackage("Lilies", 1.8, 1500, 10)
package4 = FlowerPackage("Daisies", 1.2, 1800, 15)  # יישרדו את הטיסה
package5 = FlowerPackage("Sunflowers", 1.0, 2500, 14)  # יישרדו את הטיסה


# רשימת חבילות
packages = [package1, package2, package3, package4, package5]

# זמן טיסה
flight_time = 13

# חישוב ההפסד
compensation(packages, flight_time)
