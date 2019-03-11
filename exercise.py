
def generate_num_dict(range):
    num_dict = {}
    for num in range:
        if (num % 2 == 0) and (num % 7 == 0):
            num_dict[num] = num * 2
        elif num % 2 == 0:
            num_dict[num] = num + 1
        elif num % 7 == 0:
            num_dict[num] = num - 1
        else:
            num_dict[num] = num
    return num_dict

# test it out
d = generate_num_dict(range(1,51))
for i, num in d.items():
    print('*', i, num)
