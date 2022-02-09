def fruits(tuple_of_fruits):
    chosed_fruits={}
    for fruit in tuple_of_fruits:
        if fruit['shape'] == 'sphere':
            if fruit['mass'] in range(299,601):
                if fruit['volume'] in range(99,501):
                    if fruit['name'] not in chosed_fruits.keys():
                        chosed_fruits[fruit['name']]=1
                    else:
                        chosed_fruits[fruit['name']] += 1
    return chosed_fruits

if __name__ == '__main__':
    output = fruits((
        {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
        {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))
    print(output)