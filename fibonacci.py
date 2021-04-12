num=int(input("ENTER THE VALUES HERE :"))
F1,F2=0,1
F3=F1+F2
print("THE VALUE OF FIRST",num, "is");
print(F1)
print(F2)
for i in range (4):
    print(F3)
    F1=F2
    F2=F3
    F3=F1+F2
