file=open("test.txt","a",encoding="utf-8")
file.write("\n안녕하세요")
file.close()

with open("test.txt","a",encoding="utf-8")as file:
	file.write("안녕하세요")

with open("memo.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)

for line in lines:
	print(line.strip())

with open("memo.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")


memo=input("메모를 입력하세요: ")

with open("memo.txt","w",encoding="utf-8")as file:
	file.write(memo)

students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n") #숫자처럼 보여도 문자로 저장됨



def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)
			
students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

save_students(students,"students.txt")

def load_students(filename):
    students = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")

        student = {
            "name": data[0],
            "score": int(data[1])
        }

        students.append(student)

    return students

students=load_students("students.txt")

print(students)

def load_students(filename):
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")

            student = {
                "name": data[0],
                "score": int(data[1])
            }

            students.append(student)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

    except ValueError:
        print("점수 데이터가 숫자가 아닙니다.")

    return students

import os

print(os.getcwd())


if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")

stocks = [
    {"date": "2026-09-01", "name": "삼성전자", "close": 70000},
    {"date": "2026-09-02", "name": "삼성전자", "close": 72000},
    {"date": "2026-09-03", "name": "삼성전자", "close": 71000}
]

import csv

with open("stock.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "name", "close"])

    for stock in stocks:
        writer.writerow([
            stock["date"],
            stock["name"],
            stock["close"]
        ])

stocks = []

with open("stock.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        stock = {
            "date": row[0],
            "name": row[1],
            "close": int(row[2])
        }

        stocks.append(stock)


total = 0

for stock in stocks:
    total += stock["close"]

average = total / len(stocks)

print(f"평균 종가 : {average:,.0f}원")

players = [
    {"name": "철수", "시도횟수": 5},
    {"name": "영희", "시도횟수": 3}
]

lotto_history = [
    [1, 5, 10, 20, 30, 40],
    [2, 7, 15, 22, 35, 44]
]

import json

game_data = {
    "players": players,
    "lotto_history": lotto_history
}

with open("game_data.json", "w", encoding="utf-8") as file:
    json.dump(game_data, file, ensure_ascii=False, indent=4)


try:
    with open("game_data.json", "r", encoding="utf-8") as file:
        game_data = json.load(file)

    players = game_data["players"]
    lotto_history = game_data["lotto_history"]

except FileNotFoundError:
    players = []
    lotto_history = []