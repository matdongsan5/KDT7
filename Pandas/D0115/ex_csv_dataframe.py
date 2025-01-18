""" 
CSV 데이터 파일을 --> Pandas의 Dataframe으로 읽어들이기

"""
# 모듈 로딩
import pandas as pd #데이터분석용 패키지 로딩

# 전역 변수
# 파일 전체에서 사용되는 변수
DATA_PATH = r'C:\Users\kdt\OneDrive\바탕 화면\KDT7\Pandas\DATA\iris.csv' 

#데이터 읽어 들이기
#1) 일반 파일 읽기 방식.
# 파이썬 내장함수 open
#   open('파일경로,이름', 모드, 인코딩방식)
        # read(), write()
        # close()

#파일 열기
dataF = open(DATA_PATH, 'r', encoding='euc-kr')

#파일에서 읽ㄱ
# all_text = dataF.read()
# print(all_text)

print()

all_line_text = dataF.readlines()
for i in all_line_text:
    print(i.split(','))


#파일 닫기
dataF.close()


    
# with open('..\DATA\iris.csv', 'r', encoding="euc-kr") as files:
#     data = files.readlines()
#     print(data)

# txt = 'Hello, world\n life is too long'    
# with open('test.csv', 'w') as files:
#     files.write(txt)
    
#데이터 읽어 들이기
#2) Pandas 파일 읽기 방식
# Pandas 내장 함수 : read_csv('경로+파일명')
#                   => Dataframe 즉 표 형태로 변환.
##CSV 파일.
dataDF = pd.read_csv(DATA_PATH)
#json -> read_json
#
print(dataDF)