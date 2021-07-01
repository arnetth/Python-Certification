################################################################################
# Author: Hannah Arnett
# Date: 03/07/2021
# This program inputs scores, determines the letter grade for each score, and outputs an average of a list of scores
################################################################################
scores = [] # creates the list of scores
def determine_grade(score): # determines the letter grade for each score
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    elif score >= 0 and score < 60:
        grade = 'F'
    print(f'The letter grade for {score:0.1f} is {grade}.')

def calc_average(scores): # calculates the average of the list of scores
    sum = 0
    count = 0
    for i in range(len(scores)):
        sum += scores[i]
        count += 1
    average = sum/count
    return (average)

def get_valid_score(): # asks user to input scores, rejects if not between 0-100
    while 1:
        score = float(input('Enter a score: '))
        if score > 100 or score < 0:
            print('Invalid Input. Please try again.')
            continue
        break
    return (score)

def main(): # asks for user input, outputs letter grade and calculates average after 5 scores
    for i in range(5):
        score = get_valid_score()
        scores.append(score)
        determine_grade(score)
        if i == 4:
            calc_average(scores)
            avg = calc_average(scores)
            print(f'The average score is {avg:.2f}.')

if __name__ == '__main__':
    main()
