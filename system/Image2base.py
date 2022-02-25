import os.path
import base64

def image_to_base64(filename, path):
    path = os.path.join(path, filename)
    # 转为二进制格式
    with open(path, "rb") as f:
        data = str(base64.b64encode(f.read()), "utf-8")
    return data
