# replace in strings:
import re;

url = input("enter url: ").strip().lower();
username = url.replace("https://www.google.com/", "");
print(f"username: {username}");

username = re.sub(r"^(https?://)?(wwww?\.)?google\.com/", "",url);
print(f"username: {username}");

username = re.search(r"^(https?://)?(www?\.)?google\.com/(\w+)$", url, re.IGNORECASE);
print(f"username: {username.group(0)}");
print(f"username: {username.group(1)}");
print(f"username: {username.group(2)}");
print(f"username: {username.group(3)}");