
'''
202611845 최민솔

모듈2 주 기능
- 신규 등록 및 중복 체크: UI 및 엑셀 파일로부터 데이터를 받아 중복 검사 후 리스트 및 파일에 추가
- 조회 및 검색: 전체 목록 조회 및 이름·식별번호 기반 상세 검색 기능 제공
- 수정 및 BMI 자동 재계산: 특정 레코드의 키·몸무게 수정 시 공식(체중/(키/100)**2)에 따른 BMI 및 비만도 재산출 연동
- 삭제: 선택된 레코드의 안전한 제거 및 파일 동기
- 통계 산출: 전체 인원수, 평균 키, 평균 몸무게, 평균 BMI 등의 유용한 통계 데이터 연산
- 핵심 비즈니스 로직 및 CRUD, 통계 연산, 건강정보관리자 클래스 내 메소드 추가, 콘솔 APP으로 테스트


CRUD
- Create (생성): 새로운 데이터를 만드는 기능
- Read (읽기/조회): 저장된 데이터를 확인하는 기능
- Update (수정/갱신): 기존 데이터를 변경하는 기능
- Delete (삭제): 데이터를 지우는 기능


클래스
- ExcelRepository: CSV 파일 읽기, 저장, 중복 검사
- HealthLogic: HealthManager를 상속받아 건강 기록의 등록, 검색, 수정, 삭제, 통계
'''

from modules.health_db import HealthManager, HealthRecord
import csv

# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: CSV 파일을 읽어 건강정보 데이터를 불러오는 방법을 정확히 이해하지 못하여 사용함. 특히 DictReader를 이용하여 CSV 파일의 데이터를 딕셔너리 형태로 저장하는 방법을 이해하기 위해 사용함.
# 사용한 프롬프트: 파이썬에서 CSV 파일을 읽고 각 행의 데이터를 딕셔너리 형태로 리스트에 저장하는 방법을 알려줘.
# 작성일: 2026-11-23

class ExcelRepository:

    # CSV 파일 읽기
    def load_records(self, file_path):

        records = []

        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    records.append(row)

        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")

        except Exception as e:
            print("파일 읽기 오류:", e)

        return records


    # 중복 검사 후 기록 추가
    def add_record(self, record, records):

        for existing in records:

            if existing.id == record.id:
                print("중복된 식별번호입니다.")
                return False

        records.append(record)

        return True


    # 건강 기록 목록을 CSV 파일에 저장
    def save_records(self, file_path, records):

        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:

                writer = csv.writer(f)

                writer.writerow([
                    'id', 'name', 'birth_year', 'gender',
                    'height', 'weight', 'bmi', 'status'
                ])

                for record in records:

                    writer.writerow([
                        record.id,
                        record.name,
                        record.birth_year,
                        record.gender,
                        record.height,
                        record.weight,
                        record.bmi,
                        record.status
                    ])

        except Exception as e:
            print("파일 저장 오류:", e)

# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: 키와 몸무게를 이용하여 BMI를 계산하고 계산된 BMI 값에 따라 비만도를 구분하는 방법을 정확히 이해하지 못하여 사용함.
# 사용한 프롬프트: 파이썬에서 키와 몸무게를 이용해 BMI를 계산하고 BMI 수치에 따라 저체중, 정상, 과체중, 비만으로 구분하는 함수를 만들어줘.
# 작성일: 2026-11-23

class HealthLogic(HealthManager):

    # BMI 계산
    def calculate_bmi(self, height, weight):

        bmi = weight / (height / 100) ** 2

        return round(bmi, 2)


    # 비만도 판정
    def calculate_status(self, bmi):

        if bmi < 18.5:
            return "저체중"

        elif bmi < 23:
            return "정상"

        elif bmi < 25:
            return "과체중"

        else:
            return "비만"


    # 신규 등록
    def create_record(self, name, birth_year, gender, height, weight):

        # 중복 이름 검사
        for record in self.records:

            if record.name == name and record.birth_year == birth_year:
                print("이미 등록된 사람입니다.")
                return False


        # 식별번호 생성
        patient_id = self.generate_id()


        # BMI 계산
        bmi = self.calculate_bmi(height, weight)


        # 비만도 계산
        status = self.calculate_status(bmi)


        # 건강 기록 객체 생성
        new_record = HealthRecord(
            patient_id,
            name,
            birth_year,
            gender,
            height,
            weight,
            bmi,
            status
        )


        # 기록 추가
        self.add_record(new_record)

        print("등록 완료!")

        return new_record


    # 전체 목록 조회
    def get_all_records(self):

        return self.records


    # 이름 또는 식별번호 검색
    def search_record(self, keyword):

        result = []

        for record in self.records:

            if keyword in record.name or keyword in record.id:
                result.append(record)

        return result


    # 건강정보 수정
    def update_record(self, patient_id, height, weight):

        for record in self.records:

            if record.id == patient_id:

                # 키와 몸무게 수정
                record.height = height
                record.weight = weight


                # BMI 다시 계산
                record.bmi = self.calculate_bmi(height, weight)


                # 비만도 다시 계산
                record.status = self.calculate_status(record.bmi)

                print("수정 완료!")

                return True


        print("해당 기록을 찾을 수 없습니다.")

        return False


    # 건강정보 삭제
    def delete_record(self, patient_id):

        for record in self.records:

            if record.id == patient_id:

                self.records.remove(record)

                print("삭제 완료!")

                return True


        print("해당 기록을 찾을 수 없습니다.")

        return False

# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: 여러 건강정보 객체가 들어 있는 리스트에서 전체 인원수와 평균 키, 평균 몸무게, 평균 BMI를 계산하는 방법을 이해하기 위해 사용함. 특히 sum()과 리스트 내포를 활용하여 객체의 특정 속성들의 평균을 구하는 방법을 이해하기 위해 사용함.
# 사용한 프롬프트: 파이썬 클래스 객체가 저장된 리스트에서 각 객체의 키, 몸무게, BMI를 가져와 평균을 계산하고 딕셔너리로 결과를 반환하는 방법을 알려줘.
# 작성일: 2026-11-23

    # 통계 계산
    def get_statistics(self):

        if len(self.records) == 0:
            return None


        # 전체 인원수
        total = len(self.records)


        # 평균 키
        avg_height = sum(
            record.height for record in self.records
        ) / total


        # 평균 몸무게
        avg_weight = sum(
            record.weight for record in self.records
        ) / total


        # 평균 BMI
        avg_bmi = sum(
            record.bmi for record in self.records
        ) / total


        # 통계 결과 저장
        statistics = {
            "인원수": total,
            "평균 키": round(avg_height, 2),
            "평균 몸무게": round(avg_weight, 2),
            "평균 BMI": round(avg_bmi, 2)
        }

        return statistics


# 테스트
if __name__ == "__main__":

    health = HealthLogic()


    # 신규 등록
    health.create_record("홍길동", 1995, "남", 175.0, 72.5)
    health.create_record("최민솔", 2007, "여", 182.0, 40.0)


    # 전체 목록 조회
    print("\n===== 전체 목록 =====")

    for record in health.get_all_records():

        print(record.to_dict())


    # 검색
    print("\n===== 검색 결과 =====")

    result = health.search_record("홍길동")

    for record in result:

        print(record.to_dict())


    # 수정
    print("\n===== 수정 =====")

    health.update_record("P2026-0001", 180.0, 80.0)


    # 통계
    print("\n===== 통계 =====")

    print(health.get_statistics())


    # 삭제
    print("\n===== 삭제 =====")

    health.delete_record("P2026-0002")


    # 삭제 후 목록 조회
    print("\n===== 삭제 후 목록 =====")

    for record in health.get_all_records():

        print(record.to_dict())
