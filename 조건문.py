'''
#123pg
#반복문 복습
money = 3000
card = True
if money>=3600 and card:
    print("택시타고 가라")
else:
    print("걸어가라")
'''

'''
#성적관리 프로그램
#A : 100~91
#B : 90~81
#C : 80~71
#D : 70~61
#F : 60~
#입력 : 점수, 출력 : 등급
score=int(input("점수를 입력하세요: "))
if 100>=score and 91<=score:
    grade="A"
elif 90>=score and 81<=score:
    grade="B"
elif 80>=score and 71<=score:
    grade="C"
elif 70>=score and 61<=score:
    grade="D"
elif 60>=score and 1<=score:
    grade="F"
elif 0>=score:
    grade="z"
print(f'점수 = {score}, 등급={grade}')
if grade=="F":
    print("재수ㅊㅋㅊㅋ")
else :
    print("아 까비 재수 피했누ㅋ")
    '''
import random # random 패키지 사용
num=int(input("숫자를 입력하세요:"))
f=random.randrange(1,20) #1이상 2미만의 숫자를 랜덤 생성
if f==num:
    print("정답")
else:
    print("오답")
print(f"정답 {f}입니다") 
