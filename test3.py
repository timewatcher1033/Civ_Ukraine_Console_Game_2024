
#тест від Gemini

player_surv_food: int = 100
player_surv_water: int = 100

def check_player_status():
    if player_surv_food <= 0 or player_surv_water <= 0:
        print("Гравець помер , ви програли :(")
    else:
        print("Рівень здоров'я: "+player_health)
          

while True:
    check_player_status()
    
    # Оновлення значень змінних
    player_surv_food = int(input("Введіть нове значення харчів: "))
    player_surv_water = int(input("Введіть нове значення води: "))


