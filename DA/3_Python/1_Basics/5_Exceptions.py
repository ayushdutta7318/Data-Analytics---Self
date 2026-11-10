# Exceptions:

# x = int(input("x: "));
# print(f"x is {x}");

# try:
#     y = int(input("y: "));
# except ValueError:
#     print(f"y is not an integer");
# else:
#     print(f"y is {y}");

# while True:
#     try:
#         z = int(input("z: "));
#     except ValueError:
#         print("z is not integer");
#     else:
#         print(f"z is {z}");
#         break;


# fn

def main():
    z = get_int("what is z: ");
    print(f"z is {z}");


def get_int(prompt):
    while True:
        try:
            return int(input(prompt));
        except:
            print("entered value is not an integer!");

main();