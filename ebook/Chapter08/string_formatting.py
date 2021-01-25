s = "hello world"
print(s.count('l'))
print(s.find('l'))
# print(s.rindex('m'))

s = "hello world, how are you"
s2 = s.split(' ')
print(s2)
print('#'.join(s2))
print(s.replace(' ', '**'))
print(s.partition(' '))

name = "Dusty"
activity = "writing"
formatted = f"Hello {name}, you are currently {activity}."
print(formatted)


classname = "MyClass"
python_code = "print('hello world')"
template = f"""
public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("{python_code}");
    }}
}}"""

print(template)

