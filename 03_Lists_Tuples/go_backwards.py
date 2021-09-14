data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# iterating backwards
# for index in range(len(data)-1, -1, -1):
#     if (data[index]<min_valid) or (data[index]>max_valid):
#         del data[index]

# using reverse function
top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    # print(top_index-index, value)
    if value < min_valid or value > max_valid:
        del data[top_index - index]

print(data)

string = '12345'
print(max(string))