import time
import random
import math_problems


def time_user(question, correct_answer):
    start_time = time.time()
    
    try:
        user_answer = int(input(question))
    except ValueError:
        user_answer = None
    
    end_time = time.time()

    answer_time = end_time - start_time

    if user_answer == correct_answer:
        return answer_time
    else:
        return 0


if __name__ == '__main__':
    # Changes the order of the questions. Helps with learning
    random.shuffle(math_problems.questions)

    total_solve_time = 0
    for question in math_problems.questions:
        solve_time = time_user(question[0], question[1])
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
