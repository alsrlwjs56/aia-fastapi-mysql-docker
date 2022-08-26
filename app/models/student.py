# 클래스에 학생의 이름을 입력하면
# 해당 학생이 얻은 '국어','영어','수학' 3과목의 평균점수에 따라 A - F 가지 출력하시오.
class Student (object):
    def __init__(self, name, korean, english, math, count ) :
        self.korean = korean
        self.english = english
        self.math = math
        self.count = count
        self.name = name
        
    def na(self):
        return self.name 
        
    def ave(self):
        return (self.korean + self.english + self.math) / self.count
    