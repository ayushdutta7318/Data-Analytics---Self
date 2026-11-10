class Wizard:
    def __init__(self, name):
        self.name = name;

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name);
        self.house = house;

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name);
        self.subject = subject;

def main():
    ayush = Student("ayush", "house_3");
    print(ayush.house);

if __name__ == "__main__":
    main();