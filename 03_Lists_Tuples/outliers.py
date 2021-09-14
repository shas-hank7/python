data = [4, 5, 104, 105, 110, 120, 130, 140, 150, 160, 170, 183, 185, 187,
        188, 191, 350, 350
        ]
print(data)

min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value>min_valid:
        stop = index
        break

del data[:stop]
print(data)

start = 0
for index in range(len(data)-1, -1 ,-1):
    if data[index] < max_valid:
        start = index
        break

del data[start+1:]
print(data)

