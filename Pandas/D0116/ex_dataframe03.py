""" 
    DataFrame 생성하기 -> 표 만들기
"""
#모듈 로딩
import pandas as pd
import numpy as np

#전역변수
data = [[17, '남', '덕영고'], [15,'여', '대구중']]


##데이터 프레임 만들기
""" 
class DataFrame(
    data: ListLikeU | DataFrame | dict[Any, Any] | Iterable[ListLikeU | tuple[Hashable, ListLikeU] | dict[Any, Any]] | None = ...,
    index: Axes | None = ...,
    columns: Axes | None = ...,
    dtype: ... = ...,
    copy: _bool = ...
)
# 데이터 이외에는 모두 None. 없으면 알아서 번호할당해서 만듬
"""

dataDF = pd.DataFrame(data)
print('dataDF= \n' , dataDF)

#데이터 프레임의 속성 읽기
print('index = ', dataDF.index)
# RangeIndex(start=0, stop=3, step=1)

print('column= ' , dataDF.columns)
# Index(['홍', '마'], dtype='object')

print('values = ', dataDF.values, type(dataDF.values))

print()
dataDF.info()
print()

dataDF2 = pd.DataFrame(data, index = ['홍', '마'], columns = ['나이', '성별', '학교'])
print('dataDF2= \n' , dataDF2)
#데이터 프레임의 속성 읽기
print('index = ', dataDF2.index)
# index =  Index(['홍', '마'], dtype='object')

print('column= ' , dataDF2.columns)
# column=  Index(['나이', '성별', '학교'], dtype='object')
print('values = ', dataDF2.values, type(dataDF2.values))
# value만 뽑아옴. ndarray 타입.
# numpy 는 
#  [[17 '남' '덕영고']
#  [15 '여' '대구중']]
print()
dataDF2.info()
print()

# 데이터프레임의 속성 변경
## - 컬럼명 속성을 영어로 변경
dataDF2.columns = ['age', 'gender', 'school']
print(dataDF2)

## - 행 index 변경
dataDF2.index = ['H01', 'M01']
print(dataDF2)

## 값 변경
# dataDF2.values = [[17, '남', '덕영고'], [15,'여', '대구중']]
# AttributeError: can't set attribute


dataDF2.iloc[:,0] = [31, 27]
print(dataDF2)
