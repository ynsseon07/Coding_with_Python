x = int(input())

num_list = list(map(int, input().split()))
num_list.sort()
N = num_list[0] * num_list[len(num_list)-1]
print(N)