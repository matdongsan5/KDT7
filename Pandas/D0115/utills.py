""" 
FILENAME    : utils.py
DESCRIPTION : 데이터 분석에 자주 사용되는 기능의 함수들 관련 모듈
DATE        :2025/01/15
HISTORY     : WRITER        DATE        DESC
                james       25.01.03    print_info() 추가
                james       25.01.03    print_info() 추가
"""

""" 
함수기능: 개발 정보 출력 기능
함수이름: print_info
매개변수: none
리턴값 : none
"""    

def print_info():
    print('---------------')
    print('회사명: KNU')
    print('연락처: 053-123-4567')
    print('버  전: v1.0')
    print('담당자: 홍길동')
    print('---------------')
    
## 함수 호출/사용
import utills
if __name__ == '__main__':
    # 해당 파일이 실행 될 때.
    # import해서는 사용되지 않음.    
    print('OK')
    print('utils.py', __name__)
    
def check():
    if __name__ == '__main__':
    # 해당 파일이 실행 될 때.
    # import해서는 사용되지 않음.    
        print('OK')
        print('utills.py', __name__)
        
    else:
        print('NOT OK')
        print('utills.py', __name__)