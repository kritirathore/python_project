t1 = (123,146,235);

for i in t1:
	if(i==146):
		i=134;

li = list(t1);
li[0]="300";		

t1 = tuple(li);
print (t1);

