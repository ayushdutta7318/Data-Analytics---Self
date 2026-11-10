name = "Ayush Dutta";
print(f"my name is {name}");

# input fn
name_ = input("Enter your name: ");
print(f"Good Morning! {name_.capitalize()}");

str_ = "            ayush is my name        ";
print(str_.strip());

print(f"hello, {name_.title()}");

print("hello i am from infdre".split(" "));

# unpacking list:
first_name, last_name = "Ayush Dutta".split(" ");
print(f"first_name: {first_name}\nlast_name: {last_name}");

# OPertators
n_1 = float(input("enter n_1: "));
n_2 = float(input("enter n_2: "));
div_result = round(n_1/n_2, 3);
print(f"Division Rsult: {div_result}");