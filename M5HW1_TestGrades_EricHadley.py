# Test Grades
# 7/1/2017
# CTI-110 M5HW1 Test Average and Grade
# Eric Hadley

def main():
    
    print ('Please enter five test scores.')
    score1 = int(input('Please enter test score: '))
    score2 = int(input('Please enter test score: '))
    score3 = int(input('Please enter test score: '))
    score4 = int(input('Please enter test score: '))
    score5 = int(input('Please enter test score: '))

    print('Score 1:',determine_grade(score1))
    print('Score 2:',determine_grade(score2))
    print('Score 3:',determine_grade(score3))
    print('Score 4:',determine_grade(score4))
    print('Score 5:',determine_grade(score5))
          
    print('average: ',calc_average(score1, score2, score3, score4, score5 /5)) 
    

def calc_average(score1, score2, score3, score4, score5):
    
    average = (score1 + score2 + score3 + score4 + score5) /5.0
    return average

def determine_grade(score):
    
    if score >= 90:
        letterGrade = 'A'
    else:
        if score >= 80:
            letterGrade = 'B'
        else:
            if score >= 70:
                letterGrade = 'C'
            else:
                if score >= 60:
                    letterGrade = 'D'
                else:
                    if score < 60:
                        letterGrade = 'F'
        

    return letterGrade


# begin program
main()
