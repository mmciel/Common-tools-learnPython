
def solve(str):
    return  str[6]+str[7]+str[4]+str[5]+str[2]+str[3]+str[0]+str[1]
    pass


print("十六进制转十进制：\n"+
      "实验室门禁bug：无法添加新卡\n"+
      "解决方案：利用手机NFC读卡，读到的16进制数据进行字节逆置(门禁的加密方案)，然后转换成十进制\n")
while True:
    code = input("请输入16进制IC卡信息：")
    scode = solve(code)
    print("加密数据为："+scode)
    data = int(scode,16)
    print("最终十进制序号："+str(data))
