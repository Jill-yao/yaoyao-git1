from dotenv import  load_dotenv
load_dotenv()
import os
key = os.environ.get('envr')
if key:
    masked = key[:2]+ "***" +key[-3:]
    print(f"key 读取成功：{masked}")
    print(f"key 长度：{len(key)}")
else:
    print("未读取到key,请检查。env文件名和变量名")

print("hello world" )