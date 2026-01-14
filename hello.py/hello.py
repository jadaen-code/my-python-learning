a=input("請輸入你要的符號+,-,*,/,**(第一個數字的平方加上第二個數字的平方)")
b=float(input("請輸入第一個數字"))
c=float(input("請輸入第二個數字"))
if a=='+':
    print(b+c)
elif a=='-':
    print(b-c)
elif a=='*':
    print(b*c)
elif a == '/':
 if c == 0:
     print("⚠ 數學錯誤：除數不能為零！請重新輸入。")
 else:
     print(b / c)

elif a=='**':
    print((b**2)+(c**2))
else:
    print("請檢察輸入文本")