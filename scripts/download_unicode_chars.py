#!/usr/bin/env python3
"""
下载Unicode古文字图片
- 楔形文字 (Cuneiform): U+12000 - U+123FF
- 圣书体 (Egyptian Hieroglyphs): U+13000 - U+1342F
"""

import os
import requests
from concurrent.futures import ThreadPoolExecutor

# 创建保存目录
BASE_DIR = "/workspace/projects/assets/ancient_scripts"
os.makedirs(f"{BASE_DIR}/cuneiform", exist_ok=True)
os.makedirs(f"{BASE_DIR}/hieroglyphs", exist_ok=True)
os.makedirs(f"{BASE_DIR}/oracle_bone", exist_ok=True)

def download_char(char_code, char_name, save_dir):
    """下载单个字符图片"""
    # 使用Unicode官方图片服务
    url = f"https://unicode.org/cgi-bin/char.gif?{char_code:04X}"
    save_path = f"{save_dir}/{char_name}.gif"
    
    if os.path.exists(save_path):
        print(f"跳过 (已存在): {char_name}")
        return
    
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200 and len(resp.content) > 100:
            with open(save_path, 'wb') as f:
                f.write(resp.content)
            print(f"下载成功: {char_name}")
        else:
            print(f"下载失败: {char_name} (状态码: {resp.status_code})")
    except Exception as e:
        print(f"错误: {char_name} - {e}")

def main():
    # 楔形文字常用字符 (部分)
    cuneiform_chars = [
        # 苏美尔语高频符号
        ("12000", "A-water"), ("12001", "I"), ("12002", "KI"),
        ("12003", "NAM"), ("12004", "GI"),
        # 天/神
        ("1202D", "AN-sky"), ("12034", "DINGIR-god"),
        # 日
        ("12313", "UTU-sun"),
        # 山
        ("121B3", "KUR-mountain"),
        # 水/河
        ("121A9", "IDIGNA-Tigris"),
        # 眼睛
        ("12186", "IGI-eye"),
        # 口
        ("12197", "KA-mouth"),
        # 谷物/麦
        ("12196", "ŠE-barley"),
        # 鱼
        ("12158", "KU6-fish"),
        # 鸟
        ("12137", "MUŠEN-bird"),
        # 牛
        ("12185", "GU4-cattle"),
        # 羊
        ("12198", "UD-sheep"),
        # 男人
        ("1214B", "LÚ-man"),
        # 女人
        ("121B8", "MUNUS-woman"),
        # 王
        ("1212A", "LUGAL-king"),
        # 牛头
        ("121A6", "GU3-ox_head"),
        # 驴
        ("12187", "ANŠE-donkey"),
        # 狗
        ("12156", "UR-gi7-dog"),
        # 猪
        ("1217B", "ŠAH-pig"),
        # 田
        ("121B9", "GAN2-field"),
        # 树/木
        ("12111", "GIŠ-tree"),
        # 芦苇
        ("121BA", "GI-reed"),
    ]
    
    # 圣书体常用字符 (Gardiner编号)
    hieroglyphs_chars = [
        # N5 太阳圆盘
        ("131F3", "N5-sun"),
        # N5 太阳+射线
        ("131F4", "N5-sun_ray"),
        # N28 新月
        ("131F9", "N28-moon"),
        # N29 波浪线(水)
        ("13217", "N29-water"),
        # N35 平行线
        ("13223", "N35-lines"),
        # D4 眼睛
        ("13079", "D4-eye"),
        # D21 嘴
        ("1308B", "D21-mouth"),
        # N25 山
        ("1320B", "N25-mountain"),
        # M1 鸟
        ("1313F", "M1-bird"),
        # F18 面包
        ("130D2", "F18-bread"),
        # R4 太阳船
        ("13283", "R4-sun_boat"),
        # G1 秃鹫
        ("131C8", "G1-vulture"),
        # G43 眼镜蛇
        ("1321B", "G43-cobra"),
        # I5 鱼
        ("131A2", "I5-fish"),
        # I10 蝎子
        ("131A7", "I10-scorpion"),
        # M17 芦苇
        ("131D7", "M17-reed"),
        # Q3 篮子
        ("13259", "Q3-basket"),
        # AA1 折叠布
        ("13380", "AA1-cloth"),
        # S29 权杖
        ("132DE", "S29-scepter"),
        # V30 盘子
        ("132E6", "V30-dish"),
    ]
    
    print("=" * 50)
    print("开始下载楔形文字图片...")
    print("=" * 50)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        for code, name in cuneiform_chars:
            executor.submit(download_char, code, name, f"{BASE_DIR}/cuneiform")
    
    print("\n" + "=" * 50)
    print("开始下载圣书体图片...")
    print("=" * 50)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        for code, name in hieroglyphs_chars:
            executor.submit(download_char, code, name, f"{BASE_DIR}/hieroglyphs")
    
    print("\n" + "=" * 50)
    print("下载完成！")
    print(f"楔形文字: {BASE_DIR}/cuneiform/")
    print(f"圣书体: {BASE_DIR}/hieroglyphs/")
    print(f"甲骨文: {BASE_DIR}/oracle_bone/ (请手动添加)")

if __name__ == "__main__":
    main()
