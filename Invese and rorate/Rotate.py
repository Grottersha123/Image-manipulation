"""
поворачивает и инвертирует все картиночки на столько сколько нужно градусов и так же инвертирует по нужным нам каналам
"""


from PIL import Image # модуль Pillow 
import cot # моя функция в которой инвертируется канал картинки
import os 

def rorate(path,name,degree,rgb): # написать путь к файлу имя файла и расписать насколько ты хочешь это повернуть
	try:
		original = Image.open(path+name) # октрывает картиночки с данным путем и именнем
		out = original.rotate(degree) # поворачивает на degree градусов
		cot.invert(rgb,out) # задаем 
		out.save(path+'w'+ name) # сохраняет новый повернутый файл
	except:
		print ("Can't to load this, it's not png and jpg")
def all_files(directory,degree,rgb):# все файлы в данной директории 
	files = os.listdir(directory)
	namejp = list(filter(lambda x: x.endswith('.jpg'),files)) # выбирает все файлы с расширением jpg
	namepn = list(filter(lambda x: x.endswith('.png'),files)) # png
	for name in namejp:
		rorate(directory,name,degree,rgb) # все имена из списка с jpg поворачивает
	for name in namepn:
		rorate(directory,name,degree,rgb) #все имена из списка с png поворачивает
		
	
all_files("D:\Python\\",45,'r')
#rorate("D:\Python\\","Hurt.jpg",90,'r,g,b')



