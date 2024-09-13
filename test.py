import time
from location import player_location
from player import player_health,player_name,player_last_name

#тестовий файл

#print місцезнаходження
print("Ви зараз знаходитесь в місті: "+player_location)
#print паспорту гравця
print("Ваше прізвище та ім'я: " + player_last_name + player_name)

#print ХП та характеристик гравця
#Форматування рядків (f-рядки):
print(f"Хітпоінти: {player_health}")
#print календаря та часу
print("2024.01.01 12:00:58")