# -*- coding: utf-8 -*-

# Exercise 49. 데이터 구조 (튜플)
# a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.

# sol)
tuple_data = ("a", "b", "c", "d", "e")
print(tuple_data[0], tuple_data[-1])

# Exercise 50. 데이터 구조 (튜플)
# 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.

# 실행코드
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'
# 에러

# TypeError                                 Traceback (most recent call last)
# <ipython-input-2-db4a259aad24> in <module>()
#       1 tupledata = ('dave', 'fun-coding', 'endless')
# ----> 2 tupledata[0] = 'david'

# TypeError: 'tuple' object does not support item assignment

# sol)
# 튜플은 불변(Immutable)이기 때문에, 값을 수정할 수 없다.

# Exercise 51. 데이터 구조 (튜플)
# 다음 코드를 읽고, 최종적으로 var1과 var2의 값이 어떤 값이될지 확인해보고, 왜 이렇게 동작하는지 튜플을 기반으로 설명하세요.
# 실행코드
# var1, var2 = 1, 2
# var1, var2 = var2, var1

# sol)
# var1, var2 = 1, 2
# print(var1, var2)
# var1, var2 = var2, var1
# print(var1, var2)

# Exercise 52. 데이터 구조 (튜플)
# 다음 코드에서 두번째 데이터부터 마지막 데이터를 다음과 같이 출력하세요
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

# sol)
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')
print(tupledata[1:])

# Exercise 53. 데이터 구조 (튜플과 리스트)
# 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고, 다시 튜플 데이터로 변환하세요.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

# sol)
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
listdata = list(tupledata)
listdata.append('fun-coding4')
tupledata = tuple(listdata)
print(tupledata)

# Exercise 54. 데이터 구조 (튜플, 리스트, 딕셔너리)
# 비어 있는 튜플, 리스트, 딕셔너리 변수를 하나씩 각각 만드세요.

# sol)
tupledata = tuple()
listdata = list()
dictdata = dict()
print(type(tupledata), type(listdata), type(dictdata))

# Exercise 55. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들고, 딕셔너리 변수의 key 값인 영어단어, value 값인 의미 만을 가진 리스트 변수를 각각 만들고, 두 리스트 변수를 출력하세요.
# 영어단어	의미
# environment	환경
# company	회사
# government	정부, 정치
# face	얼굴
# 출력 예
# {'environment': '환경', 'company': '회사', 'government': '정부, 정치', 'face': '얼굴'}
# ['environment', 'company', 'government', 'face']
# ['환경', '회사', '정부, 정치', '얼굴']

# sol)
dictdata = {"environment": "환경",
            "company": "회사",
            "government": "정부, 정치",
            "face":	"얼굴"}
keylist = list(dictdata.keys())
vallist = list(dictdata.values())
print(dictdata)
print(keylist)
print(vallist)

# Exercise 56. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들어서 다음과 같이 출력하세요.
# 단, 반복문을 사용하세요.
# environment : 환경
# company : 회사
# gonernment : 정부, 정치
# face : 얼굴
# 영어단어	의미
# environment	환경
# company	회사
# government	정부, 정치
# face	얼굴

# sol)
dictdata = {"environment": "환경",
            "company": "회사",
            "government": "정부, 정치",
            "face":	"얼굴"}
print('{:11}{}'.format('영어단어', '의미'))
for k, v in dictdata.items():
    print('{:15}{}'.format(k, v))

print()
print()

# Exercise 57. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들고 외움표시가 X 인 영어단어만 출력하세요
# 단, key는 영어단어, value는 의미와 외움표시 두 데이터를 넣습니다.
# environment : 환경
# company : 회사
# gonernment : 정부, 정치
# face : 얼굴
# 영어단어	의미	외움표시
# environment	환경	X
# company	회사	O
# government	정부, 정치	X
# face	얼굴	X
# 출력 예
# environment
# government
# face

# sol)
dictdata = {"environment": ["환경", 'x'],
            "company": ["회사", 'o'],
            "government": ["정부, 정치", 'x'],
            "face":	["얼굴", 'x']}

for k, v in dictdata.items():
    if v[1] == 'x':
        print(k)

# Exercise 58. 데이터 구조 (딕셔너리)
# 다음 영어 사전 데이터를 딕셔너리 변수로 만들고 사용자로부터 영어단어를 입력받으면 해당 영어단어의 외움표시를 O로 수정하고, 외움표시가 X 인 단어만 출력하는 프로그램을 작성하세요.
# 단, key는 영어단어, value는 의미와 외움표시 두 데이터를 넣습니다.
# environment : 환경
# company : 회사
# gonernment : 정부, 정치
# face : 얼굴
# 영어단어	의미	외움표시
# environment	환경	X
# company	회사	O
# government	정부, 정치	X
# face	얼굴	X
# 입력: government
# 출력
# environment
# face

# sol)
# dictdata = {"environment": ["환경", 'x'],
#             "company": ["회사", 'o'],
#             "government": ["정부, 정치", 'x'],
#             "face":	["얼굴", 'x']}

# data = input()
# dictdata.get(data)[1] = 'o'

# for k, v in dictdata.items():
#     if v[1] == 'x':
#         print(k)

# Exercise 59. 데이터 구조 (딕셔너리)
# 다음 dict_all, dict2, dict3 딕셔너리 변수가 있을 때, dict2와 dict3 두 데이터를 dict_all 딕셔너리 변수에 추가한 후, dict_all 변수를 출력하세요.
# dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
# dict2 = {'company': '회사', 'face':'얼굴'}
# dict3 = {'apple': '사과'}

# sol1)
# dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
# dict2 = {'company': '회사', 'face':'얼굴'}
# dict3 = {'apple': '사과'}
# dict_all.update(dict2)
# dict_all.update(dict3)
# print(dict_all)

# sol2)
dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
dict2 = {'company': '회사', 'face':'얼굴'}
dict3 = {'apple': '사과'}

for k, v in dict2.items():
    dict_all[k] = v

for k, v in dict3.items():
    dict_all[k] = v

print(dict_all)

# Exercise 60. 데이터 구조 (딕셔너리)
# 다음 actor_info 딕셔너리 변수를 만들고, 홈페이지, 배우 이름, 최근 출연 영화 갯수를 다음과 같이 출력하세요
# actor_info = {'actor_details': {'생년월일': '1971-03-01',
#                    '성별': '남',
#                    '직업': '배우',
#                    '홈페이지': 'https://www.instagram.com/madongseok'},
#  'actor_name': '마동석',
#  'actor_rate': 59361,
#  'date': '2017-10',
#  'movie_list': ['범죄도시', '부라더', '부산행']}
# 출력 예:
# 배우 이름: 마동석
# 홈페이지: https://www.instagram.com/madongseok
# 출연 영화 갯수: 3

# sol)
actor_info = {'actor_details': {'생년월일': '1971-03-01',
                                '성별': '남',
                                '직업': '배우',
                                '홈페이지': 'https://www.instagram.com/madongseok'},
              'actor_name': '마동석',
              'actor_rate': 59361,
              'date': '2017-10',
              'movie_list': ['범죄도시', '부라더', '부산행']}
print('배우 이름:', actor_info.get('actor_name'))
print('홈페이지:', actor_info.get('actor_details').get('홈페이지'))
print('출연 영화 갯수:', len(actor_info.get('movie_list')))

# Exercise 61. 데이터 구조 (집합)
# number_list가 다음과 같은 리스트일 때 중복 숫자를 제거한 리스트를 만들고, 출력하세요

# number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]

# sol)
number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]
number_list = list(set(number_list))
print(number_list)