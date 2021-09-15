#建立簡單計算機

#需要取得輸入 ,用語法input("提示語..")
name=input("請輸入使用者名稱:")
print("你好,使用者"+name)
print("請問要執行什麼運算")
print("加/減/乘/除:1/2/3/4")
key="sel"

while key!='c':
    x1=float(input("請輸入第一個數字:"))
    x2=float(input("請輸入第二個數字:"))
    key=input("請輸入想要執行的運算:")

    if key=='1':
        print(x1,"+",x2,"=",x1+x2)
    elif key=='2':
        print(x1,"-",x2,"=",x1-x2)
    elif key=="3":
        print(x1,"*",x2,"=",x1*x2)
    elif key=='4':
        print(x1,"/",x2,"=",x1/x2)
    else:
        print("請重新輸入")
    key=input("是否繼續運算,是請按y,否請按c:")



x=5
    