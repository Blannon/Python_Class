student = {"name":"John", "email":"jn@gmail.com","age":"17"}
a = student.keys()
print(a)
b = student.values()
print(b)
c = student.items()
print(c)
student["age"]="25"
print(student)
student["email"]="john@gmail.com"
print(student)
student.update({"email":"joho@hotmail.co.ke"})
print(student)
if "name" in student:
    print("yes name is in student")
else:
    print("name not in student")