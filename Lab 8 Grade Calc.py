#Name: Cesar Giner
#Lab 8
#10/21/2022
####################################

#importing math method
import math



#function to calculate standard deviation
def calc_std(lyst):
    leng = len(lyst)
    tot = 0
    std = 0
    avg = sum(lyst)/len(lyst)

    for i in range(leng):
        std = lyst[i] - avg
        tot += (std * std)

    tot = tot/len(lyst)
    std = (tot ** .5)
    std = round(std,2)

    return std
    


#function to execute whichever option the user chose,
def execute(user_choice):



    #if user chooses D/d, display the current information
    if user_choice == 'D' or user_choice == 'd':
        
        print('{}{:>15}{:>10}{:>10}{:>10}{:>10}'.format('Type    ','#','min','max','avg','std'))

        print('='.center(60,'='))

        print('{}{:>15}{:>10}{:>10}{:>10}{:>10}'.format('Tests   ',len(tests),min_tests,max_tests,avg_test,std_tests))

        print('{}{:>15}{:>10}{:>10}{:>10}{:>10}'.format('Programs',len(assignments),min_assignments,max_assignments,avg_assignment,std_assignments))
        

        print('\nThe weighted score is  {}'.format(weight_grade))








    # if user chooses 1, add Test score
    if user_choice == '1':
        while(1):
            try:
                test_score = float(input('Enter the new Test score here===> '))
                while test_score < 0:
                    test_score = float(input('Score must be above 0. Enter the new Test score here===> '))
                break
            except:
                print('Invalid Input. Enter a number')

        tests.append(test_score)

   









    #if user choose 2, remove tests score from tests list
    if user_choice == '2':
        while(1):
            try:
                test_score_remove = float(input('Enter the Test score to remove here ==> '))
                while test_score_remove < 0:
                    test_score_remove = float(input('Enter a valid score, above 0. Enter new score here==> '))
                break
            except:
                print('Invalid input. Enter a number.')

        if test_score_remove not in tests:
            print('Could not locate that score to remove')
        else:
            tests.remove(test_score_remove)
            print('Done')
    





    #if user choose 3, clears all value in tests list
    if user_choice == '3':

        tests.clear()
        print('All tests cleared')
           
               
       




    #if user chooses 4, add program score
    if user_choice == '4':

        while(1):
            try:
                assignment_score = float(input('Enter the new Assignment score here===> '))
                while assignment_score < 0:
                    assignment_score = float(input('Score must be above 0. Enter the new Assignment score here===> '))
                break
            except:
                print('Invalid Input. Enter a number')

        assignments.append(assignment_score)




        


    #if user chooses 5, remove a program score from the assignments list
    if user_choice == '5':
        while(1):
            try:
                assignment_score_remove = float(input('Enter the Assignment score to remove here ==> '))
                while assignment_score_remove < 0:
                    assignment_score_remove = float(input('Enter a valid score, above 0. Enter new score here==> '))
                break
            except:
                print('Invalid input. Enter a number.')

        if assignment_score_remove not in assignments:
            print('Could not locate that score to remove')
        else:
            assignments.remove(assignment_score_remove)
            print('Done')
            








    #if user chooses 6, clears all elements in assignments list
    if user_choice == '6':
        assignments.clear()
        print('All assignments cleared')
    






    


#function to calculate the weighted grade
def calc_weight_grade():
    try:
        x = ((sum(tests)/len(tests)) * .6)
    except:
        x = 0.00
    try:
        y =  ((sum(assignments)/len(assignments)) * .4)
    except:
        y = 0.00

    if len(assignments) == 0 and len(tests) == 0:
        weight_grade = 0.00
    elif len(tests) > 0 and len(assignments) == 0:
        weight_grade = sum(tests)/len(tests)
    elif len(tests) == 0 and len(assignments) > 0:
        weight_grade =  sum(assignments)/len(assignments)
    elif len(tests) > 0 and len(assignments) > 0:
        weight_grade = x + y

    weight_grade = round(weight_grade,2)
       
       
    return weight_grade








'''---------------------------------------------------------------------------
MAIN'''

#set default value to start while loop
user_choice = 0
#all valid inputs that user can choose
options = ['1','2','3','4','5','6','D','d','Q','q']

#setting list variables
tests = []
assignments = []

#setting while varaible to stop program if user inputs Q/q
while user_choice != 'Q' and user_choice != 'q':



    #variable to ask user choice
    try:
        user_choice = input('\n{:>22}\n\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignments\n5 - Remove Assignments\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> '.format('GRADE MENU'))
        while user_choice not in options:
            user_choice = input('Error. Please enter a valid option.\n\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignments\n5 - Remove Assignments\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> '.format('GRADE MENU'))
           
    except:
        print('Unknowon Error: user_choice')






    #information variable to display to the user
    try:
        min_tests = min(tests)
    except:
        min_tests = 'N/A'

    try:
        max_tests = max(tests)
    except:
        max_tests = 'N/A'

    try:
        min_assignments = min(assignments)
    except:
        min_assignments = 'N/A'

    try:
        max_assignments = max(assignments)
    except:
        max_assignments = 'N/A'

    try:
        avg_test = sum(tests)/len(tests)
    except:
        avg_test = 'N/A'

    try:
        avg_assignment = sum(assignments)/len(assignments)
    except:
        avg_assignment = 'N/A'

    try:
        std_tests = calc_std(tests)
    except:
        std_tests = 'N/A'

    try:
        std_assignments = calc_std(assignments)
    except:
        std_assignments = 'N/A'
        

    weight_grade = calc_weight_grade()





    #calling execute function, runs whichever 'if' statement corresponds to the user choice variable
    execute(user_choice)
