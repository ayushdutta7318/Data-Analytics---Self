import cowsay;
import sys;
import json;
import requests;

# if(len(sys.argv)==2):
#     cowsay.trex("hello, " + sys.argv[1]);

# with open("9_api.json", "r") as file:
#     data = json.load(file);

# print(data);

# employee_data = '{"name": "Ada","age": 25}';

# emp_data = json.loads(employee_data);
# print(emp_data["name"]);
# print(emp_data["age"]);
# print(emp_data);

if(len(sys.argv) != 2):
    sys.exit();

response = requests.get("https://itunes.apple.com/search?term=SEARCH_TERM" + sys.argv[1]);
print(response.json());
print();
print(json.dumps(response.json()));

print();
result_obj = response.json();

for obj in result_obj["results"]:
    print(obj);