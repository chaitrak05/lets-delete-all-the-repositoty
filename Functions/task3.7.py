#Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
list1[-1:] = list2
print(list1)
