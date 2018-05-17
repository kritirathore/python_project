l1 = ["hello",1,0.0];
l1.append("bye");
l2=l1[1:3];
del l1[0];
l1.reverse();
print(l1);


t1=("hello",3.5,[1,2]);
for i in t1:
	if(i==[1,2]):
		i.append(2);
		print(i);
print(t1);

list1 = [];

for i in range(0,5):
	number = int(input(" please enter Number"));
	list1.append(number);
print(list1);	
