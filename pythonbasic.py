## 파이썬 시작하기
#1. 화면에 Hello World 문자열을 출력하세요.
print("Hello World")
#2. 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")
#3. 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')
#4. 화면에 "C:\Windows"를 출력하세요.
print("C:\Windows")
#5. print 탭과 줄바꿈
print("안녕하세요.\n만나서\t\t반갑습니다.")
#6. print 여러 데이터 출력 *** , 로 구분하면 공백이 출력된다.
print ("오늘은", "일요일")
#7,8. naver;kakao;sk;samsung 또는 naver/kakao/sk/samsung 을 출력한다. *** sep="구분자"를 넣는다.
print("Naver", "Kakao", "SK", "Samsung", sep=";")
print("Naver", "Kakao", "SK", "Samsung", sep="/")
#9. *** 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용. *** end="" 는 줄바꿈없이 출력.
print("first");print("second")
print("first", end="");print("second")
#10. 5/3의 결과를 화면에 출력하세요.
print(5/3)
## 파이썬 변수
#11. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
#12. 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 29000000000000
현재가 = 50000
PER = 15.79
print(시가총액)
print(현재가)
print(PER)
#13. s = "hello", t = "python" 을 hello! python 로 출력하기.
s = "hello"
t = "python"
print(s+"!", t)
print(s+"! "+t)
#14. 2 + 2 * 3
print(2 + 2 * 3)
#15. type() 함수는 데이터 타입을 판별합니다.
a = 128
print(type(a))
b = "128"
print(type(b))
#16. 문자열 '720'를 정수형으로 변환해보세요. *** int(변수명): int 로 변환하기
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))
#17. 정수 100을 문자열 '100'으로 변환해보세요. *** str(변수명): str 로 변환하기
num = 100
result = str(num)
print(result, type(result))
#18. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요. *** float(변수명): float 로 변환하기
data = "15.79"
data_f = float(data)
print(data_f, type(data_f))
#19. year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
year_i = int(year)
print(year_i, year_i+1, year_i+2)
#20. 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
airconditioner = 48584
installment = 36
total_price = airconditioner * installment
print(total_price)
## 문자열
#21. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요. 실행 예: p t
letters = 'python'
print(letters[0], letters[2])
#22. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[-4:])
#23. 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2])
#24. 문자열을 거꾸로 뒤집어 출력하세요. *** 거꾸로 뒤집어서 출력하기. [::-1]
string = "PYTHON"
print(string[::-1])
#25. 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요. 실행 예: 010 1111 2222 *** 문자열의 일부를 바꾸기. .replace("바꿀문자", "새문자")
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
#26. 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace("-", ""))
#27. url 에 저장된 웹 페이지 주소에서 도메인(kr)을 출력하세요. *** .split("구분할 문자"): 구분할 문자를 기준으로 문자열을 나누어 list 를 만듬.
url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split)
print(url_split[-1])
#28. 아래 코드의 실행 결과를 예상해보세요. *** 문자열은 수정할 수 없음.
# lang = 'python'
# lang[0] = 'P'
# print(lang)
#29. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요. string = 'abcdfe2a354a32a'
string = 'abcdfe2a354a32a'
string_cap = string.replace("a", "A")
print(string_cap)
#30. 아래 코드의 실행 결과를 예상해보세요. *** 문자열은 수정할 수 없음. 다른 변수를 지정해야 수정됨.
string = 'abcd'
string.replace('b', 'B')
print(string)