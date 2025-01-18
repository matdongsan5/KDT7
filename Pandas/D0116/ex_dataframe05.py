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

#데이터 프레임의 인덱스와 컬럼명 설정.
# 인덱스 : 학생1, 학생2
# 컬럼즈 : 연력, 성별, 학교.
dataDF1.columns = ['연령', '성별', '학교']
dataDF1.index = ['학생1', '학생2','학생3', '학생4']

print(dataDF1)

""" 
method) def drop(
    labels: Hashable | Sequence[Hashable] | Index[Any],
    *,
    axis: Axis = ...,
    index: None = ...,
    columns: None = ...,
    level: Level | None = ...,
    inplace: Literal[False] = ...,
    errors: IgnoreRaise = ...
) -> DataFrame
라벨즈 = 인덱스명
drop('학생1') 은 사실 drop(labels='학생1')
drop(labels='학생1', axis=0) 은 drop(columns='학생1')과 같다.
columns를 지정하면 axis를 지정할 필요가 없음.
컬럼명이 지정되었으니까 라벨도 필요 없음.


"""

## 행 삭제
# 학생1 행 삭제.
dataDF2 = dataDF1.drop('학생1', axis=0)
#                                   index 라고 적어도 된다.                                    
print('dataDF2\n', dataDF2)

# 학생2, 학생4 삭제 원본에 적용
dataDF1.drop(['학생2', '학생4'], axis='index', inplace=True)
#                                   index 라고 적어도 된다.                                    
print('dataDF1\n', dataDF1)



## 열 삭제
# 성별 삭제
dataDF4 = dataDF1.drop('성별', axis='columns')
# KeyError: "['성별'] not found in axis"
# axis의 기본값은 0이므로 행에서 먼저 찾는다.
print('dataDF4\n', dataDF4)

#- 연령, 학교 컬럼 삭제
dataDF3 = dataDF1.drop(['연령', '학교'], axis=1)
#                                       columns
print('dataDF1\n', dataDF1)
print('dataDF3\n', dataDF3)
