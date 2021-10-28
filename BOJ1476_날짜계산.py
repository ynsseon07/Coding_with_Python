import sys

E, S, M  = map(int, sys.stdin.readline().split())
year = 1
year_list = [1] * 3

while True:
    if year_list[0] == E and year_list[1] == S and year_list[2] == M:
        break

    year += 1
    
    if year_list[0] == 15:
        year_list[0] = 1
    else:
        year_list[0] += 1

    if year_list[1] == 28:
        year_list[1] = 1
    else:
        year_list[1] += 1

    if year_list[2] == 19:
        year_list[2] = 1
    else:
        year_list[2] += 1

print(year)