import sys
import os

#тестова змінна для ручного переміщення або прогресу по грі, увівши 0 гра закінчиться
player_alfa_test_func_check = 100

#Міста гри
ukraine_city_1 = "Київ"
ukraine_city_2 = "Дніпро"
ukraine_city_3 = "Харків"
ukraine_city_4 = "Львів"
ukraine_city_5 = "Кривий Ріг"
europe_city_1 = "Варшава"
europe_city_2 = "Лондон"
europe_city_3 = "Берлін"

#Змінна поточного місцеположення гравця
player_location = ukraine_city_1

#сюди зберігаються стать, ім'я та призвище при старті гравця
player_sex = input("Введіть будь ласка ти хлопчик чи дівчинка: ")
player_name = input("Введи ім'я гравця ")
player_last_name = input("Введи призвіще гравця ")


#статки гравця
player_health: int = 100

player_strenght: int = 1
player_agility: int = 1
player_intelligence: int = 1
player_stamina: int = 1

player_surv_food: int = 100
player_surv_water: int = 100

player_surv_food: int = 100
player_surv_water: int = 100
#Нова версія часу у грі
def increment():
  """Функція, яка збільшує внутрішнє число на 1 при кожному виклику.

  Returns:
    Нове значення числа після інкременту.
  """
  #count змінна днів або будьякого часу    
  global day  # Оголошення глобальної змінної для зберігання лічильника
  day += 1
  return day

day = 0


#функція підчищеня консолі, щоб новий вивід гри не змішувався з  старим
def clear_console():
    """Очищає консоль за допомогою команди ОС."""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Якщо ОС Windows
        command = 'cls'
    os.system(command)

#Головна функція гри
def check_player_status():
    if player_surv_food <= 0 or player_surv_water <= 0:
        print("Гравець помер , ви програли :(")
        sys.exit()
    else:
        clear_console()

        print("")

        print("Стать: "+ player_sex)
        print("Ваше прізвище та ім'я: "+ player_name + " " + player_last_name)
        print("Рівень здоров'я: "+ str(player_health))
        print("Зневоднення: "+ str(player_surv_water))
        print("Голод: "+ str(player_surv_food))
        print("Ви у місті: "+ player_location)

        print("")
    
        print("Ваші характеристики:")
        print("Сила: "+ str(player_strenght))
        print("Спритність: "+ str(player_agility))
        print("Інтелект: "+ str(player_intelligence))
        print("Витривалість: "+ str(player_stamina))

        print("")
        print("День: "+ str(increment()))
          
#Тепер можна додати щось для нових inputi'в або умов

while True:
    check_player_status()
    
    # Оновлення значень змінних ,можна змінити на свої змінні , бо ці чисто для наглядності
    player_alfa_test_func_check = int(input("Введіть нове значення щоб перейти далі... "))
    player_surv_food = int(input("Введіть нове значення харчів: "))
    player_surv_water = int(input("Введіть нове значення води: "))

                                                    # MAIN CODE END #

