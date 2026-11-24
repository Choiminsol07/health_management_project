''' 
202611845 최민솔

모듈 2 주 기능
- 화면 레이아웃 구성: 입력 폼(Entry), 버튼, 파일 형식 선택 위젯 등을 갖춘 윈도우 인터페이스 제공
- 표 시각화 (Treeview): 등록된 건강 정보를 엑셀 표 격자 형태로 출력하고 스크롤바 연동
- 이벤트 바인딩: 표의 행 클릭 시 입력창에 데이터가 자동 입력(<<TreeviewSelect>>)되도록 연동
- 로직 호출 및 피드백: 사용자 액션을 모듈 2(로직)로 전달하고, 성공/실패 여부를 messagebox로 안내

클래스
-
'''

from tkinter import*

window = Tk()
window.title("BMI 건강관리 프로그램")
window.geometry("1000x800")

button = Button(
    window,
    font=("맑은 고딕", 35, "bold"),
    text="bmi 건강관리 프로그램",
    bg="black",
    fg="white",
    width=1000,
    height=800,
)
button.pack(expand=True)

window.mainloop()