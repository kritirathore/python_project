print("Select Operation");
print("1. Add");
print("2. Subtract");
print("3. Multiply");
print("4. Divide");

num1 = int(input("Enter Number 1:"));
num2 = int(input("Enter Number 2:"));

x = input("enter choice 1,2,3,4: ");

if x == '1':
		result=num1+num2;
		print(result);
		
elif x == '2':
		result=num1-num2;
		print(result);
elif x == '3':
		result=num1*num2;
		print(result);	
elif x == '4' :
		result=num1/num2;
		print(result);		
else :
		print("invalid input");
		
		
		
word = "Python";
print(word[0:2]);