l1 = []
l2 = []
print("how many number is there in list 1  ?")
n1 = int(input())
print("how many number is there in list 2  ?")
n2 = int(input())

for i in enumerate(range(1,n1+1),start=1):
	l1.append(int(input(f"enter number {i} for list 1: ")))

for i in enumerate(range(1,n2+1),start=1):
	l2.append(int(input(f"enter number {i} for list 2: ")))

len_max = max(len(l1),len(l2))

result= []
carry= 0

for i in range(len_max):
	total = l1[i] + l2[i] + carry
	result.append(total%10)
	carry = total // 10
	

if carry:
 result.append(carry)


print(result)