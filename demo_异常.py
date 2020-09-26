import time
# print("呼呼呼")
# try:
#     f=open('text1.txt','r')
#     try:
#       while True:
#              con=f.readline()
#              print(con)
#              if len(len(con)==0):break
#     except:print('文件被意外终止')
#     finally:
#         f.close()
#         print('文件关闭')
# except:
#         print("文件不存在")
class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length=length
        self.min_len=min_len
    def __str__(self):
        return f'你输入的长度为{self.length},不能少于{self.min_len}'
def main():
    try:
        con=input('请输入密码')
        if len(con)<3:
            raise ShortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')
main()