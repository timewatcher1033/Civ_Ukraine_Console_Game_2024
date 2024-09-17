
#сюди зберігаються ім'я та призвище при старті гравця
#перевірка його хіт поінтів
player_name: str = None
player_last_name: str = None

player_name: str = "Nosach"
player_last_name: str = "Alex"

player_health: int = 100

player_strenght= 1
player_agility= 1 
player_intelligence= 1
player_stamina= 1

player_surv_food= 100
player_surv_water= 100


print("тут почалася перевірка чи живий гравець")

def player_alive(player_health):
  """Перевіряє, чи гравець ще живий.

  Args:
    player_health: Поточне здоров'я гравця.

  Returns:
    True, якщо гравець живий, False - інакше.
  """

  return player_health > 0

# 