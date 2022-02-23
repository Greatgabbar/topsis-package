# Shubham Trivedi
# 101903131
# 3COE5

import math
import sys
import pandas as pd
import numpy as np


if len(sys.argv) != 4:
    print('NOT ENOUGH ARG')
    sys.exit()

try:
    filename = sys.argv[1]
    weights = sys.argv[2]
    impact = sys.argv[3]
    weights = weights.split(",")
    weights = [float(x) for x in weights]
    impact = impact.split(",")
except:
    print("INVALID INOUT VALUES")
    sys.exit()
try:
    df = pd.read_csv(filename)
except:
    print("File Not Found")
    sys.exit()
# print(df)
dff = df.iloc[:, 1:].copy(deep=True)
# print(dff)
# arr = np.zeros((r, c-1))
# print(arr)

# for i in range(0, r):
#     arr[i]=arr[i] + df[]
#     print(arr[i])

# Array of rms value of all column
rms = {}
r = len(dff)
c = len(dff.columns)
if c < 3:
    print("Input file must contain three or more columns")
    sys.exit()
if len(weights) != c:
    print("INSUFFICIENT WEIGHTS")
    sys.exit()
if len(impact) != c:
    print("INSUFFICIENT IMPACT VALUES")
    sys.exit()
# print(dff.columns.dtype)
dff.astype(float)
print(df.applymap(np.isreal))
for i in dff:
    dff[i].astype(float)

for i in dff:
    sum = 0
    for j in dff[i]:
        # print(dff[i][j])
        sum = sum+j*j
    rms[i] = sum

for i in rms:
    rms[i] = math.sqrt(rms[i])

# print(rms)

# normalizing values

for i in dff:
    for j in range(0, r):
        # print(dff[i][j], rms[i], dff[i][j]/rms[i])
        dff[i][j] = float(dff[i][j]/rms[i])

# print(dff)
# multiplying by weights

index = 0
for i in dff:
    w = weights[index]
    for j in range(0, r):
        print(dff[i][j])
        dff[i][j] = w*dff[i][j]
    index = index+1

# print(dff)

ideal_best = {}
ideal_worst = {}

index = 0
for i in dff:
    if impact[index] == "+":
        ideal_best[i] = dff[i].max()
        ideal_worst[i] = dff[i].min()
    if impact[index] == "-":
        ideal_best[i] = dff[i].min()
        ideal_worst[i] = dff[i].max()
    index = index+1

# print(ideal_best)

# print(ideal_worst)

edistance_positive = []
edistance_negative = []

for i in range(0, r):
    temp_p = 0
    temp_n = 0
    for j in dff:
        best = ideal_best[j]
        worst = ideal_worst[j]
        # print(dff[j][i], best, worst)
        temp_p = temp_p+(dff[j][i]-best)*(dff[j][i]-best)
        temp_n = temp_n+(dff[j][i]-worst)*(dff[j][i]-worst)
    edistance_positive.append(math.sqrt(temp_p))
    edistance_negative.append(math.sqrt(temp_n))

# print(edistance_positive)
# print(edistance_negative)

# topsis score
pscore = []

for i in range(0, r):
    pscore.append(
        edistance_negative[i]/(edistance_negative[i]+edistance_positive[i]))

# print(pscore)

# finding rank
# array = np.array(pscore)
# order = array.argsort()
# ranks = order.argsort()

rank = {}

pscore_sorted = np.sort(pscore)[::-1]

for i in range(len(pscore_sorted)):
    rank[pscore_sorted[i]] = i+1

# print(rank)
ranks = []

for i in pscore:
    gg = rank[i]
    ranks.append(gg)

print(ranks)
df["TScore"] = pd.Series(pscore)
df["Rank"] = pd.Series(ranks)
print(df)
