# 导包
import json


# 定义函数，读取数据json文件
def read_json_data(path_filename):
    with open(path_filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            tmp = tuple(item.values())
            list_data.append(tmp)

    return list_data


if __name__ == '__main__':
    ret = read_json_data()
    print(ret)
