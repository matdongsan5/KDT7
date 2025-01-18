#모듈 로딩
from utills import *

#기능
if __name__ == '__main__':
    # 해당 파일이 실행 될 때.
    # import해서는 사용되지 않음.    
    print('OK')
    print('use.py', __name__)
    
check()

# print('NOT OK')               NOT OK
# print('utills.py', __name__) utills.py utills
# __name__은 사용된 장소로 변경됨.
#uitls.py에서 실행되었다면 __main__이 됨.