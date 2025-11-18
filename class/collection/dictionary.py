st = {
    "name":"Tisha",
    "email":"tisha@gmail.com",
    "language":["gujarati","hindi","english","maths"]
}

# print(st)

# print(st['name'])

# print(st.get('name'))

# st['name'] = "Zeel"
# print(st)

# st.update({"subject":"Python","stram":"IT"})
# print(st)

# print(st['language'][0])

s = dict(name="devanshi",email="devanshi@gmail.com")

# print(s)

# print(s['name'])

# print(s.get('name'))

# print(s.keys())

# print(s.values())

# print(s.items())

# for i in s:
#     print(i)

# for i in s.keys():
#     print(i)

# for i in s.values():
#     print(i)

# for i in s.items():
#     print(i)

# for i,j in s.items():
#     print(i)

# for i,j in s.items():
#     print(j)

# for i,j in s.items():
#     print(i,j)

# s['name1']="tisha"
# print(s)

# s.update({"name":"tisha","phone":"2135698953"})
# print(s)

# s.pop('name')
# print(s)

# s.popitem()
# print(s)

# s.clear()
# print(s)

# x = s.copy()
# print(s)

# del s
# print(s)

students = {
    "zeel":{
        "email":"zeel@gmail.com",
        "phone":"4846623549"
    },
    "ekta":{
        "email":"ekta@gmail.com",
        "phone":"6235489123"
    }
}

# for i,j in students.items():
#     print(i)

# for i,j in students.items():
#     print(j)

# for i,j in students.items():
#     print(i)
#     print(j)

# for i,j in students.items():
#     print(i)
#     for a,b in j.items():
#         print(a,b)

# x = ('key1','key2','key3')
# y = "hello"

# thisdict = dict.fromkeys(x,y)

# print(thisdict)

l = [1,2,3,4,5]
a = 6

k = dict.fromkeys(l,a)
print(k)