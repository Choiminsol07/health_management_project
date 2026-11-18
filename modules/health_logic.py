''' 
202611845 최민솔

모듈2 주 기능
- 신규 등록 및 중복 체크: UI 및 엑셀 파일로부터 데이터를 받아 중복 검사 후 리스트 및 파일에 추가
- 조회 및 검색: 전체 목록 조회 및 이름·식별번호 기반 상세 검색 기능 제공
- 수정 및 BMI 자동 재계산: 특정 레코드의 키·몸무게 수정 시 공식(체중/(키/100)**2)에 따른 BMI 및 비만도 재산출 연동
- 삭제: 선택된 레코드의 안전한 제거 및 파일 동기
- 통계 산출: 전체 인원수, 평균 키, 평균 몸무게, 평균 BMI 등의 유용한 통계 데이터 연산
- 핵심 비즈니스 로직 및 CRUD, 통계 연산, 건강정보관리자 클래스 내 메소드 추가, 콘솔 APP으로 테스트


-CRUD: 컴퓨터 소프트웨어와 데이터베이스에서 데이터를 처리하는 가장 기본적인 4가지 기능의 앞자리를 딴 용어
• Create (생성): 새로운 데이터를 만드는 기능 (SQL: INSERT)
• Read (읽기/조회): 저장된 데이터를 확인하는 기능 (SQL: SELECT)
• Update (수정/갱신): 기존 데이터를 변경하는 기능 (SQL: UPDATE)
• Delete (삭제): 데이터를 지우는 기능 (SQL: DELETE)

클래스
- ExcelRepository: UI 및 엑셀 파일로부터 데이터를 받아 중복 검사 후 신규 등록 및 중복 체크
- HealthLogic:  HealthManager을 상속받아 건강 기록의 등록, 검색, 수정, 삭제, 통계
'''
from modules.health_db import HealthManager, HealthRecord
import csv # 파일을 읽기 위해 불러옴

class ExcelRepository:
    # 엑셀 파일을 읽어 건강 기록 목록과 오류 정보를 반환
    def load_records(self, file_path):
        self.file_path = file_path
        with open('health_data','r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
    # 기록을 검증하고 중복이 아니면 목록에 추가
    def add_record(self, record, records):
        self.recode = recode
        self.recodes = recodes
        
        
    # 건강 기록 목록을 엑셀 파일에 저장
    def save_records(self, file_path, records):
        



class HealthLogic:
    