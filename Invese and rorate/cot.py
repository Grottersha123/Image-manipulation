# split the image into individual bands
from PIL import Image

def invert(rgb,name): # попиксельно инвертируем каждый канал, который нам нужен
	px = name.load() # загружаем нашу картинку в пикселях
	lol = rgb.split(",",maxsplit = 3) # делаем из нашей строки список 
	inv = {'r':0,'g':0,'b':0} # словарь для того чтобы понять какие нам надо инвертировать каналы
	for key in inv:  # цикл для словаря , чтобы вытаскивать имена ключей
		for lis in range(len(lol)):  #цикл для списка , чтобы вытаскивать элементы списка 
			if (key == lol[lis]): # (дальше три условия , они нужны для того , чтобы понять какие каналы нужно инвертировать, если есть канал , то 1 , если нет, то ноль)
					inv[key] = 1
			if (key == lol[lis]):
					inv[key] = 1
			if (inv[key] == lol[lis]):
					inv[key] = 1
	a = list(name.size) # просто из котежа делаем список берем размер картинки 
	for i in range(a[0]): #  цикл для икса 
		for j in range(a[1]): # цикл для игрека
				px[i,j] = (abs(255*inv['r']-px[i,j][0]),abs(255*inv['g']-px[i,j][1]),abs(255*inv['b']-px[i,j][2])) # инвертируем канал из 255 * на значение ключа и вычитаем значение канала в данном пикселе




