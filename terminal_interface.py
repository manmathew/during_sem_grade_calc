import calculator
import os
import time
#from simple_term_menu import TerminalMenu
os.system('clear')
list_of_schemes = []

key_bind = ['1','2','3','4','5','6','7','8','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']

course_name = ''

file_name = ''

def new_options():
    list_of_schemes.append(calculator.add_sect())

def editing_options(name):
    os.system('clear')
    print('')
    print(name)
    print('')

    print("Choose an editing option:")
    a = 0
    while a < len(list_of_schemes):
        temp = list_of_schemes[a]
        print('['+ key_bind[a] + '] ' + str(temp.percent) + '% ' + temp.name)
        a += 1
    print('')
    print('[9] New Rule')
    print('[s] Save to file')
    print('[=] Calculate Grade')
    print('[0] Exit')
    print('')
    choice = input("choice:                                             ")
    return choice

print("Are you editing an existing file?")
edit = input("Enter y/n: ")
if edit == 'n' or edit == 'N': edit = False
elif edit == 'y' or edit == 'Y': edit = True
else:
    print("Input Error!")
    exit

def continuing(filename, coursename, list_of_schemes):
    choising = 'A'
    while choising != '0':
        choising = editing_options(coursename)
        if choising == '0':
            os.system('clear')
            break
        elif choising == 's': calculator.write_to_file(filename, coursename, list_of_schemes)
        elif choising == '9':
            if len(list_of_schemes) == len(key_bind) - 1:
                print("You have already reached the max amoung of grading factors!!!")
                time.sleep(3)
            else:
                list_of_schemes.append(calculator.add_sect())
        elif choising == '=':
            grade = calculator.calculate_grade(list_of_schemes)
            os.system('clear')
            print('')
            print('')
            print("Calculated Grade = " + str(grade))
            for i in range(5):
                print('')
            calculator.graphic(grade, list_of_schemes)
            time.sleep(1)
        elif choising not in key_bind:
            print("Please input a valid choice!", end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
            time.sleep(1)
            print('.', end='')
        else:
            indexing = key_bind.index(choising)
            calculator.edit_sect(list_of_schemes, indexing)

if edit == True:
    file_name = input("Enter the filename: ")
    if '.txt' not in file_name: file_name += '.txt'
    tups = calculator.read_into_class(file_name)
    course_name = tups[0]
    list_of_schemes = tups[1]
    continuing(file_name, course_name, list_of_schemes)

else:
    course_name = input("Enter the Course name: ")
    file_name = input("Enter the filename that you'd like to create: ")
    new_options()
    continuing(file_name, course_name, list_of_schemes)

#new_options()
