spam = ['ganyu', 'razor', 'zhongli', 'bennett', 'diona']

def commaCopy(list):
    string = ''
    for i in range(len(list)):
        if i == len(list)-1:
            string += 'and ' + str(list[i])
        else:
            string += str(list[i]) + ', '
    return string


string = commaCopy(spam)
print(string)
