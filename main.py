from modules.health_db import HealthManager, HealthRecord

def main():
    manager = HealthManager()

    while True:
        print("\n===== 건강정보 관리 프로그램 =====")
        print("1. 건강정보 추가")
        print("2. 건강정보 전체 조회")
        print("3. JSON 저장")
        print("4. JSON 불러오기")
        print("5. CSV 저장")
        print("6. CSV 불러오기")
        print("7. TXT 저장")
        print("8. TXT 불러오기")
        print("9. Pickle 저장")
        print("10. Pickle 불러오기")
        print("0. 프로그램 종료")

        choice = input("메뉴를 선택하세요: ")

        # 건강정보 추가
        if choice == "1":
            name = input("이름을 입력하세요: ")
            birth_year = int(input("생년을 입력하세요: "))
            gender = input("성별을 입력하세요: ")
            height = float(input("키(cm)를 입력하세요: "))
            weight = float(input("몸무게(kg)를 입력하세요: "))

            # BMI 계산
            bmi = weight / ((height / 100) ** 2)
            bmi = round(bmi, 2)

            # 비만도 상태 계산
            if bmi < 18.5:
                status = "저체중"
            elif bmi < 23:
                status = "정상"
            elif bmi < 25:
                status = "과체중"
            else:
                status = "비만"

            # 식별번호 자동 생성
            patient_id = manager.generate_id()

            # 건강정보 객체 생성
            record = HealthRecord(
                patient_id,
                name,
                birth_year,
                gender,
                height,
                weight,
                bmi,
                status
            )

            manager.add_record(record)

            print("\n건강정보가 추가되었습니다.")
            print("식별번호:", patient_id)

        # 건강정보 전체 조회
        elif choice == "2":
            if len(manager.records) == 0:
                print("등록된 건강정보가 없습니다.")

            else:
                print("\n===== 건강정보 목록 =====")

                for record in manager.records:
                    print("------------------------")
                    print("식별번호:", record.id)
                    print("이름:", record.name)
                    print("생년:", record.birth_year)
                    print("성별:", record.gender)
                    print("키:", record.height)
                    print("몸무게:", record.weight)
                    print("BMI:", record.bmi)
                    print("비만도 상태:", record.status)

        # JSON 저장
        elif choice == "3":
            manager.save_json()

        # JSON 불러오기
        elif choice == "4":
            manager.load_json()

        # CSV 저장
        elif choice == "5":
            manager.save_csv()

        # CSV 불러오기
        elif choice == "6":
            manager.load_csv()

        # TXT 저장
        elif choice == "7":
            manager.save_txt()

        # TXT 불러오기
        elif choice == "8":
            manager.load_txt()

        # Pickle 저장
        elif choice == "9":
            manager.save_pickle()

        # Pickle 불러오기
        elif choice == "10":
            manager.load_pickle()

        # 프로그램 종료
        elif choice == "0":
            print("건강정보 관리 프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴입니다. 다시 선택해주세요.")


# 프로그램 실행
if __name__ == "__main__":
    main()