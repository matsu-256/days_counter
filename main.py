import tkinter as tk
def uru(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#　メインの処理
def foo():
    ans = 0
    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    # 入力を受け取る
    while True:
        try:
            year1 = int(year1_E.get())
            month1 = int(month1_E.get())
            day1 = int(day1_E.get())

            year2 = int(year2_E.get())
            month2 = int(month2_E.get())
            day2 = int(day2_E.get())
        except ValueError:
            result.set("自然数を入力してください")
        if year1 == 0 or month1 == 0 or day1 == 0 or year2 == 0 or month2 == 0 or day2 == 0:
            result.set("自然数を入力してください")
        
        # 日付のエラー判定 　具体的には、日付が負の値、日にちの値がその月の日数を超過している、FROM > TOの時
        if ( year1 < 0 or month1 < 0 or day1 < 0 or year2 < 0 or month2 < 0 or day2 < 0 ) or \
        ( (uru(year2) and month2 == 2) and (months[month1 - 1] < day1 or months[month2 - 1] + 1 < day2) ) or \
        ( ( uru(year1) and month1 == 2 ) and (months[month1 - 1] + 1 < day1 or months[month2 - 1] < day2) ) or \
        ( ( (not uru(year1)) and (not uru(year2)) ) and (months[month1 - 1] < day1 or months[month2 - 1] < day2)  ) or \
        ( ((year2 - year1) < 0) or ( year1 == year2 and month1 > month2 ) or ( year1 == year2 and month1 == month2 and day1 > day2)):
            result.set("日付がおかしいです！")
            continue
        else:
            break
    # 年
    if year2 - year1 >= 2:
        years = [i for i in range(year1 + 1 , year2)]
        for i in years:
            if uru(i):
                ans += 366
            else:
                ans += 365

    # 月
    if year1 != year2:
        if month1 != 12:
            for i in range(month1 + 1,13):
                if i == 2 and uru(year1):
                    ans += months[i - 1] + 1
                else:
                    ans += months[i - 1]
        if month2 != 1:
            for i in range(1,month2):
                if i == 2 and uru(year1):
                    ans += months[i - 1] + 1
                else:
                    ans += months[i - 1]
    elif month2 - month1 >= 2:
        for i in range(month1 + 1, month2):
            if i == 2 and uru(year1):
                ans += months[i - 1] + 1
            else:
                ans += months[i - 1]

    # 日
    if month2 - month1 >= 1 or year1 != year2:
        if uru(year1) and month1 == 2:
            ans += (months[month1 - 1] + 1 - day1) + day2
        else:
            ans += (months[month1 - 1] - day1) + day2
    else:
        ans += day2 - day1

    # 出力
    result.set(str(ans))

# GUI
root = tk.Tk()
root.title("days counter")
result = tk.StringVar(value="")

Static1 = tk.Label(root, text="経過日数を計算します", anchor=tk.CENTER).grid(row=0, column=0, columnspan=6, sticky="ew")

Label1 = tk.Label(root, text="いつから？").grid(row=1, column=0, columnspan=6, sticky="w")

year1_E = tk.Entry(root, width=7)
year1_E.grid(row=2, column=0, sticky="e")
year1_L = tk.Label(root, text="年")
year1_L.grid(row=2, column=1, sticky="w")
month1_E = tk.Entry(root, width=3)
month1_E.grid(row=2, column=2, sticky="w")
month1_L = tk.Label(root, text="月")
month1_L.grid(row=2, column=3, sticky="w")
day1_E = tk.Entry(root, width=3)
day1_E.grid(row=2, column=4, sticky="w")
day1_L = tk.Label(root, text="日")
day1_L.grid(row=2, column=5, sticky="w")

Label2 = tk.Label(root, text="いつまで？").grid(row=3, column=0, columnspan=6, sticky="w")

year2_E = tk.Entry(root, width=7)
year2_E.grid(row=4, column=0, sticky="e")
year2_L = tk.Label(root, text="年")
year2_L.grid(row=4, column=1, sticky="w")
month2_E = tk.Entry(root, width=3)
month2_E.grid(row=4, column=2, sticky="w")
month2_L = tk.Label(root, text="月")
month2_L.grid(row=4, column=3, sticky="w")
day2_E = tk.Entry(root, width=3)
day2_E.grid(row=4, column=4, sticky="w")
day2_L = tk.Label(root, text="日")
day2_L.grid(row=4, column=5, sticky="w")

button = tk.Button(root, text="計算", width=10, command=foo).grid(row=5, column=2, columnspan=6, sticky="w")

Label3 = tk.Label(root,text="計算結果 :")
Label3.grid(row=6, column=0, sticky="w")
Label4 = tk.Label(root,textvariable=result)
Label4.grid(row=6, column=1, sticky="ew")

root.mainloop()
