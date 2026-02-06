# l = [10,20,30,40,50,50,"Hello",41.56,True]
# l1 = list((10,20,30,40))
# print(l)
# print(len(l))
# print(l1)

l = ["tisha","sanket","vansh","kajal","shriya"]

# print(l[1])
# print(l[-1])
# print(l[2:4])
# print(l[::-1])

# l[1] = "dhruvin"
# print(l)

# l[1:3] = ["A"]
# print(l)

# l.insert(1,"dhruvin")
# print(l)

# l.append("devanshi")
# print(l)

# k = ["a","1","hello"]
# l.extend(k)
# print(l)

# l.remove("tisha")
# print(l)

# l.pop(1)
# print(l)

# l.pop()
# print(l)

# l.clear()
# print(l)

# del l
# print(l)

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i = 0
# while i<len(l):
#     print(l[i])
#     i += 1

k = []

# for i in l:
#     if 's' in i:
#         k.append(i)
# print(k)

# k=[i for i in l if "s" in i]
# print(k)

# k=[i for i in l if i.startswith('k')]
# print(k)

# k=["a" for i in l]
# print(k)

# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# l.reverse()
# print(l)

# k=l.copy()
# print(k)

# k=list(l)
# print(k)

# k=l[:]
# print(k)

# k=l
# print(k)

a=[10,20,30,10]
b=[100,200,300]

# c=a+b
# print(c)

# a.extend(b)
# print(a)

# print(a.count(10))

# print(a.index(10))

#interview

nums = [5,7,1,3,2,4,9,8]

nums = list(set(nums))      # remove duplicates
nums.sort()

print(nums[-2])  