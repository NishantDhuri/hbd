list1=[]
c=int(input("Enter the number of elements that you want to insert in List: "))
for i  in range(0,c):
   ele = int(input("Enter the element: "))
   list1.append(ele)
a = int(input("Enter the number that you want to find in List: "))
if a not in list1:
    print("\nThe list does not contain", a )
else:
    print("\nThe list contains", a )