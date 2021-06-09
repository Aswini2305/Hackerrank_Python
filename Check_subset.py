"""You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False."""
loop=int(input())
def checker():
    size_set_A=int(input())
    set_A=set(map(int,input().split()))
    size_set_B=int(input())
    set_B=set(map(int,input().split()))
    result=set()
    for i in set_A:
        if i in set_B:
            result.add(i)
    if result==set_A:
        print(True)
    else:
        print(False)
for j in range(loop):
    checker()