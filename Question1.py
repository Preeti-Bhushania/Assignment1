s=int(input("Enter starting value:"))
e=int(input("Enter ending value:"))
print("Prime Numbers are-")
for i in range(s,e+1):
	j=2
	while(j<i):
		if(i%j==0):
			break
		j=j+1
	if(i==j):
		print(i)