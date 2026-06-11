import requests

# 目标网址
url = "https://ip.164746.xyz/ipTop.html"
# 保存的文件名
file_name = "ip_list.txt"

def main():
    try:
        # 获取网页内容
        response = requests.get(url, timeout=15)
        # 写入文件
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("抓取成功")
    except Exception as e:
        print(f"抓取失败: {e}")

if __name__ == "__main__":
    main()
