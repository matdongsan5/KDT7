""" 
    CSV file ==> DataFrame으로 가져오기
    -함 수: pandas.read_csv(파일경로+파일명)

"""
#모듈 로딩
import pandas as pd
import numpy as np

# #데이터 준비.
# dataM = open(r'../DATA/member.csv', 'r', encoding = 'utf-8')
# dataDF1 = dataM.readlines()
# print(dataDF1)

#파일경로 = '파일경로' 해도 됨

dataM = pd.read_csv('..\DATA\member.csv')
print(dataM)