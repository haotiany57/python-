xia=0
shan=1000
shuru=input("输入")
xun=int(shuru)
jishu=0
if xun>shan:
    print ("找不到")
    exit(0)
while xia<=shan:
    zhon=(xia+shan)/2 
    if zhon==xun:
        print ("这个数是"+str(zhon))
        print ("找了"+str(jishu)+"次")
        break
    elif zhon>xun:
        shan=zhon
    else:
        xia=zhon
    jishu=jishu+1
