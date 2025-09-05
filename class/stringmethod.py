# st = "my name is tisha"

# print(len(st))
# print(str.lower(st))
# print(str.upper(st))
# print(str.capitalize(st))
# print(str.title(st))

# st = "     my name is tisha"
# print(str.strip(st))

# print(str.replace('s','k',2))

# print(st.find("in"))

st = "sun rises in East ß"

# print(len(st))

# print(st.lower())
# print(st.casefold())

# print(st.upper())
# print(st.capitalize())
# print(st.title())
# print(st.strip())
# print(st.replace('s','K',2))
# print(st.find("ini"))
# print(st.startswith("s"))
# print(st.endswith("ß"))
# print(st.split(" ",3))
# print("abc".join("XYZ"))
# print("abc11".isalpha())
# print("123dfd".isdigit())
# print("ssas12".isalnum())
# print("abc".zfill(10))
# print("abc".center(21,"*"))

k = "hello python hello 4545 ddds 545454"

# a = 0
# b = 0
# for i in k:
#     if str(i).isalpha():
#         a+=1
#     elif str(i).isdigit():
#         b+=1
# print("alpha : ",a)
# print("numbers : ",b)

# print(k[5:])
# print(k[:5])
# print(k[5:9])
# print(k[-8:-1])
# print(k[::-1])

s = ""
for i in range(len(k)-1,-1,-1):
    s+=k[i]

print(s)