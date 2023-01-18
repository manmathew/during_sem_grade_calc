import time
class potion:
    def __init__(self, cut = 1, pieces = [], name = None):
        self.percent = cut
        self.name = name
        self.assigns = pieces

def add_sect():
    clasy = potion()
    clasy.name = input("Enter the assignment type: ")
    clasy.percent = int(input("Enter the percentage out of 100 (int only): "))
    listy = []
    inputs = 0
    while type(inputs) == int:
        inputs = input("Enter a grade you'd like to add to the section. Enter a non-int to exit: ")
        if inputs.isdigit(): inputs = int(inputs)
        if type(inputs) == int: listy.append(inputs)
    clasy.assigns = listy

    return clasy

def edit_sect(scheme, index):
    clasy = scheme[index]
    listy = []
    inputs = 0
    while type(inputs) == int:
        inputs = input("Enter a grade you'd like to add to the section. Enter a non-int to exit: ")
        if inputs.isdigit(): inputs = int(inputs)
        if type(inputs) == int: listy.append(inputs)
    clasy.assigns += listy

def read_into_class(file):
    file_open = open(file, 'r')
    class_list = []
    files = file_open.readlines()
    h = 0
    filed = []
    while h < len(files):
        filed.append(files[h].rstrip('\n'))
        h += 1
    class_name = filed[0]
    start_indexes = []
    a = 1
    while a < len(filed):
        if filed[a][0] == '-': start_indexes.append(a)
        a += 1
    list_of_list = []
    b = 0
    while b < len(start_indexes) - 1:
        list_of_list.append(filed[start_indexes[b]:start_indexes[b+1]])
        b += 1
    list_of_list.append(filed[start_indexes[-1]:])
    c = 0
    while c < len(list_of_list):
        temp_list = list_of_list[c]
        temp_clas = potion()
        temp_clas.name = temp_list[1]
        temp_clas.percent = int(temp_list[0][1:])
        grade_lis = []
        for i in temp_list[2:]:
            grade_lis.append(int(i))
        temp_clas.assigns = grade_lis
        class_list.append(temp_clas)
        c += 1
    return (class_name, class_list)
    
def calculate_grade(scheme):
    grade = 0
    a = 0
    while a < len(scheme):
        sum = 0
        current = scheme[a]
        if len(current.assigns) == 0: break
        perc = float(current.percent / 100)
        for i in current.assigns: sum += i
        if sum != 0: port = sum / len(current.assigns)
        else: port = 0
        grade += (port * perc)
        a += 1
    return grade

def write_to_file(name, course, scheme):
    if '.txt' in name: files = open(name, 'w')
    else: files = open(name+'.txt', 'w')
    files.write(course + '\n')
    
    a = 0
    while a < len(scheme):
        tempy = scheme[a]
        files.write('-' + str(tempy.percent) + '\n')
        files.write(tempy.name + '\n')
        if len(tempy.assigns) != 0:
            for item in tempy.assigns:
                files.write(str(item) + '\n')
        a += 1

#print(calculate_grade(read_into_class('test.txt')[1]))

'''
open a file or create a new file
if opening:
    select the object's keybind, create new has a keybind as well
if creating:
    while loop of while input is keybind:
        add new section each time
'''

#scripted_text()

def graphic(grade, schemes):
    grade = round(grade/10)*10
    sum_compare = 0
    for item in schemes:
        if len(item.assigns) != 0: sum_compare += item.percent
    sum_compare = round(sum_compare/10)*10
    print('|', end='')
    a = 0
    while a < grade:
        print('-', end='')
        a += 1
    print('|')
    a = 0
    print('|', end='')
    while a < sum_compare:
        print('-', end='')
        a += 1
    print('|')
    