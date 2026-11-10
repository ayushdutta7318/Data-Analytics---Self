# # Conditionals:

# x = int(input("enter x: "));
# y = int(input("enter y: "));

# if(x>y):
#     print(f"x>y");
# elif(x<y):
#     print(f"x<y");
# else:
#     print(f"x==y");

# # Q. Even or Odd:
# num = int(input("enter num: "));

# if((num % 2)==0):
#     print(f"{num} is even");
# else:
#     print(f"{num} is odd");

# match statemenmt:
name = input("Enter name: ");
match name:
    case "ayush" | "rohan" | "harry":
        print("indore");

    case "sarah" | "rohini" | "alice":
        print("mumbai");

    case _:
        print("invalid name");
