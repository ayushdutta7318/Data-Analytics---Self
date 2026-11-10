# # loops:

# # while:

# i = 1;
# while(i<=5):
#     print(f"Iteration #: {i}");
#     i+=1;

# # for:
# print("\n------FOR LOOP----------\n");
# for i in [1,2,3,4,5]:
#     print(f"Iteration #: {i}");

# print("\n");
# for i in range(1,6):
#     print(f"Iteration #: {i}");

# # break and continue:

# while True:
#     n = int(input("enter n: "));
#     if n>10:
#         break;


# def main():
#     meow(3);
#     get_number();

# def meow(n):
#     for _ in range(n):
#         print("meow");

# def get_number():
#     while True:
#         n = int(input("enter n: "));
#         if n>10:
#             return;

# main();

# loop and list
students = ["ayush", "rohan", "harry"]
for elements in students:
    print(elements)

for index in range(len(students)):
    print(f"student #{index+1}: {students[index]}")

# loop and dictionary
address = {
    "house_1": "ayush",
    "house_2": "harry",
    "house_3": "rohan",
}

for element in address:
    print(f"{element}: {address[element]}");

def pattern(n):
    for i in range(n):
        print("*"*(i+1));

pattern(5);


def print_quad(n):
    for _ in range(n):
        print_line(n);

def print_line(n):
    print("*"*n);

print_quad(5);

def print_hollow(n):
    for i in range(n):
        if(i==0 or i==(n-1)):
            print("*"*n);
        else:
            print("*", " "*(n-4), "*");

print_hollow(5);
print("-----------------------")
print_hollow(10);
print("-----------------------")
print_hollow(15);

print("ayush" + " "+"dutta")