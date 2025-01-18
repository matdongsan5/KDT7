""" 
    Module
    관련성이 있는 변수, 함수, 클래스를 모아둔 파일.
    -사용법
     import 모듈명   <= 파일 확장자 제외.
     import 모듈명 as 별칭
     from 모듈명 import 변수, 함수, 클래스
     
     -위치
     일반적으로 파일 가장 상단에 import 구문을 기입 - 가독성 고려.
     파일의 어디서든 import 가능함.
"""
# 수학 관련된 기능 필요 --> 내장 모듈 math.py
import math
#임의의 수 추출 모듈 -> random
import random as r

""" 
모듈 내의 변수, 함수, 클래스 사용
-문법: 모듈명.변수명
        모듈명.함수()
        모듈명.클래스 """
        
print(math.tau)
print(math.inf)

# 모듈 내의 함수 사용.
print(math.factorial(8))
print(math.pow(3,9))

# 모듈 내의 클래스 사용
r.Random()
rObjceter = r.Random()  
rObjceter.random()  # 0<= ~ <1.0 범위에 임의의 실수 추출.
print('임의의 실수', rObjceter.random())


