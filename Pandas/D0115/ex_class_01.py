""" 
    클래스
    특정 기능을 하기 위한 변수와 하나로 묶어 둔 Type
    제품의 설계도에 비유 /틀
    설계도에 근거해서 만들어진 제품이 바로 객체
    제품이 생성된 상세 클래스 정보를 인스턴스
    
    class exClass:
        class_attr1: 'abc'
        class_attr2: '123'
        #클래스 변수.
        
        
        def __init__(self, attr1, attr2, ...., attrN):
        # __init__ 초기값을 의미. 클래스호출시 실행되는 메서드
        # self = 실행되는 객체, 즉 여기서는 불러오는 인스턴스를 의미
        # JAVA에서의 this.
        # 인스턴스에서 실행되면 각 인스턴스를 의미한다.
        # 첫 매개변수는 self 입력.
        # 각 인스턴스에 저장된 메모리주소를 찾아가서 인스턴스를 시작하라는 의미
        # p1 = person()  # 이 경우 p1에는 메모리주소가 할당되고 그 메모리에는 클래스정보가 기록된다.
                        # p1.~~ 호출시 p1의 메모리에 저장된 클래스정보를 실행하는것.
        # p1.eat() 실행시 p1이 저장된주소 100을 eat(메모리주소=100)으로 처리.
        # eat(self) 이므로 클래스에 저장된 eat()를 실행하게 된다.
        # self. 각 인스턴스의 메모리주소.
        # 그리고 인스턴스 변수들.
        
        self.attr1 = attr1
        self.attr2 = attr2
        
        def class_func1(self):
            return

        def class_method1(self):
            self.class_func1()
            # 클래스 내에서 메서드 호출시의 방식.
            # (각 인스턴스의 메모리주소).메서드()
            # 
            return
            
"""

""" 
    클래스 설계 및 사용
"""

""" 
    설계때 속성. 기능. 변수등을 정해야함
    

    사람 정보를 저장하는 데이터 타입 생성
    클래스 이름: Person
    
    클래스 속성: 클래스 변수(정적 변수):loc
                인스턴스 변수(동적 변수) : name, gender, age, #loc    
    
    클래스 기능: eat(), sleep(), 
    클래스 내의 self:
        클래스 정의 안에서만 사용됨.
        
"""

class Person:
    #클래스 변수/속성 : 정적 변수
    loc = '대한민국'
    
    #메모리(힙)에 속성 저장해주는 기능 메서드 __init__
    def __init__(self , name, gender, age):
        # name, gender, age 인스턴스 변수.
        print('__init__()')
        self.name = name
        self.gender = gender
        self.age = age
        # self.loc = loc
        
    
    #Person 클래스 전용 함수 즉, 메서드
    def eat(self, food='밥'):
        print(f'{self.name}이 {food}를 먹는다')
    
    def sleep(self):
        print('잔다')
        
# james = Person()
# james = Person('james', 'male', 29, 'newyork')
# p1 = Person('홍길동', 12, '남', '대한민국')
# p2 = Person('마징가', 14, '남', '대한민국')
# james.eat()
# james.sleep() 
# print(james.name, james.age)
# print(dir(james))


# Person 인스턴스 속성 읽기와 변경.
# - 읽기 : 객체변수명.속성명.
# - 쓰기 : 객체변수명.속성명 = 새로운값.
p1 = Person('홍길동', 12, '남')
print(f"[현재 이름]: {p1.name}")
p1.name='마파두부'
print(f"[현재 이름]: {p1.name}")
