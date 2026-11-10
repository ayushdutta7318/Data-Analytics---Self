import csv;
def main():
    name = input("enter name: ");
    house = input("house: ");
    with open("student_append.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"]);
        writer.writerow({"name": name, "house": house});


if __name__ == "__main__":
    main();