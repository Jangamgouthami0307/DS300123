## 1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

arr = [ 4, 6, 8, 10, 12, 14, 16 ]
n = len(arr)
num = 18
for i in range(0, n): 
    for j in range(i+1, n):
        if((arr[i]+arr[j])==num):
          print(arr[i]," + ",arr[j]," = ",num) 


 ## 2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
 
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    reverseList(A, 0, 5)
    print("Reversed list is")
    print(A)    


 ## 3.Write a program to check if two strings are a rotation of each other?

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
    if (temp.count(string2) > 0):
        return 1
    else:
        return 0
if __name__ == "__main__":
    string1 = "AACD"
    string2 = "ACDA"
    if areRotations(string1, string2):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")


 ## 4.Write a program to print the first non-repeated character from a string?
str = "GOUTHAMIGOUTHAM"
l = len(str)
flag = 0
for i in range(l):
    flag = 0
    for j in range(l):
        if str[i] == str[j] and i != j:
            flag = 1
            break
    if flag == 0:
        print("First non-repeating character is :", str[i])
        break
if flag == 1:
    print("No non-repeating character")


 ## 5.Read about the Tower of Hanoi algorithm. Write a program to implement it.     
  
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    N = 3
    TowerOfHanoi(N, 'A', 'C', 'B')



