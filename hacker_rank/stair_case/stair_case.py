import sys


n = int(input().strip())
rows = []
for num_hash in range(1,n+1):
    row = []
    num_space = n - num_hash
    row.append(" "*num_space)
    row.append("#"*num_hash)
    rows.append("".join(row))
for row in rows:
    print(row)
