def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for name in f:
            names = name.split(",")[0]
            cast_list.append(names)
    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for names in cast_list:
    print(names)