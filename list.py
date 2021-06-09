"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    n = int(input())
    output_list=[]
for i in range(0,n):
    ip=input().split()
    if ip[0]=="print":
        print(output_list)
    elif ip[0]=="insert":
        output_list.insert(int(ip[1]),int(ip[2]))
    elif ip[0]=="remove":
        output_list.remove(int(ip[1]))
    elif ip[0]=="pop":
        output_list.pop()
    elif ip[0]=="append":
        output_list.append(int(ip[1]))
    elif ip[0]=="sort":
        output_list.sort()
    else:
        output_list.reverse()
        
    
