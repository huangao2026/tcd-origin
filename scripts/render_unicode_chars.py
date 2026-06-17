#!/usr/bin/env python3
"""
使用Pillow渲染Unicode古文字字符为图片
需要安装: pip install Pillow
"""

import os
from PIL import Image, ImageDraw, ImageFont

# 创建保存目录
BASE_DIR = "/workspace/projects/assets/ancient_scripts"
os.makedirs(f"{BASE_DIR}/cuneiform", exist_ok=True)
os.makedirs(f"{BASE_DIR}/hieroglyphs", exist_ok=True)
os.makedirs(f"{BASE_DIR}/oracle_bone", exist_ok=True)

# 字体映射 - 使用系统或下载的字体
# 尝试多个字体
FONT_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
]

def get_font(size=120):
    """尝试加载可用的字体"""
    for font_path in FONT_PATHS:
        try:
            return ImageFont.truetype(font_path, size)
        except:
            continue
    return ImageFont.load_default()

def create_char_image(char, save_path, bg_color=(255,255,255), fg_color=(0,0,0)):
    """创建单个字符图片"""
    if os.path.exists(save_path):
        print(f"跳过: {save_path}")
        return
    
    img = Image.new('RGB', (200, 200), bg_color)
    draw = ImageDraw.Draw(img)
    font = get_font(120)
    
    # 计算字符居中位置
    bbox = draw.textbbox((0, 0), char, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (200 - text_width) // 2
    y = (200 - text_height) // 2
    
    draw.text((x, y), char, font=font, fill=fg_color)
    img.save(save_path, 'PNG')
    print(f"生成: {save_path}")

def main():
    # 楔形文字常用字符
    cuneiform_chars = [
        # 苏美尔语高频符号
        ("𒀀", "A-water"), ("𒁹", "I"), ("𒆠", "KI"),
        ("𒉣", "NAM"), ("𒂟", "GI"),
        # 天/神
        ("𒀭", "AN-sky"), ("𒁮", "DINGIR-god"),
        # 日
        ("𒌓", "UTU-sun"),
        # 山
        ("𒆳", "KUR-mountain"),
        # 水
        ("𒀀", "A-water"),
        # 眼睛
        ("𒅆", "IGI-eye"),
        # 口
        ("𒅗", "KA-mouth"),
        # 谷物
        ("𒊨", "SE-barley"),
        # 鱼
        ("𒈪", "fish"),
        # 鸟
        ("𒄤", "bird"),
        # 牛
        ("𒄤", "cattle"),
        # 王
        ("𒈗", "LUGAL-king"),
        # 树/木
        ("𒄑", "GIS-tree"),
        # 芦苇
        ("𒂅", "GI-reed"),
        # 田
        ("𒃷", "GAN-field"),
        # 手
        ("𒊊", "SU-hand"),
        # 脚
        ("𒉾", "foot"),
        # 心
        ("�心跳", "heart"),
        # 房子
        ("𒂊", "E-house"),
    ]
    
    # 圣书体常用字符
    hieroglyphs_chars = [
        # 太阳
        ("𓇳", "sun-disk"),
        # 月亮
        ("𓇽", "moon"),
        # 水/尼罗河
        ("𓈗", "water-Nile"),
        # 眼睛
        ("𓁹", "eye-horus"),
        # 嘴巴
        ("𓂋", "mouth"),
        # 山
        ("𓈋", "mountain"),
        # 鸟
        ("𓆭", "bird"),
        ("𓄿", "vulture"),
        # 鱼
        ("𓅐", "fish"),
        # 蝎子
        ("𓆰", "scorpion"),
        # 芦苇
        ("𓎡", "papyrus"),
        # 蛇
        ("𓆓", "serpent"),
        # 狮子
        ("𓍋", "lion"),
        # 牛头
        ("𓃀", "ox-head"),
        # 面包
        ("𓊃", "bread"),
        # 篮子
        ("𓋴", "basket"),
        # 权杖
        ("𓋹", "was-scepter"),
        # 生命
        ("𓂀", "ankh"),
        # 太阳船
        ("𓇥", "sun-boat"),
        # 心脏
        ("𓍶", "heart"),
        # 手
        ("𓂧", "hand"),
        # 脚
        ("𓆑", "leg"),
    ]
    
    print("=" * 50)
    print("开始生成楔形文字图片...")
    print("=" * 50)
    
    for char, name in cuneiform_chars:
        create_char_image(char, f"{BASE_DIR}/cuneiform/{name}.png")
    
    print("\n" + "=" * 50)
    print("开始生成圣书体图片...")
    print("=" * 50)
    
    for char, name in hieroglyphs_chars:
        create_char_image(char, f"{BASE_DIR}/hieroglyphs/{name}.png")
    
    print("\n" + "=" * 50)
    print("生成完成！")
    print(f"楔形文字: {BASE_DIR}/cuneiform/")
    print(f"圣书体: {BASE_DIR}/hieroglyphs/")
    print(f"甲骨文: {BASE_DIR}/oracle_bone/ (请手动添加)")
    print("=" * 50)

if __name__ == "__main__":
    main()
