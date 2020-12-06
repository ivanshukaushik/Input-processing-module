import itertools
import re

initial_input = []
initial_rules = []

with open('input_file.txt') as input_file:
    for line in input_file:
        if not line.isspace():
            initial_input.append(line.strip())
initial_input_two = []

for i in initial_input:
    hello = i.split('#')
    initial_input_two.append(hello[0])

stru = 'STRU'
end = 'END'


def cumulative_sum(ind, bin_list):
    cum_sum = 0
    for i, val in enumerate(bin_list):
        if i <= ind:
            cum_sum = cum_sum + val
        else:
            break
    return cum_sum


final_input = []

for value in initial_input_two:
    final_input.append(value.strip('\n'))

number_of_lines = len(final_input)
binary = []

for number in final_input:
    if 'STRU' in number:
        binary.append(1)
    elif 'END' in number:
        binary.append(-1)
    else:
        binary.append(0)

sum_one_bin = []
na = 0

for bin in binary:
    sum_one_bin.append(cumulative_sum(na, binary))
    na += 1

input = {}
level_one = []
level_one_index = []

for i, val in enumerate(final_input):
    if sum_one_bin[i] == 1 and (sum_one_bin[i - 1] == 0 or i == 0):
        temp = val.split()
        input[temp[1]] = {}
        level_one.append(temp[1])
        level_one_index.append(i)

level_one_index.append(len(final_input))
sum_bin_two = []
final_input_two = []
level_two = []
level_two_index = []
level_three = []

for i in range(len(level_one)):
    sum_bin_two.append([])
    final_input_two.append([])
    level_two.append([])
    level_two_index.append([])
    level_three.append([])

for j in range(len(level_one_index) - 1):
    sum_bin_two[j] = sum_one_bin[level_one_index[j]:level_one_index[j + 1]]
    final_input_two[j] = final_input[level_one_index[j]: level_one_index[j + 1]]

for i in range(len(final_input_two)):
    for j, ip in enumerate(final_input_two[i]):
        if sum_bin_two[i][j] == 2 and sum_bin_two[i][j - 1] == 1:
            temp = ip.split()
            level_two[i].append(temp[1])
            level_two_index[i].append(j)
    level_two_index[i].append(len(final_input_two[i]))

for i in range(len(final_input_two)):
    for j, ip in enumerate(final_input_two[i]):
        if sum_bin_two[i][j] == 2 and sum_bin_two[i][j - 1] == 1:
            temp = ip.split()
            if level_two[i].count(temp[1]) > 1:
                input[level_one[i]][temp[1]] = []
                for q in range(level_two[i].count(temp[1])):
                    input[level_one[i]][temp[1]].append([])
            else:
                input[level_one[i]][temp[1]] = {}

final_input_three = []
final_input_four = []
sum_bin_three = []

for i in range(len(level_two)):
    final_input_three.append([])
    sum_bin_three.append([])

    for j in range(len(level_two[i])):
        final_input_three[i].append([])
        sum_bin_three[i].append([])

for i in range(len(final_input_two)):
    for j in range(len(final_input_three[i])):
        final_input_three[i][j] = (final_input_two[i][level_two_index[i][j]: level_two_index[i][j + 1]])
        sum_bin_three[i][j] = (sum_bin_two[i][level_two_index[i][j]: level_two_index[i][j + 1]])

for i in range(len(sum_bin_three)):
    for j, val in enumerate(sum_bin_three[i]):
        for k, su in enumerate(sum_bin_three[i][j]):
            if su == 3 and sum_bin_three[i][j][k - 1] == 2:
                temp = final_input_three[i][j][k].split()
                level_three[i].append(temp[1])
x = 0

for i in range(len(sum_bin_three)):
    for j, val in enumerate(sum_bin_three[i]):
        if 3 in val:
            for k, s in enumerate(val):
                if s == 3 and sum_bin_three[i][j][k - 1] == 2:
                    temp = final_input_three[i][j][k].split()
                    temp[1] = {}

                    input[level_one[i]][level_two[i][j]][x].append(temp[1])
            x = x + 1
x = 0
for i in range(len(sum_bin_three)):
    for j, val in enumerate(sum_bin_three[i]):
        y = 0
        if 3 in val:
            for k, s in enumerate(val):
                if s == 3 and sum_bin_three[i][j][k - 1] == 2:
                    temp = final_input_three[i][j][k].split()
                    input[level_one[i]][level_two[i][j]][x][y][temp[1]] = {}
                    y += 1
            x += 1
z = 0

for i, one in enumerate(final_input_three):
    for j, two in enumerate(final_input_three[i]):
        if 4 in sum_bin_three[i][j]:
            for k, three in enumerate(sum_bin_three[i][j]):
                if three == 4 and sum_bin_three[i][j][k - 1] == 3:
                    temp = final_input_three[i][j][k].split()
                    key = final_input_three[i][j][0].split()
                    input[level_one[i]][key[1]][z][1][level_three[i][1]][temp[1]] = []
            z += 1
z = 0

for i, one in enumerate(final_input_three):
    for j, two in enumerate(final_input_three[i]):
        if 4 in sum_bin_three[i][j]:
            key = final_input_three[i][j][0].split()
            for k, three in enumerate(sum_bin_three[i][j]):
                temp = final_input_three[i][j][k].split()
                if three == 4 and sum_bin_three[i][j][k - 1] == 3:
                    input[level_one[i]][key[1]][z][1][level_three[i][1]][temp[1]].append([])
            z += 1
a = 0

for i, z in enumerate(final_input_three):
    for j, y in enumerate(sum_bin_three[i]):
        for k, x in enumerate(final_input_three[i][j]):
            key = final_input_three[i][j][0].split()
            if type(input[level_one[i]][key[1]]) == dict:
                if k > 0 and final_input_three[i][j][k] != end:
                    temp = x.split()
                    input[level_one[i]][key[1]][temp[0]] = temp[1]

for i, z in enumerate(final_input_three):
    for j, y in enumerate(sum_bin_three[i]):
        for k, x in enumerate(final_input_three[i][j]):
            key = final_input_three[i][j][0].split()
            if type(input[level_one[i]][key[1]]) == list and 4 not in sum_bin_three[i][j]:
                if k > 0:
                    if j > 8:
                        di = final_input_three[i][j][k].split()
                        if len(di) > 1:
                            temp = j - 10
                            input[level_one[i]][key[1]][temp].append({di[0]: di[1]})
                    else:
                        di = final_input_three[i][j][k].split()
                        if len(di) > 1:
                            temp = j - 1
                            input[level_one[i]][key[1]][temp].append({di[0]: di[1]})
            elif type(input[level_one[i]][key[1]]) == list and 4 in sum_bin_three[i][j] and k > 0:
                if sum_bin_three[i][j][k] == 3 and sum_bin_three[i][j][k - 1] == 2:
                    key_one = final_input_three[i][j][k].split()
                elif sum_bin_three[i][j][k] == 3 and sum_bin_three[i][j][k - 1] == 3:
                    tem = final_input_three[i][j][k].split()
                    input[level_one[i]][key[1]][j - 8][0]['GEOM'][tem[0]] = tem[1]
                elif sum_bin_three[i][j][k] == 2 and sum_bin_three[i][j][k] == 2:
                    te = final_input_three[i][j][k].split()
                    if len(te) > 1:
                        input[level_one[i]][key[1]][j - 8].append({te[0]: te[1]})
                elif sum_bin_three[i][j][k] == 4 and sum_bin_three[i][j][k - 1] == 3 and k > 0:
                    key_two = final_input_three[i][j][k].split()
                elif sum_bin_three[i][j][k] == 4 and sum_bin_three[i][j][k - 1] == 4 and k > 0:
                    temper = final_input_three[i][j][k].split()
                    if len(temper) > 1:
                        ind = int((k - 12) / 5)
                        input[level_one[i]][key[1]][j - 8][1]['INIT']['COND'][ind].append({temper[0]: temper[1]})

print(input)