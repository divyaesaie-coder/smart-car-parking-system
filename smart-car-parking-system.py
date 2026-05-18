#Python program for a smart car parking management system taht handles vehicle entry,exit,parking slot management and time tracking
car_num=[]
entry_time=[]
exit_time=[]
slots=5
while True:
	print("1)Entry car:")
	print("2)Exit car:")
	print("3)Show number of slots:")
	print("4)Exit:")
	ch=input("Choose:")
	if ch=="1":
		car=int(input("Enter the car number:"))
		if slots==0:
			print("No place!")
		elif car in car_num:
			print("Invalid!")
		else:
			slots=slots-1
			car_num.append(car)
			entry=float(input("Enter the time:"))
	if ch=="2":
		car=int(input("Enter the car number:"))
		if car in car_num:
			car_num.remove(car)
			slots=slots+1
			exit=float(input("Enter the time:"))
		else:
			print("Car doesn't exist!")
	if ch=="3":
		print(slots)
	if ch=="4":
		print("Have a great day!Visit again!")
		break

