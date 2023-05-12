
'''
a=int(input("a를 입력하세요:"))
b=int(input("b를 입력하세요:"))

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
'''
'''
a=int(input("a를 입력하세요:"))
b=int("b를 입력하세요:"))

print("a=%d 입니다,b=%d 입니다"%(a,b))
'''
#내가 희망하는 키 출력
name="우희서"
age=14
height=160
hope=int(input("키를 입력하세요:"))
print("제 이름은 %s입니다.\n 나이는 %d,희망키는 %d." %(name,age,hope))
print("제 이름은{}입니다.\n나이는 {},희망키는 {}.".format(name,age,height))

tmp=hope-height

print("그럼 앞으로 30만큼 커야겠네요ㅋㄷ"%(hope-height))
print("그럼 앞으로 "+str(tmp)+"만큼 커야겠네요ㅋㄷ")
