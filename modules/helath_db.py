''' 
202611845 최민솔

모듈1 주 기능
- 데이터 구조화(레코드) 및 파일 I/O (JSON, CSV, TXT, Pickle), 클래스(건강정보, 건강정보관리자), 파일입출력
- 레코드모델링: 식별번호, 이름, 생년, 성별, 키, 몸무게, BMI, 비만도상태를담는객체구조및
- 딕셔너리변환(to_dict) 지원
- 식별번호자동생성: 신규레코드추가시고유한환자식별번호발급로직구현
- 다중파일I/O: JSON, CSV, TXT, Pickle등영구파일포맷별저장(save) 및로드(load) 기능제공
- 예외처리: 파일부재나손상시예외처리(try-except) 구현
클래스
- HealthRecord: 건강 기록(식별번호, 이름, 생년, 성별, 키, 몸무게, BMI, 비만도 상태)을 저장
- HealthManager: 건강 기록 목록 관리 및 식별번호 생성 및 JSON, CSV, TXT, Pickle 파일의 저장 및 불러오기
'''


import json  # json : 데이터를 키와 값의 쌍으로 구성하여 저장하는 파일 형식
import csv  # csv : 데이터를 ,로 구분하여 저장하는 파일 형식
import pickle  # pickle : 파이썬 객체를 직렬화하여 저장하는 파일 형식

# 건강정보 클래스 구현
class HealthRecord:
    def __init__(self, id,name,birth_year,gender,height,weight,bmi,status):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status   
    
    # 건강정보 딕셔너리 변환 : JSON에 저장하기 위해
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "status": self.status
        }


# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: 인터넷 검색 (uuid) 이 알맞은 방식이 아닌 것 같아 도움을 요청하기 위해, 신규 건강정보를 추가할 때마다 고유한 식별번호를 순차적으로 생성하는 방법을 찾지 못하여 사용함.
# 사용한 프롬프트: 파이썬에서 uuid 말고 P2026-0001 형식으로 순차적으로 식별번호를 생성하는 방법 추천해줘.
# 작성일: 2026-11-14

class HealthManager:

    # 사용자 식별번호 생성
    def __init__(self):
        self.records = []
        self.next_number = 1

    def generate_id(self):
        patient_id = f"P2026-{self.next_number:04d}"
        self.next_number += 1

        return patient_id

    # 여러 사람의 건강 정보 추가하기
    def add_record(self, record):
        self.records.append(record)

# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: json 사용 방법을 정확히 이해하지 못하여 정확한 이해 및 json을 저장하기 위해
# 사용한 프롬프트: 파이썬 클래스에 저장된 객체 정보를 JSON 파일로 저장하고 다시 불러오려면 어떻게 해야해?
# 작성일: 2026-11-14

    def save_json(self):
        data = []

        for record in self.records:
            data.append(record.to_dict())

        with open("health_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("저장 완료")

    
    def load_json(self):
        try:
            with open("health_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.records = []

            for item in data:
                record = HealthRecord(
                    item["id"],
                    item["name"],
                    item["birth_year"],
                    item["gender"],
                    item["height"],
                    item["weight"],
                    item["bmi"],
                    item["status"]
                )

                self.records.append(record)

            print("불러오기 완료")

        except FileNotFoundError:
            print("저장된 파일이 없습니다.")


# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: csv 사용 방법을 이해하고 저장하기 위해, CSV 파일에 건강정보를 저장할 때 열 제목을 설정하고 각 데이터를 다시 객체로 변환하는 방법을 이해하지 못하여 사용
# 사용한 프롬프트: 파이썬에서 클래스 객체에 저장된 데이터를 CSV 파일로 저장하고 다시 불러오는 방법을 알려줘.
# 작성일: 2026-11-16


    #csv 파일 저장하기
    def save_csv(self):
        with open("health_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["id", "name", "birth_year", "gender",
                             "height", "weight", "bmi", "status"])

            for record in self.records:
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

        print("CSV 저장 완료")


    # csv 파일 불러오기
    def load_csv(self):
        try:
            with open("health_data.csv", "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)

                next(reader)  # 첫 번째 줄(제목) 건너뛰기

                self.records = []

                for row in reader:
                    record = HealthRecord(
                        row[0],
                        row[1],
                        int(row[2]),
                        row[3],
                        float(row[4]),
                        float(row[5]),
                        float(row[6]),
                        row[7]
                    )

                    self.records.append(record)

            print("CSV 불러오기 완료")

        except FileNotFoundError:
            print("저장된 CSV 파일이 없습니다.")


    # TXT 파일 저장하기
    # 구글 txt 파일 저장 방법 참고
    def save_txt(self):
        with open("health_data.txt", "w", encoding="utf-8") as f:

            for record in self.records:
                f.write(f"{record.id},{record.name},{record.birth_year},{record.gender},{record.height},{record.weight},{record.bmi},{record.status}\n")

        print("TXT 저장 완료")
    
    # TXT 파일 불러오기
    # 구글 txt 파일 불러오기 방법 참고
    def load_txt(self):
        try:
            with open("health_data.txt", "r", encoding="utf-8") as f:
                self.records = []

                for line in f:
                    data = line.strip().split(",")

                    record = HealthRecord(
                        data[0],
                        data[1],
                        int(data[2]),
                        data[3],
                        float(data[4]),
                        float(data[5]),
                        float(data[6]),
                        data[7]
                    )

                    self.records.append(record)

            print("TXT 불러오기 완료")

        except FileNotFoundError:
            print("저장된 TXT 파일이 없습니다.")

# AI 사용 주석
# AI 종류: ChatGPT (GPT-6)
# AI 사용 목적: Pickle을 이용하여 객체가 저장된 리스트를 파일로 저장하고 원래 형태로 불러오는 방법을 알지 못하여 사용
# 사용한 AI 프롬프트: 파이썬에서 Pickle을 사용하여 클래스 객체가 들어 있는 리스트를 저장하고 불러오는 방법을 알려줘.
# 사용 날짜: 2026.11.16

    # Pickle 파일 저장하기
    def save_pickle(self):
        with open("health_data.pkl", "wb") as f:
            pickle.dump(self.records, f)

        print("Pickle 저장 완료")
    
    # Pickle 파일 불러오기
    def load_pickle(self):
        try:
            with open("health_data.pkl", "rb") as f:
                self.records = pickle.load(f)

            print("Pickle 불러오기 완료")

        except FileNotFoundError:
            print("저장된 Pickle 파일이 없습니다.")

        except (pickle.UnpicklingError, EOFError):
            print("Pickle 파일이 손상되었습니다.")
