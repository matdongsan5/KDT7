""" 
    DataFrame 에서 행 선택/추출 ==> 가로 한줄 선택
"""
# 1 모듈로딩
import pandas as pd
import numpy as np

# 2 데이터 준비
irisDF = pd.read_csv('../DATA/iris.csv')
print(irisDF)

# 3 데이터 확인
# => 속성: 
print(f"irisDF.index => {irisDF.index}")
print(f"irisDF.columns => {irisDF.columns}")
print()
print(f"irisDF.shpae => {irisDF.shape}")
print(f"irisDF.dtypes => {irisDF.dtypes}")
print()
print(f"irisDF.ndim => {irisDF.ndim}")
print(f"irisDF.axes => {irisDF.axes}")


## 메서드
irisDF.info()

## DataFrame 컬럼별 수치형 컬럼에 대한 통계치 계산 메서드 객체변수명.desc()
print(irisDF.describe())

## DataFrame의 모든 컬럼에 대한
# print(irisDF.describe(include='all'))
# print(irisDF.describe(include='object'))
# print(irisDF.describe([0.25, 0.9], include='float64'))
# print(irisDF.describe([0.25, 0.9], exclude='float64'))

## 4 행 선택/ 추출
##  -> 객체변수명.loc[행인덱스]
##  -> 객체변수명.iloc[행인덱스-정수]
# 1개 행 추출
print('0 이름을 가진 행', irisDF.loc[0])
""" 
Access a group of rows and columns by label(s) or a boolean array.
.loc[] is primarily label based, but may also be used with a boolean array.
## label based  <- 중요.
iris의 index는 0~149로 되어있다.
만약 index가 숫자가 아니라 다른 것이라면.
"""
print('0번째 행.', irisDF.iloc[0])
'''
Purely integer-location based indexing for selection by position.
.iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
## (from 0 to length-1 of the axis)  <- 정수. 레인지나 슬라이싱과 같은 방식. 따라서 -1도 사용가능하다.
'''

# 여러 행 선택 추출
print('loc 0번 행~ 2번행', irisDF.loc[0:2])

irisDF1 = irisDF.rename({0:'Zero', 2:'Two'})
# print(irisDF1)
print('df1.loc 0번 행~ 2번행\n', irisDF1.loc['Zero':3])

print('0번 행~ 4번행', irisDF.iloc[0:4])
#진짜 슬라이싱. [0:4] = [0,1,2,3]



# 행인덱스 일부변경.
irisDF2 = irisDF.rename({0:'Zero',1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five'})
# print(irisDF1)
print('df2.loc 0번 행~ 2번행\n', irisDF2.loc['Zero':6])
print('df2.loc 타입', type(irisDF2.loc['Zero':6]))
