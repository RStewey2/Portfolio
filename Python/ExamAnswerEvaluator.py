#Program to evaluate answers from an external document and output pass/fail result
def Main():

#print start of program
    print("This program will evaluate answers for a driving exam.")

# set correct answers list    
    correct_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

# call moddule to import the answer file    
    user_answers = get_answers()

# check the answers against the correct answer
    wrong_answer_list = check_answers(user_answers,correct_answers)

# calculate final score
    final_score = (20 - len(wrong_answer_list))

# print results
    print('Your score: ' +str(final_score)+' out of 20.')
    print('Your answered ' +str(20-final_score)+' incorrectly.')
    print('You must score 15 or more to pass.')
    print('Incorrect Answers: ' + str(wrong_answer_list))
   
    if final_score >= 15:
        print('Result: PASS')
    else:
        print('Result: FAIL')

# module to import and display provided answers. 
def get_answers():
    with open('C:/Users/rstew/Documents/school/CSC500/student1.txt') as z:
        student_answers = list(z.read())
    for i in range(9):
        print('0'+ str(int(i+1)) +': '+str(student_answers[int(i)]) + '   |   ' + str(int(i+11)) +': '+str(student_answers[int(i+10)]).upper())
    print('10: '+str(student_answers[int(9)]) + '   |   ' + str(int(20)) +': '+str(student_answers[int(19)]).upper())
    return student_answers

# module to check answers against the correct answers.
def check_answers(x, y):
    wrong_answers = []
    for i in range(20):
        if x[i] != y[i]:
            wrong_answers.append(i+1)

    return wrong_answers

Main()