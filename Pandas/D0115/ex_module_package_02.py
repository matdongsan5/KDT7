""" 
    Module
    관련성이 있는 변수, 함수, 클래스를 모아둔 파일.
    -사용법
     import 모듈명   <= 파일 확장자 제외.
     import 모듈명 as 별칭
     from 모듈명 import 변수, 함수, 클래스
     from 모듈명 import * (모든 변수, 함수, 클래스)
                        # 안 될 때 잇음.
     
     -주의점
     파일 내에 동일한 변수, 함수, 클래스 존재시
     덮어씌워진다.
     
     
     -위치
     일반적으로 파일 가장 상단에 import 구문을 기입 - 가독성 고려.
     파일의 어디서든 import 가능함.
"""
#수학모듈에서 팩토리얼만.
from math import factorial
from math import *

print('4!', factorial(4))

##전역변수 선언
pi = '삼점일사'

##사용자 정의 함수
def factorial(x):
        print('my facto')

        
print('4!', factorial(4))