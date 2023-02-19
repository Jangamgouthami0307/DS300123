Entered_num = int(input("Enter any number :"))
n1, n2 = 0,
sum = 0
if Entered_num <= 0:
    print('Please enter number greater than 0')
else:
    for i in range(0, Entered_num):
        print(sum, end=" ")   
        n1 = n2
        n2 = sum
        sum = n1 + n2
        if sum >= 50:
         break