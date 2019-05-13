import os

from PIL import Image,  ImageDraw,  ImageFont,  ImageFilter
import numpy as np
import random, time


# 随机字母:
def rndChar():
    return chr(random.randint(65,  90))


# 随机颜色1:
def rndColor():
    return (random.randint(64,  255),  random.randint(64,  255),  random.randint(64,  255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32,  127),  random.randint(32,  127),  random.randint(32,  127))


# 随机自定义字符
def my_random_str(my_str_list, n):
    return random.sample(my_str_list, n)
    # return my_str_list


def mk_captcha(my_str_list, width, height, num_of_str, font=20, gray_value=255,
               font_family=r'D:\scene_type\pycapt\pycapt\word_ttc\ZiTiGuanJiaYinXiangTi-1.ttf'):  # font 设置字体大小 字体类型
    image = Image.new('RGB',  (width,  height), (225, 225, 225))

    # 创建Font对象:
    font = ImageFont.truetype(font_family,  font)

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            # draw.point((x,  y),  fill=rndColor())
            draw.point((x,  y),  fill=(255,  255,  255))

    # 输出文字:
    char_list = my_random_str(my_random_str(my_str_list, 4), num_of_str)

    for t in range(num_of_str):
        # rndColor2()
        draw.text((25+8 * t,  1),  char_list[t],  font=font,  fill=(0, 0, 255))  # 字体位置

    # image = image.filter(ImageFilter.BLUR)  # 模糊效果

    # image.save('train_imgs/1.png',  'jpeg');
    return char_list, image


if __name__ == '__main__':
    # 测试
    # info_list = ""
    # for i in range(10000*10):
    #     a,  b = mk_captcha(['a', 'q', '2', 'S'], 100, 30, 4)
    # print(a)
    # b.show()


    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in range(100):
        print(j)
        a, b = mk_captcha(characters, 100, 30, 4)
        timec = str(time.time()).replace(".", "")
        # p = os.path.join(r"D:\scene_type\cnn_captcha\sample\train", "{}_{}.{}".format("".join(a), timec, "png"))
        p = os.path.join(r"D:\scene_type\cnn_captcha\sample\test", "{}.{}".format("".join(a), "png"))
        b.save(p)
