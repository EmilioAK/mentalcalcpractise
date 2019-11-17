import time
import random

def mentalcalc(question, correct):
    start = time.time()
    answer = eval(input(question))
    end = time.time()

    answer_time = end-start

    if answer == correct:
        return answer_time
    else:
        return 0

questions = [["5+2= ", 7], ["6+2= ", 8], ["4+2= ", 6], ["7+2= ", 9], ["8+7= ", 15], ["5+7= ", 12], ["5+8= ", 13], ["6+7= ", 13], ["8+6= ", 14]]
random.shuffle(questions)

#-------------

total_solve_time = 0
for question in questions:
    solve_time = mentalcalc(question[0], question[1])
    if solve_time == 0:
        print("Wrong. Start over.")
        # Brings it back to 0 so I can make this the condition for faliure in the last if
        total_solve_time = 0
        break
    else:
        total_solve_time += solve_time
        print(str(total_solve_time) + " seconds of solve time")

if total_solve_time:
    print("\nTotal time: " + str(total_solve_time))