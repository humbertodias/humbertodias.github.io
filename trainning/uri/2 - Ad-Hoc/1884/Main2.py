# mat = [[0 for i in range(12)] for j in range(12)]
# for i in range(12):
#     for j in range(12):
#         mat[i][j] = float(raw_input())

op = raw_input()
mat = [int(i) for i in raw_input().split(' ')]

sum_above = 0
for i in range(12):
    for j in range(12):
        if j < i:
            sum_above += mat[i][j]

if op == 'S':
    print '%.1f' % (sum_above)
else:
    print '%.1f' % (sum_above / float(66))