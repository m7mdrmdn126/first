print("hello world")

yes = 11


hello = yes 

print(hello)

if hello == True:
    print("id")
elif hello == False:
    print("gg")
else:
    print("from else")


flist = ["mai", "mai2", "mai3"]

print(flist[-2])

print(0 + 2)

print(len(flist))

flist.append("mai4")

print(flist)
print(flist[2:4])

flist[0] = "mai0"
print(flist)

flist.insert(1, "mai1")
print(flist)

flist.remove("mai2")
print(flist)



flist[0] = ""

print(flist)

del flist[0]

print(flist)

mai_number = 0

while mai_number == 0:
    print(flist)
    mai_number += 3


for i in range(len(flist)):
    print("hello world")

for i in range(3):
    print(flist[i])

for j in flist:
    print(j)


print(range(3))



def do_print(no):
    return no

print(do_print("noth"))


fe = input("enter your name  : ")

print(fe)
