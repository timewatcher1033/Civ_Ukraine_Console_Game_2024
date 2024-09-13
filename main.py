
import time
from clock import display
from location import player_location
from player import player_name,player_last_name
from input import input_name,input_last_name 


gametime = display()
print(f"{"ігрова дата "[:len(gametime)//2]}\n{"другий рядок ігрового тексту "[len("друга частина другог орядку")//2:]}")


welcome_message01 = "Вітаємо тебе у грі Цивілізація Олексія Великого 2024" 
time.sleep(1)
print(welcome_message01)

#не дописав до головного циклу інпути, вони якось не правильно працюють.
input(input_name)
input(input_last_name)




player_sex = input("Ти хлопець чи дівчина? введи будь ласка тільки Чоловік або Жінка ")
    #Порівняння якого полу гравець
if player_sex == "Чоловік":
        print("значить чоловік...добре ,поїхали далі ")
elif player_sex == "Жінка":
        print("значить дівчинка...добре ,поїхали далі ")
else:
        input("Треба вводити чітко на англійській Чоловік або Жінка ")


time.sleep(2)
print("Вітаємо ваше початкове місцеположення " + player_location)


time.sleep(2)

print("Кінець наявної частини гри")









