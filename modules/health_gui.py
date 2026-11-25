
''' 202611845 최민솔

모듈3 주 기능
- 화면 레이아웃 구성: 입력 폼(Entry), 버튼, 파일 형식 선택 위젯 등을 갖춘 윈도우 인터페이스 제공
- 표 시각화 (Treeview): 등록된 건강 정보를 엑셀 표 격자 형태로 출력하고 스크롤바 연동
- 이벤트 바인딩: 표의 행 클릭 시 입력창에 데이터가 자동 입력되도록 연동
- 로직 호출 및 피드백: 사용자 액션을 모듈 2(로직)로 전달하고 성공/실패 여부를 안내

클래스
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("건강관리 프로그램")
root.geometry("1000x1200")
root.configure(bg="black")

BG = "black"
BLUE = "steelblue4"
GREEN = "darkgreen"
ORANGE = "chocolate4"
WHITE = "white"
GRAY = "gray"

header = tk.Frame(root, bg=BLUE, height=85)
header.pack(fill="x", padx=10, pady=10)

tk.Label(
    header,
    text="bmi 건강관리 프로그램",
    font=("맑은 고딕", 20, "bold"),
    bg=BLUE,
    fg=WHITE
).pack(anchor="w", padx=15, pady=(10, 0))

tk.Label(
    header,
    text="BMI 기반 개인 건강정보 관리 시스템",
    font=("맑은 고딕", 11),
    bg=BLUE,
    fg="lightgray"
).pack(anchor="w", padx=15)

stats_frame = tk.Frame(root, bg=BG)
stats_frame.pack(fill="x", padx=10)


def create_card(parent, title, value, unit, color, bg):

    card = tk.Frame(parent, bg=bg, height=100)
    card.pack(side="left", fill="x", expand=True, padx=5)
    card.pack_propagate(False)

    tk.Label(
        card,
        text=title,
        bg=bg,
        fg="gray",
        font=("맑은 고딕", 11)
    ).pack(anchor="w", padx=10, pady=8)

    tk.Label(
        card,
        text=value,
        bg=bg,
        fg=color,
        font=("맑은 고딕", 20, "bold")
    ).pack(anchor="w", padx=10)

    tk.Label(
        card,
        text=unit,
        bg=bg,
        fg="gray"
    ).pack(anchor="w", padx=10)


create_card(stats_frame, "등록 인원", "120", "명",
            "dodgerblue", "gray5")

create_card(stats_frame, "평균 BMI", "22.5", "",
            "mediumspringgreen", "gray5")

create_card(stats_frame, "평균 체중", "65.2", "kg",
            "darkorange", "gray5")

tk.Label(
    root,
    text="건강정보 관리",
    bg=BG,
    fg=WHITE,
    font=("맑은 고딕", 15, "bold")
).pack(anchor="w", padx=12, pady=12)

menu_frame = tk.Frame(root, bg=BG)
menu_frame.pack(fill="x", padx=10)


def create_button(parent, text, color):

    btn = tk.Button(
        parent,
        text=text,
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        font=("맑은 고딕", 13, "bold"),
        relief="flat",
        height=2,
        cursor="hand2"
    )

    btn.pack(side="left", fill="x", expand=True, padx=5)

    return btn


create_button(menu_frame, "♙\n정보 등록", "gray10")
create_button(menu_frame, "⌕\n정보 조회", "darkgreen")
create_button(menu_frame, "▥\n통계 확인", "chocolate4")

tk.Label(
    root,
    text="등록된 건강정보",
    bg=BG,
    fg=WHITE,
    font=("맑은 고딕", 15, "bold")
).pack(anchor="w", padx=12, pady=12)

tk.Label(
    root,
    text="화면 예시 데이터",
    bg=BG,
    fg=GRAY,
    font=("맑은 고딕", 10)
).pack(anchor="w", padx=12)

table_frame = tk.Frame(root, bg=BG)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = (
    "식별번호",
    "이름",
    "성별",
    "키",
    "몸무게",
    "BMI"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=7
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor="center")

sample_data = [
    ("P0001", "김민수", "남", 175, 70, 22.86),
    ("P0002", "이서연", "여", 162, 52, 19.81),
    ("P0003", "박지훈", "남", 180, 90, 27.78)
]

for data in sample_data:
    tree.insert("", "end", values=data)

scroll_y = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scroll_y.set)

scroll_x = ttk.Scrollbar(
    table_frame,
    orient="horizontal",
    command=tree.xview
)

tree.configure(xscrollcommand=scroll_x.set)

tree.grid(row=0, column=0, sticky="nsew")
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x.grid(row=1, column=0, sticky="ew")

table_frame.grid_rowconfigure(0, weight=1)
table_frame.grid_columnconfigure(0, weight=1)

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background="black",
    foreground="white",
    fieldbackground="black",
    rowheight=35,
    font=("맑은 고딕", 11)
)

style.configure(
    "Treeview.Heading",
    background="gray10",
    foreground="white",
    font=("맑은 고딕", 11, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "steelblue4")],
    foreground=[("selected", "white")]
)

tk.Label(
    root,
    text="검색 및 관리",
    bg=BG,
    fg=WHITE,
    font=("맑은 고딕", 15, "bold")
).pack(anchor="w", padx=12, pady=12)


search_frame = tk.Frame(root, bg=BG)
search_frame.pack(fill="x", padx=10)

search_entry = tk.Entry(
    search_frame,
    bg="gray15",
    fg=WHITE,
    insertbackground=WHITE,
    font=("맑은 고딕", 11),
    relief="flat"
)

search_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8
)

create_button(search_frame, "검색", BLUE)

manage_frame = tk.Frame(root, bg=BG)
manage_frame.pack(fill="x", padx=10, pady=10)

create_button(manage_frame, "등록", "darkgreen")
create_button(manage_frame, "수정", "steelblue4")
create_button(manage_frame, "삭제", "firebrick4")

tk.Label(
    root,
    text="건강정보 입력",
    bg=BG,
    fg=WHITE,
    font=("맑은 고딕", 15, "bold")
).pack(anchor="w", padx=12, pady=10)

form_frame = tk.Frame(root, bg="gray10")
form_frame.pack(fill="x", padx=10, pady=5)


def create_entry(parent, label):

    tk.Label(
        parent,
        text=label,
        bg="gray10",
        fg=WHITE,
        font=("맑은 고딕", 10)
    ).pack(side="left", padx=5)

    entry = tk.Entry(
        parent,
        bg="gray20",
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        width=12
    )

    entry.pack(side="left", padx=5, ipady=6)

    return entry


name_entry = create_entry(form_frame, "이름")
gender_entry = create_entry(form_frame, "성별")
height_entry = create_entry(form_frame, "키(cm)")
weight_entry = create_entry(form_frame, "몸무게(kg)")

file_frame = tk.Frame(root, bg=BG)
file_frame.pack(fill="x", padx=10, pady=10)

tk.Label(
    file_frame,
    text="파일 형식 선택",
    bg=BG,
    fg=WHITE,
    font=("맑은 고딕", 10)
).pack(side="left", padx=5)

file_type = ttk.Combobox(
    file_frame,
    values=["Excel (.xlsx)", "CSV (.csv)"],
    state="readonly",
    width=15
)

file_type.set("Excel (.xlsx)")
file_type.pack(side="left", padx=5)

create_button(file_frame, "파일 등록", "gray20")
create_button(file_frame, "파일 저장", "gray20")

root.mainloop()
