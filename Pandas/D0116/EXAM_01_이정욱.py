#1
import pandas as pd
import numpy as np

data = [['김나나', 35, '과장'], ['이민아', '28', '대리']
        ,['박정민', 30, '대리']]

#1-1
dataDF1 = pd.DataFrame(data)
dataDF1.columns = ['이름', '나이', '직급']
print(dataDF1)

#1-2
dataDF1.drop(columns='이름',inplace=True)
print(dataDF1)

#1-3
dataDF1 = pd.DataFrame(data)
dataDF1.columns = ['이름', '나이', '직급']

dataDF1.drop(index=[1,2],inplace=True)
print(dataDF1)


#2
data = [
["037730", "3R", 1510, 7.36],
["036360", "3SOFT", 1790, 1.65],
["005760", "ACTS", 1185, 1.28],
]
columns = ["종목코드", "종목명", "현재가", "등락률"]

#2-1
dataDF2 = pd.DataFrame(data)
dataDF2.columns = columns
print(dataDF2)

#2-2
dataDF2.drop(columns=['현재가', '종목코드'], inplace=True)
#원본 미수정시 False 나 생략
print(dataDF2)

#2-3
dataDF2.drop(index=[2],inplace=True)
print(dataDF2)

#2-4
index = ["037730", "036360", "005760"]
data = [["3R", "1510"],["3SOFT", 1790],["ACTS", 1185]]
columns = ["종목명", "현재가"]

dataDF3 = pd.DataFrame(data, index = index, columns = columns)
# dataDF2.columns = columns
print(dataDF3)

#2-5
dataDF2_5 = dataDF3.drop(index=['037730'])
print(dataDF2_5)

#2-6
dataDF3.drop(index=[index[0],index[2]], inplace=True)
print(dataDF3)

#########3
3-1
fishDF=pd.red_csv('..\DATA\fish.csv')

3-2
irisDF=pd.red_csv('..\DATA\iris.csv')


######4
#4-1
# 클래스는 속성과 메서드로 구성된다.

#4-2
# 객체는 데이터와 데이터를 처리하는 메서드를 묶은 것
# 인스턴스는 클래스를 통해 만들어낸 객체

#4-3
# self는 그 인스턴스가 저장된 메모리주소를 말하며
# self를 매개변수로 하여 해당 메모리주소로 가서
# 인스턴스 속성을 읽고 메서드를 실행한다.

#4-4
#패키지는 모듈의 집합
#특정 기능에 관련된 모듈을 모아서 구성한 것이 패키지다.

#4-5
# import 모듈
# import 모듈.(함수,변수,클래스)
# from 모듈 import 함수, 변수, 클래스, *
# from 패키지 import 모듈
# from 패키지.모듈 import * (모든 것.)
# 패키지.모듈 입력시 똑바로 입력하지 않으면
# 패키지.모듈을 모듈.속성으로 읽어 오류가 난다.
# as 를 붙여 다른 변수명으로 사용할 수 있다.
# import 모듈 as md

#4-6
#__name__은 현재 사용중인 모듈을 가져온다.
# __name__이 저장된 모듈이 그 파일 내에서 직접 사용되면 __main__이지만
# 다른 파일에서 임포트되어 모듈로써 사용되면 해당 모듈 이름을 갖게 된다.

#4-7
# conda install kdt
# pip install kdt