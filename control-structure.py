manob_age = 15
anek_age = 20
somchai_age = 25
somsri_age = 30
somsak_age = 35
somyin_age = 20
I_am_handsome = True
fruit = ["apple","banana","mango","orange"]

a=print(somchai_age>anek_age)
b=print(anek_age<somchai_age)
c=print(anek_age==somyin_age)
d=print(somyin_age>=anek_age)
e=print(somyin_age<=somchai_age)
f=print(somsak_age!=somsri_age)
print("mango" in fruit)

print(somsri_age>manob_age and somsri_age>somchai_age)
print(anek_age>=somyin_age or somsri_age<=somsak_age)

age = 17
has_bike_certificate = True

if(age >= 18 and has_bike_certificate):
    print("คุณขับรถได้")
elif(age < 18 and not has_bike_certificate):
    print("คุณขับรถได้แต่โดนตำรวจจับ")
else:
    print("ควรดื่มนมที่บ้าน")

score = 77

if(score >= 80):
    print("คุณได้เกรด A")
elif(score >= 70):
    print("คุณได้เกรด B")
elif(score >= 60):
    print("คุณได้เกรด C")
elif(score >= 50):
    print("คุณได้เกรด D")
else:
    print("คุณได้เกรด F")

