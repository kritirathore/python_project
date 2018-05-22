def calculate_bmi(weight, height):
    bmi = weight / height
	
    return bmi
	
def print_category(bmi):
    if(bmi < 18.5):
        print("You are underweight")
    elif(18.5 <= bmi <= 24.9):
        print("You are of normal weight")
    elif(24.9 < bmi < 30):
        print("You are overweight")
    else:
        print("You are obese")
		
username= input(("Your Name Please:"));		
weight = float(input("Enter Weight in kgs:"));
height = float(input("Enter Height in metres:"));

print ("Your BMI is:", calculate_bmi(weight,height));
bmi= calculate_bmi(weight,height);

bmi_res= print_category(bmi);
print(bmi_res);
fp= open("bmi_result.txt","a+");
fp.write(username);
fp.write("\n")
fp.write("%f:"%weight);
fp.write("\n")
fp.write("%f:"%height);
fp.write("\n")
fp.write("%f:"%bmi);
fp.write("\n")
fp.write(bmi_res);
fp.close();