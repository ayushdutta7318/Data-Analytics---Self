# Modules:

import sys;

# print(sys.argv);
# print(sys.argv[0]);
# print(sys.argv[1]);
# print(sys.argv[2]);
# print(sys.argv[3]);

try:
    print(f"hello, my name is {sys.argv[1]}");
except IndexError:
    print("Too few arguments");

# aliter

if(len(sys.argv) < 2):
    print("Too few arguments");
elif(len(sys.argv)>2):
    print("Too many argument");
else:
    print(f"my name is {sys.argv[1]}");