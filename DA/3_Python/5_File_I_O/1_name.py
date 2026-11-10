# file input output
import csv;
def main():
    with open("name_4.csv", "r") as file:
       for line in file:
           row = line.rstrip().split(",");
           print(f"{row[0]} lives in {row[1]}");

    with open("name_4.csv") as file:
       for line in file:
           name, house = line.rstrip().split(","); #list unpacking
           print(f"{name} lives in {house}");

    students = [];
    with open("name_4.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",");
            names_d = {"name": name, "house": house};
            students.append(names_d);

    print(students);

    def get_name(student):
        return student["name"];

    for student in sorted(students, key=get_name):
        print(student);

    def get_house(student):
        return student["house"];

    for student in sorted(students, key=get_house):
        print(student);

    friends_ = [];
    with open("student.csv") as file:
        reader = csv.DictReader(file);
        for line in reader:
            print(f"{line["name"]} lives in {line["house_number"]}");
            friends_.append(line);

    print(friends_);
    for element in sorted(friends_, key=lambda student: student["name"]):
        print(f"{element["name"]} lives in {element["house_number"]}");

    name = input("enter name: ");
    house = input("enter house: ");
    with open("student_append.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house_number"]);
        writer.writerow[{"name":name, "house":house}];



if __name__ == "__main__":
    main()
