# This is a sample Python script.
class Image:
    def __init__(self,title_str):
        self.resolution='1920x860'
        self.title = title_str
        self.extension = 'jpeg'

    def resize(self,resolution_new):
        self.resolution =resolution_new

    def __str__(self):
        return f"{self.title}.{self.extension}"



    def __add__(self, other):
        # Создаем новое название, объединяя названия с помощью подчеркивания
        new_title = f"{self.title}_{other.title}"
        # Выбираем максимальное разрешение
        # Предполагается, что разрешение в формате 'ширинаxвысота'
        new_resolution = max(self.resolution, other.resolution, key=lambda x: [int(i) for i in x.split('x')])
        new_image = Image(new_title)
        new_image.resize(new_resolution)
        # Предполагаем, что расширение нового изображения будет таким же, как и у первого
        new_image.extension = self.extension
        return new_image

    def __eq__(self, other):
        return self.resolution == other.resolution and self.title == other.title and self.extension == other.extension

# Пример использования
img1 = Image("Mountain")
img1.resize("1920x1080")
img2 = Image("River")
img2.resize("2560x1440")

img3 = img1 + img2
print(img3)  # Mountain_River.jpeg
print(img3.resolution)  # 2560x1440

print (type(img3))

# Сравнение изображений
img4 = Image("Mountain")
img4.resize("1920x1080")
print(img1 == img4)  # True или False, в зависимости от того, как был изменен класс


image1 = Image('Hello')
image1.resize('1080X480')

image2 = Image('Congratulate')
print(image2.__dict__)

print(image1.__dict__)

image2.title=(image2.title).upper()

print(image2.__dict__)




list_1 = ['Привет', False, 10.12, 5,{1:'Fedor'}]
list2 = list_1[:]
k = list2.pop(-2)
list2[-1].setdefault('3','Ваня')
list3=[15,'Пк']
list2.extend(list3)
print(id(list_1),list_1)
print(id(list2),list2)

print ('Введите пары значени для словаря \n')
my_dict = dict()
for i in range(3):
    key,value = input('Введите через пробел ключ и значение элемента:').split(' ')
    my_dict[key] = value

print(my_dict)
