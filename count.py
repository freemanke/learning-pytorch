import os


def count():
    dic = {}
    root = "C:\\Users\\freeman\\Documents\\jinan250"
    dirs = os.listdir(root)
    for d in dirs:
        dic[d] = len(os.listdir(os.path.join(root, d)))
    print(len(dic))
    print(dic.values())


if __name__ == '__main__':
    count()
