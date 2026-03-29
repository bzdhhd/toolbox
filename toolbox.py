import os
import shutil
import time
from datetime import datetime

# ======================
# 1. 文件批量重命名
# ======================
def batch_rename(folder_path, prefix="file_"):
    try:
        # 获取文件夹中的所有文件
        files = os.listdir(folder_path)
        count = 1
        for file in files:
            # 获取文件路径
            old_path = os.path.join(folder_path, file)
            if os.path.isfile(old_path):
                # 获取文件扩展名
                ext = os.path.splitext(file)[1]
                # 新文件名
                new_name = f"{prefix}{count}{ext}"
                # 新文件路径
                new_path = os.path.join(folder_path, new_name)
                # 重命名文件
                os.rename(old_path, new_path)
                count += 1
        print("✅ 批量重命名完成！")
    except Exception as e:
        print(f"❌ 出错：{e}")

# ======================
# 2. 自动整理文件夹
# ======================
def auto_sort(folder_path):
    ext_map = {
        '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        '文档': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pdf', '.txt'],
        '视频': ['.mp4', '.mov', '.avi', '.mkv'],
        '音乐': ['.mp3', '.wav', '.flac'],
        '压缩包': ['.zip', '.rar', '.7z']
    }
    # 创建文件夹
    for folder in ext_map.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
    # 移动文件
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, exts in ext_map.items():
                if ext in exts:
                    target = os.path.join(folder_path, folder, file)
                    shutil.move(file_path, target)
                    break
    print("✅ 文件夹整理完成！")

# ======================
# 3. 定时提醒
# ======================
def reminder(msg, delay_seconds):
    print(f"⏰ 提醒将在 {delay_seconds} 秒后触发...")
    time.sleep(delay_seconds)
    current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🔔【{current}】{msg}")

# ======================
# 4. 主菜单
# ======================
def main():
    print("===== Python 自动化工具箱 =====")
    print("1. 文件批量重命名")
    print("2. 自动整理文件夹")
    print("3. 定时提醒")
    print("================================")

    choice = input("请输入功能编号：")

    if choice == "1":
        path = input("输入文件夹路径：")
        prefix = input("输入文件名前缀（默认 file_）：") or "file_"
        batch_rename(path, prefix)

    elif choice == "2":
        path = input("输入要整理的文件夹路径：")
        auto_sort(path)

    elif choice == "3":
        msg = input("输入提醒内容：")
        sec = int(input("输入延迟秒数："))
        reminder(msg, sec)

    else:
        print("无效输入")

if __name__ == "__main__":
    main()