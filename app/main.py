import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    menu =input('메뉴 선택')
    return menu

def main():
    
    while 1 :
        menu = print_menu()
        if menu == '0':
            print('전체 프로그램을 종료합니다')
            break
        elif menu =='1':
            calculatorservice = CalculatorService()
            first = int(input('첫번째 값 :'))
            second = int(input('두번째 값 :'))
            calculatorservice.calculate(first,second)
            
if __name__ == '__main__':
    main()

