""" 
    행인덱스 & 열이름 일부 변경하기
    - 메서드 renmae()
"""

#모듈 로딩
import pandas as pd
import numpy as np

# #데이터 준비.
# dataM = open(r'../DATA/member.csv', 'r', encoding = 'utf-8')
# dataDF1 = dataM.readlines()
# print(dataDF1)
data = [[17, '남', '덕영고'], [15,'여', '대구중']]
##데이터프레임 생성

dataDF1 = pd.DataFrame(data)

print(dataDF1)


#데이터 프레임의 인덱스와 컬럼명 설정.
# 인덱스 : 학생1, 학생2
# 컬럼즈 : 연력, 성별, 학교.
dataDF1.columns = ['연령', '성별', '학교']
dataDF1.index = ['학생1', '학생2']

print(dataDF1)


# 인덱스 : 학생1> 학생01
# 컬럼즈 연령> 나이
# dataDF1.index[0] = '학생01'
# dataDF1.columns[0] = '나이'
# TypeError: Index does not support mutable operations
# dataDF2 = dataDF1.rename(, inplace=False)
dataDF2 = dataDF1.rename(index={'학생1':'학생01'}, columns={'연령':'나이'}, inplace=False)
#원본 대신 새로운 데이터프레임을 반환하므로
#새로운 데이터프레임을 저장하여 출력.
print('DF1', dataDF1)
print()
print('DF2',dataDF2)

dataDF3 = dataDF1.rename(index={'학생1':'학생01'}, columns={'연령':'나이'}, inplace=True)
print('DF3',dataDF3)               
#True 일  경우 원본을 수정하므로 반환값이 없다.
#none 반환.
print()
print('DF1',dataDF1)

print(dataDF1.T)