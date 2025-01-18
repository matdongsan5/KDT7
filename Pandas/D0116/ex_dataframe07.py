""" 
    axis => 0
    ||
     1
    
    행 & 열 삭제
    - 메서드 : drop()
     * axis 매개변수: 삭제 방향을 정하는 매개변수
                    axis = 0은 행, axis = 1 은 열
     * inplace 매개변수: True 원본변경(반환 none), False 새로운DF 반환(반환 DF)
"""
#모듈 로딩
import pandas as pd
import numpy as np

# #데이터 준비.
data = [[17, '남', '덕영고'], [15,'여', '대구중'],
        [13, '남', '중앙초'], [19,'남', '성북고']]
##데이터프레임 생성
dataDF1 = pd.DataFrame(data)
print('dataDF1\n', dataDF1)

## 행 삭제 => drop(행인덱스, axis=0, inplace=False)
#                          axis='index'
# 0행 삭제 단, 원본 변경 X
dataDF2= dataDF1.drop(0)
print('dataDF2\n', dataDF2)


# 0번행, 3번행 삭제 단, 원본 변경 X
dataDF3= dataDF1.drop([0,3])
#axis= 0, inplace = False 는 기본값이므로 생략
# 열의 경우에는 axis = 1로 
# 원본변경시에는 inplace = True로
print('dataDF3\n', dataDF3)

print(dataDF1[1].isin(['남']))
print(dataDF1[dataDF1[1].isin(['남'])])


## 열 삭제
# 1번 열 삭제. 원본변경x
dataDF4= dataDF1.drop(1, axis=1)
print('dataDF4\n', dataDF4.values)


# 0번 2번 열 삭제. 원본변경
dataDF1.drop([0,2], axis=1, inplace=True)
print('dataDF1\n', dataDF1)
