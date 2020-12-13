# pip install [라이브러리이름]
# pip install bs4 터미널에 입력 후 사용!

# 웹크롤러 어플리케이션 코딩
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 사용자에게 주소 입력 받기
inputValue = input('주소? ')

# 사용자가 http://로 입력 안 했을 때의 처리
first7chars = inputValue[0:7]
if (first7chars != 'http://' and first7chars != 'https://'):
    inputValue = 'http://'+inputValue

# 완성된 inputValue를 크롤링해서 soup변수에 넣기
url = urlopen(inputValue)
soup = BeautifulSoup(url, 'html.parser')

# 메모장 내용 초기화
f = open('output.txt', 'w', encoding='utf-8') # a는 이어쓰기, w는 덮어쓰기
f.write('')
f.close()

# 크롤링결과를 가공해서 메모장에 저장
for anchor in soup.find_all('a'): # a 태그를 검색해서 있을 때마다, 변수 anchor에 넣음
    # 1. 변수안에 넣어버리자.
    link = anchor.get('href', '/')

    # 2. 앞의 문자를 잘라서 가져와보자.
    first7chars = link[0:7]

    # 3. 조건문으로 거를 거 거르자.
    if (first7chars != 'http://' and first7chars != 'https://'):
        continue
    
    print(link)
    
    # 메모장에 저장
    fileName = 'output.txt'
    f = open(fileName, 'a', encoding='utf-8') # a는 이어쓰기, w는 덮어쓰기
    link = link + '\n'
    f.write(link)
    f.close()

