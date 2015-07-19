from PIL import Image
import os

def rorate(path,name,degree):
	try:
		original = Image.open(path+name) # октрывает картиночки с данным путем и именнем
		out = original.rotate(degree) # поворачивает на degree градусов
		out.save(path+'w'+ name) # сохраняет новый повернутый файл
	except:
		print ("Can't to load this, it's not png and jpg")
def all_files(directory,degree):
	files = os.listdir(directory)
	namejp = list(filter(lambda x: x.endswith('.jpg'),files)) # выбирает все файлы с расширением jpg
	namepn = list(filter(lambda x: x.endswith('.png'),files)) # png
	for name in namejp:
		rorate(directory,name,degree)
	for name in namepn:
		rorate(directory,name,degree)
		

all_files("D:\Python\\",45)
#rorate("D:\Python\\","Lol.jpg",90)



