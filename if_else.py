"""Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6to20 , print Weird
If  is even and greater than 20 , print Not Weird
Input Format:
A single line containing a positive integer, .
Constraints
Output Format:
Print Weird if the number is weird. Otherwise, print Not Weird."""

if __name__ == '__main__':
    n = int(input().strip())
if(n%2==0):
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")
else:
    print("Weird")