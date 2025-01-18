""" 
Package(패키지)
 - 동일 카테고리에 여러 개의 모듈을 묶어 둔 것.
 - 접근 : 패키지명. 모듈명
 - 사용법 : import 패키지명.모듈명
"""

# import urllib
# ## 기능 코드.
# import urllib.request
# urllib.request.urlopen('http://www.google.co.kr')   
#모듈을 불러와야 함.
#module 'urllib' has no attribute 'request'
#패키지명.모듈명 으로 불러와야 모듈명으로 인식함.
#제대로 불러오지않으면 attribute, 속성으로 인식하여 호출에러발생.

                        
import urllib.request as request
# request.urlopen()
#TypeError: urlopen() missing 1 required positional argument: 'url'
LOGO_URL = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
request.urlretrieve(LOGO_URL, 'logo.png')
