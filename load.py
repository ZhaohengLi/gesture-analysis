import json

folder = './uploads'


def tset():
    with open("./uploads/1-10.json", 'r') as file:
        data = json.load(file)
        print(data)


if __name__ == '__main__':
    tset()
    pass
