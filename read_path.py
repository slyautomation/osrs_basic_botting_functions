import random


def get_current_path():
    with open(r'C:\Users\i7 8700\Desktop\paths.txt', 'r') as file:
        path_array = []
        data = file.read().replace('\n', '')
        data = data.replace('[','')
        data = data.replace(']', '')
        final = data.split("), ")
        print(final)
        i = 0
        print(len(final))
        while i < len(final):
            x = final[i][final[i].find('x=') + 2: final[i].find('y=') - 2]
            y = final[i][final[i].find('y=') + 2: final[i].find('plane=') - 2]
            path_array.append([int(x), int(y)])
            i += 1
        print(path_array)
    return path_array

def get_current_path_random():
    with open(r'C:\Users\i7 8700\Desktop\paths.txt', 'r') as file:
        path_array = []
        data = file.read().replace('\n', '')
        data = data.replace('[','')
        data = data.replace(']', '')
        final = data.split("), ")
        print(final)
        i = 0
        print(len(final))
        while i < len(final):
            x = final[i][final[i].find('x=') + 2: final[i].find('y=') - 2]
            y = final[i][final[i].find('y=') + 2: final[i].find('plane=') - 2]
            path_array.append([int(x), int(y)])
            i += random.randrange(1, 15)
            if i > len(final):
                i = len(final) - 1
                x = final[i][final[i].find('x=') + 2: final[i].find('y=') - 2]
                y = final[i][final[i].find('y=') + 2: final[i].find('plane=') - 2]
                path_array.append([int(x), int(y)])
                break
        print(path_array)
    return path_array