def getstudenttype(choice):
	if choice == 2:
		print("Select your type.");
		print("1.Existing");
		print("2.New");
		type_stu = int(input("Enter choice(1/2):"));
		return type_stu
	if choice == 1:
		username = input(("Enter Username:"));
		password = input(("Enter Password:"));
		if username == "admin" and password == "admin@123":
			str_res = print("Login Successfull");
			return str_res
		else:
			str_res = print("Invalid Username and Password");
			return str_res
		
			
				
				
def getstudentdata(choice):
	if choice == 2:
		name = input("Enter Your Full Name:");
		age = input("Enter Your Age:");
		class_no = input("Enter Your Class:");
		roll_no = input("Enter Your Roll No.:");
		fee = input("Enter Your Fees:");
		fp = open("student_data.txt","r+");
		fp.write(name);
		fp.write(age);
		fp.write(class_no);
		fp.write(roll_no);
		fp.write(fee);
		fp.close();
		res_out = print("Registered successfully");
		return res_out

print("Select your category.")
print("1.Admin")
print("2.Student")
print("3.Faculty")

choice1 = input("Enter choice(1/2/3):");
student1 = getstudenttype(choice1);
student = getstudentdata(student1);
