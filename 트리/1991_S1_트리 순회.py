import sys
sys.stdin = open("input.txt", "r")

def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

def inorder(x):
    if x != '.':
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

def postorder(x):
    if x != '.':
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')

N = int(input())
tree = {}

for i in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')