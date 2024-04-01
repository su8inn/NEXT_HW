from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook

#원하는 url입력
url = "http://ticket.yes24.com/New/Genre/GenreMain.aspx?genre=15456&Gcode=009_202_001"

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    #응답 상태 코드 확인
    if response.status_code==200:
        html_text = response.text
        
        soup=bs(response.text, 'html.parser')
        #yes24 콘서트 what's hot 리스트
        whatshot_concert=soup.find_all(class_='list-b-tit1')
        whatshot_concert=list(map(lambda x: x.text.strip(),whatshot_concert))
        print(whatshot_concert)
        
        concert_hall=soup.find_all(class_='list-b-tit2')
        concert_hall=list(map(lambda x: x.text.strip(),concert_hall))
        print(concert_hall)
        
        #openpyxl Workbook 객체 생성
        wb=Workbook()
        ws=wb.active
        
        ws.append (["번호","공연 제목","공연장 정보"])
        
        for i, (whatshot_concert,concert_hall) in enumerate(zip(whatshot_concert, concert_hall),start=1):
            ws.append([i,whatshot_concert,concert_hall]) 
        
        #openpyxl 액샐파일 저장
        filename= f'yes24_conertInfo.xlsx'
        wb.save(filename)
        print(f'엑셀 파일 저장완료 :{filename}')

    else:
        print (f"Error:HTP 요청 실패. 상태 코드: {response.status_code}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: 요청 중 오류 발생. 오류 메시지:{e}")