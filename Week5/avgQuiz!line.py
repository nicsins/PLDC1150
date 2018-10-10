import numpy
from library import inUtils as inu
[print(f'the average score for student {student+1} is { numpy.mean(numpy.array([ inu.putPosFloat(f"enter test score for quiZ{quiz+1}  for student {student +1} ") for  quiz in range(inu.posPutInt(f"enter the number quizez of quizes for student #{student+1}"))])):,.2f}')  for student in range (inu.posPutInt("Please enter the number of students"))]



