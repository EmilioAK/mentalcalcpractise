import time
import random
import math_problems

# Changes the order of the questions. Helps with learning
random.shuffle(math_problems.questions)

def mentalcalc(question, correct):
    start = time.time()
    try:
        answer = int(input(question))
    except ValueError:
        answer = None
    end = time.time()

    answer_time = end-start

    if answer == correct:
        return answer_time
    else:
        return 0

total_solve_time = 0
for question in math_problems.questions:
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