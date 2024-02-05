#calculate total and avg marks
rno=input("enter the roll No ")
name=input("enter the student name")
soc=int(input("enter the social marks"))
sci=int(input("enter the science marks"))
mat=int(input("enter the maths marks"))
total=soc+sci+mat
avg=total/3
print("*"*25)
print("student roll number :",rno)
print("student name :",name)
print("marks in social :",soc)
print("marks in science :", sci)
print("marks in maths :",mat)
print("total marks",total)
print("avarage",avg)
print("*"*25)
