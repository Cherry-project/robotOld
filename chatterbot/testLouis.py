import Image


def main(self):
    image = Image.open('neutre.jpg')
    data = list(im.getdata())
    print(data)