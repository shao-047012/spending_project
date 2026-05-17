date = input("請輸入日期：")

with open("花費紀錄.txt", encoding="utf-8") as file:
    lines = file.readlines()

total = 0

for line in lines:
    if date in line:
        parts = line.split("$")
        amount_str = parts[1].split("元")[0]
        total += int(amount_str)

print(f"{date} 共花費：{total} 元")
