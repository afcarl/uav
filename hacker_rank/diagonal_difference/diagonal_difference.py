import sys

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

major_diag = []
for i in range(n):
    major_diag.append(a[i][i])

secondary_diag = []
row_length = len(a[0])-1
for i in range(n):
    secondary_diag.append(a[i][row_length-i])

print(abs(sum(major_diag) - sum(secondary_diag)))
