import requests
import pandas as pd
from datetime import datetime

# 设置Web UI的URL和登录信息
qb_url = 'http://your_qbittorrent_web_ui_url'  # 替换为你的qBittorrent Web UI URL
username = 'your_username'                      # 替换为你的用户名
password = 'your_password'                      # 替换为你的密码

# 登录获取cookie
login_payload = {'username': username, 'password': password}
session = requests.Session()
response = session.post(f'{qb_url}/api/v2/auth/login', data=login_payload)

# 检查是否登录成功
if response.status_code == 200 and response.text == "Ok.":
    print("登录成功")
else:
    print("登录失败")
    exit()

# 获取种子信息
response = session.get(f'{qb_url}/api/v2/torrents/info')
if response.status_code == 200:
    torrents = response.json()
else:
    print("获取种子信息失败")
    exit()

# 函数：将字节转换为合适的单位
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"

# 提取所需的种子信息
data = []
for torrent in torrents:
    torrent_info = {
        '名称': torrent['name'],
        '大小': sizeof_fmt(torrent['total_size']),
        '已上传': sizeof_fmt(torrent['uploaded']),
        '分享率': torrent['ratio'],
        '添加时间': pd.to_datetime(torrent['added_on'], unit='s'),  # 转换时间戳为日期时间
        '完成时间': pd.to_datetime(torrent['completion_on'], unit='s') if torrent['completion_on'] != -1 else None,  # 转换时间戳为日期时间
        '更新时间': datetime.now()  # 添加最后更新时间
    }
    data.append(torrent_info)

# 创建DataFrame
df_new = pd.DataFrame(data)

# 读取先前的Excel数据
try:
    df_old = pd.read_excel('path_to_your_previous_excel_file')  # 替换为你先前的Excel文件路径
except FileNotFoundError:
    df_old = pd.DataFrame()

# 合并数据并去重
df_merged = pd.concat([df_old, df_new]).drop_duplicates(subset=['名称', '添加时间'], keep='last')

# 导出到Excel
excel_file = 'path_to_your_output_excel_file'  # 替换为输出的Excel文件路径
df_merged.to_excel(excel_file, index=False)

print(f"种子信息已导出到 {excel_file}")
