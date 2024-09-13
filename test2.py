try:
    import time
    from clock import display
    # Основний код тут
    gametime = display()
    print(f"{"ігрова дата "[:len(gametime)//2]}\n{"другий рядок ігрового тексту "[len("друга частина другог орядку")//2:]}")


    welcome_message01 = "Вітаємо тебе у грі Цивілізація Олексія Великого 2024" 
    time.sleep(1)
    print(welcome_message01)

    print(display)
except KeyboardInterrupt:
    print("Програму перервано користувачем.")
except ImportError as e:
    print(f"Помилка імпорту: {e}")