import os
import warnings
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import shutil

# 忽略所有警告
warnings.filterwarnings("ignore")

# 水印文字
text = "E42014039_杨浩然"

# 水印字体路径，可自行选择
font_path = r"C:\Windows\Fonts\STKAITI.TTF"

# 水印颜色（默认红色）
color = (255, 0, 0)

# 比例系数
scale = 0.1

# 原始图片所在文件夹路径
source_dir = "path"

# 添加水印后的图片保存路径
target_dir = "path_W"

# 删除添加水印后的文件夹中所有内容
if os.path.exists(target_dir):
    try:
        shutil.rmtree(target_dir)
    except Exception as e:
        print(f"清空目标文件夹失败：{e}")
        exit()

try:
    os.makedirs(target_dir)
except Exception as e:
    print(f"创建目标文件夹失败：{e}")
    exit()

# 遍历原始图片文件夹下的所有JPEG和PNG文件
for filename in tqdm(os.listdir(source_dir), desc="Processing", ncols=80, ascii=True):
    if os.path.isfile(os.path.join(source_dir, filename)) and \
            (filename.endswith(".jpg") or filename.endswith(".png")):
        try:
            # 打开图像文件
            with Image.open(os.path.join(source_dir, filename)) as image:
                # 水印大小
                font_size = int(min(image.size) * scale)
                font = ImageFont.truetype(font_path, font_size)

                # 水印位置
                draw = ImageDraw.Draw(image)
                text_width, text_height = draw.textsize(text, font=font)
                position = (image.size[0] - text_width, image.size[1] - text_height)

                # 水印文字
                draw.text(position, text, font=font, fill=color)

                # 保存处理后的图像文件到目标文件夹，图片名不变
                new_filepath = os.path.join(target_dir, filename)
                image.save(new_filepath)

        except Exception as e:
            print(f"处理文件 {filename} 失败：{e}")

print("添加水印完成！")
