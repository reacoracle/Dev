"""
    将图片转为Base64编码
"""

import base64

if __name__ == "__main__":
    image_path = './b90c1d6ed6f8bc4d0502b32d5cc42419.jpeg'
    with open(image_path, 'rb') as f:
        img_info = f.read()
        img_base64 = str(base64.b64encode(img_info), encoding='utf-8')
        img_base64_bin = img_base64.encode(encoding='utf-8')
        # print(img_base64)
        print(img_base64_bin)