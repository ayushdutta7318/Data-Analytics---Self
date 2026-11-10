def main():
    name = input("enter name: ");
    if name.strip() == "":
        print(hello());
    else:
        print(hello(name));

def hello(to="world"):
    return f"hello, {to}";


if __name__ == "__main__":
    main();