import re

search_string = "hello world"
pattern = "hello world"

match = re.match(pattern, search_string)

if match:
    print("regex matches")


# email address
pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string = "some.user@example.com"
match = re.match(pattern, search_string)

if match:
    domain = match.groups()[0]
    print(domain)

pattern = "^[a-zA-Z0-9.]+@([a-z.]*\.[a-z]+)$"
email = "tuan193@gmail.com"
match = re.match(pattern, email)

print("True" if match else "False")
print(f"doamin { match.groups()}")