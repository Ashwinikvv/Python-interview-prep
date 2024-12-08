# create an empty list
l1 = []
n = int(input("enter number of elements required: "))
# creating a list using loop
for i in range(0, n):
	element = int(input())
	# appending elements to the list
	l1.append(element)
print("Original List:", l1)

# sorting in decending
for i in range(0, len(l1)):
for j in range(i+1, len(l1)):
	if l1[i] <= l1[j]:
	l1[i], l1[j] = l1[j], l1[i]
	
# sorted list
print("Sorted List", l1)
