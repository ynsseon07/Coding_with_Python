import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

gamdok = 0

for i in range(len(A)):
    students = A[i]

    gamdok += 1
    students -= B
    if students <= 0 : continue

    gamdok += students // C
    if (students % C) != 0 :
        gamdok += 1

print(gamdok)