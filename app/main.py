import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.user import UserService
from app.services.calculator import CalculatorService   

def print_menu():
    print('0. 종료')
    print('1. 계산기')
    print('2. 로그인 프로그램')   # 입력받은 아이디와 비번 콘솔에 출력하기 
    
    menu =input('메뉴 선택')
    return menu

def main():
    
    while 1 :
        menu = print_menu()
        if menu == '0':
            print('전체프로그램종료')
            break
        
        elif menu =='1':
            cal = CalculatorService()
            first = int(input('첫번째 값:'))
            second = int(input('두번째 값:'))
            cal.calculate(first,second)
            
        elif menu =='2':
            userservice = UserService()
            id = input('ID:')
            password = input('PASSWORD:')
            userservice.login(id,password)    
            
if __name__ == '__main__':
    main()

