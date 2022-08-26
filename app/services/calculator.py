from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        pass
       
        
    def calculate(self,first,second):
        calculator = Calculator(first, second)
        
        print(f'첫번째값:{calculator.first}')
        print(f'두번째값:{calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.sub()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.mul()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.div()}')
        
from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) -> None:
        pass        
        
    def calculate(self,first,second):
        calculator =Calculator(first,second)
        
        print(f'첫번째값:{calculator.first}')
        print(f'두번째값:{calculator.second}')
        print(f'{calculator.first}+{calculator.second}={calculator.sum()}')
        print(f'{calculator.first}-{calculator.second}={calculator.sub()}')
        print(f'{calculator.first}*{calculator.second}={calculator.mul()}')
        print(f'{calculator.first}/{calculator.second}={calculator.div()}')
        
        