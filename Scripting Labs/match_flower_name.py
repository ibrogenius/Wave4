# match_flower_name
# Method 1
def flower(a):
    x = {}
    with open('flowers.txt') as file:
        for name in file:
            key, value = name.split(': ')
            x[key] = value[:-1]
    return x[a]


username = input("Enter your First [space] Last name only: ")
first = username[0]
print("Unique flower name with the first letter: ", flower(first))

# Method 2
def flower(filename):
    message = input("Enter your First [space] Last name only: ")
    x = []
    with open(filename) as f:
        for name in f:
            if name[0] == message[0]:
                x.append(name)
    return x

x = flower('flowers.txt')
for names in x:
    print(names)