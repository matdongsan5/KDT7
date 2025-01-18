""" 
    DataFrame 생성하기 -> 표 만들기
"""
#모듈 로딩
import pandas as pd
import numpy as np

#전역변수
data = [[17, '남', '덕영고'], [15,'여', '대구중']]

# dataM = open('../DATA/member.csv', 'r', enconding='euc-kr')

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

dataDF2 = pd.DataFrame(data, index = ['홍', '마'], columns = ['나이', '성별', '학교'])
print('dataDF2= \n' , dataDF2)