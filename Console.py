"""
python prog.py D:/test/pics 31 —inverse r
Поворачивает на 31 градус все файлы форматов (не с расширенями!) jpg и png, находящиеся в директории ~/test/pics.
17.07.15	
Параметр —inverse говорит, что в изображениях также нужно инвертировать соответствующий цветовой канал.
Примеры:
--inverse r
--inverse b,g
--inverse r,b,g
Сочетания из r,g,b могут быть любые.
"""


import argparse
import Rotate # функция , в которой поворот и инверсия 
parser = argparse.ArgumentParser(description = "Turn and invert pictures with formats .jpg or .png") # сначала создаем переменную для добавления новых команд 
parser.add_argument("directory", help = "Folder that contains pictures") #Добавляем новый аргумент конмадной строки """
parser.add_argument("degree",type=int,default = 0, help = "What degree?")
parser.add_argument("--inverse", type = str, help = "Parametrs: r - red color, g - green color, b - black color")
args = parser.parse_args() #теперь это можно вводить в консоль


Rotate.all_files(args.directory,args.degree,args.inverse ) # файлы формата jpg  и png  поворачивает на N радусов и инвертирует нужные нам каналы
#принимает путь градусы и инвертируемые каналы """
#args = parser.parse_args()


#ВСе вводится с командной строки стначала путь в конце не забудь \ дальше пишешь число градусов а потом --inverse "r,g,b" запомни, что это строчка и через запятые""""