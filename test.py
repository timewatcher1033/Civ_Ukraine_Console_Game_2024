
#тест від Gemini

player_surv_food: int = 100
player_surv_water: int = 100

def check_player_status():
    if player_surv_food <= 0 or player_surv_water <= 0:
        print("Гравець помер , ви програли :(")
    else:
        print("Ваше прізвище та ім'я: "+ player_name + player_last_name)
        print("Рівень здоров'я: "+ player_health)
        print("Зневоднення: "+ player_surv_food)
        print("Голод: "+ player_surv_food)
        print("Ви у місті: "+ player_location)
        print("Рівень здоров'я: "+ player_health)

        print("Ваші характеристики:")
        print("Сила: "+player_strenght)
        print("Спритність: "+player_agility)
        print("Інтелект: "+player_intelligence)
        print("Витривалість: "+player_stamina)
          

while True:
    check_player_status()
    
    # Оновлення значень змінних ,можна змінити на свої змінні , бо ці чисто для наглядності
    player_surv_food = int(input("Введіть нове значення харчів: "))
    player_surv_water = int(input("Введіть нове значення води: "))

                                                    # END #

 