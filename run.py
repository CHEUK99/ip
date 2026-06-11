import requests
import re

# 目标网址
url = "https://ip.164746.xyz/ipTop.html"
# 保存的文件名
file_name = "ip_list.txt"

def main():
    try:
        # 获取网页内容
        response = requests.get(url, timeout=15)
        
        # 使用正则表达式提取所有符合 IP 格式 (X.X.X.X) 的内容
        # 这是一个专门过滤文本的技术，不管网页里有多少乱七八糟的代码，它只抓 IP
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', response.text)
        
        # 去重（防止网页里同一个IP出现多次）并排序
        unique_ips = sorted(list(set(ips)))

        # 将整理好的 IP 写入文件，每个 IP 换一行
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(unique_ips))
            
        print("抓取并格式化成功")
    except Exception as e:
        print(f"抓取失败: {e}")

if __name__ == "__main__":
    main()
