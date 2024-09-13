#by ChatGPT
import time

class GameTime:
    def __init__(self):
        self.year = 1
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 0
        self.second = 0
    
    def tick(self):
        # Збільшуємо секунди
        self.second += 1
        
        # Перевірка на переповнення секунд
        if self.second >= 60:
            self.second = 0
            self.minute += 1
        
        # Перевірка на переповнення хвилин
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
        
        # Перевірка на переповнення годин
        if self.hour >= 24:
            self.hour = 0
            self.day += 1
        
        # Перевірка на переповнення днів (припускаємо 30 днів у місяці для спрощення)
        if self.day > 30:
            self.day = 1
            self.month += 1
        
        # Перевірка на переповнення місяців
        if self.month > 12:
            self.month = 1
            self.year += 1
    
    def display(self):
        # Форматований вивід дати і часу
        return f"{self.year} рік / {self.day} січня {self.hour:02}г:{self.minute:02}хв:{self.second:02}с ночі"

def main_game_loop():
    game_time = GameTime()
    
    try:
        while True:
            # Оновлюємо час
            game_time.tick()
            
            # Очищення консолі перед виводом (необов'язково, але покращує вигляд)
            print("\033[H\033[J", end="")
            
            # Виводимо поточний час
            print(game_time.display())
            
            # Затримка на 1 секунду
            time.sleep(1)
    except KeyboardInterrupt:
        # Завершення гри при натисканні Ctrl+C
        print("Гра завершена.(Debug text from clock.py)")
        
# Запускаємо головний цикл гри
main_game_loop()
