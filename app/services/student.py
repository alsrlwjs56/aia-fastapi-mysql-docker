from app.models.student import Student
class StudentService (object):
    def __init__(self) -> None:
        pass
    
    def average(self,name,korean,english,math,count):
        avera = Student(name,korean,english,math,count)
        
        print(f'이름:',{avera.name})
        print(f'국어:',{avera.korean})
        print(f'영어:',{avera.english})
        print(f'수학:',{avera.math})
        print(f'카운트:',{avera.count})
        print(f'{avera.korean}+{avera.english}+{avera.math}/{avera.count}={avera.ave()}')
        
        