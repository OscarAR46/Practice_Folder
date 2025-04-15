def calculate_tip():
    bill = float(input("Enter bill amount: $"))
    tip_percent = float(input("Enter tip percentage: "))

    tip = bill * (tip_percent / 100)
    total = bill + tip

    print(f"Tip amount: ${tip:.2f}")
    print(f"Total bill: ${total:.2f}")

    people = input("Split between how many people? (Use enter for none): ")
    if people:
        people = int(people)
        per_person = total / people
        print(f"Each person pays: ${per_person:.2f}")


if __name__ == "__main__":
    calculate_tip()