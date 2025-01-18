""" 
    DataFrame 생성하기 -> 표 만들기
"""
#모듈 로딩
import pandas as pd
import numpy as np

#전역변수
data = {'홍':[17, '남', '덕영고'],
        '마': [15,'여', '대구중']}

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
##데이터 프레임 만들기
# - Dict 타입의 데이터 ==> DataFrame 생성
# - key 가 컬럼 식별자로 설정(열)
# - value가 세로로, 컬럼값으로 설정.
""" 홍    마
0   17   15
1   남    여
2  덕영고  대구중 """
""" 
List/Tuple 타입의 데이터
     0  1    2
0  17  남  덕영고
1  15  여  대구중 """

dataDF = pd.DataFrame(data)
print('dataDF= \n' , dataDF)
