# qBittorrent Torrent Info Exporter

This script logs into the qBittorrent Web UI, retrieves torrent information, and exports it to an Excel file. The script merges new torrent data with previously saved data and removes duplicates.

## Features

- Log in to qBittorrent Web UI.
- Retrieve torrent information.
- Convert byte sizes to human-readable formats.
- Merge new data with previously saved data.
- Export data to an Excel file.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library
- `openpyxl` library (for Excel support)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/qbittorrent-torrent-info-exporter.git
    ```
2. Install the required libraries:
    ```sh
    pip install requests pandas openpyxl
    ```

## Usage

1. Edit the script to include your qBittorrent Web UI URL, username, and password.
2. Run the script:
    ```sh
    python qbittorrent_exporter.py
    ```

## 中文说明

这个脚本登录到qBittorrent Web UI，获取种子信息，并将其导出到Excel文件中。脚本将新种子数据与之前保存的数据合并，并去除重复项。

## 功能

- 登录qBittorrent Web UI。
- 获取种子信息。
- 将字节大小转换为易读格式。
- 将新数据与之前保存的数据合并。
- 导出数据到Excel文件。

## 要求

- Python 3.x
- `requests`库
- `pandas`库
- `openpyxl`库（用于Excel支持）

## 安装

1. 克隆仓库：
    ```sh
    git clone https://github.com/your_username/qbittorrent-torrent-info-exporter.git
    ```
2. 安装所需库：
    ```sh
    pip install requests pandas openpyxl
    ```

## 使用方法

1. 编辑脚本，包含你的qBittorrent Web UI URL、用户名和密码。
2. 运行脚本：
    ```sh
    python qbittorrent_exporter.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

