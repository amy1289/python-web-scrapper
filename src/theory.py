# variable type
# snake_case 사용
a_string ="like this"
a_number =3
a_float =3.12
a_boolean =False
a_none =None


# sequence type (열거형)
# 1. list (mutable) : common, mutable sequence operation 가능
days = ["Mon","Tue","Wed","Thu","Fri"]       # 대괄호 [ ]
print("Mon" in days, days[0])
days.append("Sat")
print(days)
days.reverse()
print(days)
# 2. tuple (immutable) : common sequence operation 만 가능
days = ("Mon","Tue","Wed","Thu","Fri")       # 소괄호 ( )
# 3. range (나즁에 나옴)
# #. dictionary : { 키 : 값 } 쌍
nico = {                                     # 중괄호 { }
    "name": "Nico",
    "age": 29,
    "korean": True,
    "fav_food": ["Kimchi", "Sashimi"]
}
print(nico["name"])
nico["handsome"] = True
print(nico)


# function의 정의
def say_hello(who="Stranger") :                            # 들여쓰기로 function의 body를 구분
   print("hello", who)
say_hello("Nico") #"Nico"는 parameter, who는 argument (who="Stranger"처럼 default value를 설정할수 있음.)

def minus(a=0, b=0):                     
   return a-b
minus_result=minus(b=5, a=10)
print(minus_result)

def say_info(name,age):
   return f"name : {name}, age : {age}"                     # f(format), {argument}
say_info_result= say_info("Nico",19)
print(say_info_result)


# 조건문 
# if - else
# boolean operations : or, and, not
def age_check(age):
   print(f"you are {age}")
   if age < 18:
      print("you cant drink")
   elif age==18 or age==19:
      print("you are new to this")
   elif age>20 and age<25:
      print("you are still kind of young")
   else:
      print("enjoy your drink")

# for loop
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
for x in days:
   print(x)


# import modules
import math             # math 전부 가져와서 별로
print(math.ceil(1.2))
from math import fsum   # as 별칭 가능
print(fsum([1,2,3]))


