from app.models.user import User
class  UserService(object):
    def __init__(self) -> None:
        pass
       
        
    def login(self,id,password):
        user = User(id, password)
        
        print(f'ID:{user.id}')
        print(f'PASSWORD:{user.password}')
        print(f'{user.id}')
        print(f'{user.password}')
       
        
        
        
        
        