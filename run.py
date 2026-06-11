import requests
import re
import os

url = "https://ip.164746.xyz/ipTop.html"
file_name = "ip_list.txt"

# 增加 headers，模拟真实浏览器访问，防止被网站拦截
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def main():
    try:
        # 发送请求
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # 打印一下网页内容的前 200 个字符，方便你在 GitHub 日志里检查是否抓到了数据
        print(f"网页内容预览: {response.text[:200]}...")
        
        # 提取 IP
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', response.text)
        
        # 去重并排序
        unique_ips = sorted(list(set(ips)))
        print(f"共抓取到 {len(unique_ips)} 个 IP")

        if not unique_ips:
            print("警告：未抓取到任何 IP，请检查网页格式是否变更！")
            return

        # 写入文件
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(unique_ips))
            
    except Exception as e:
        print(f"执行出错: {e}")
        exit(1)

if __name__ == "__main__":
    main()
