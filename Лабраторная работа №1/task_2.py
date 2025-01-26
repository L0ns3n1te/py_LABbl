from task_1 import Wireless_Headphones, Capacitor, Battery

if __name__ == "__main__":
    capacitor = Capacitor(100 * 10 ** -9, 350)
    my_headphones = headphones = Wireless_Headphones("Edifier", "W820NB Plus", 32)
    battery = Battery("Ni-Mh", 600, 1.2, 60)

    try:
        battery_1 = Battery("li-ion", 3000, 3.7, "2.2")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        just_headphones = headphones = Wireless_Headphones("Phillips", "TAT1108", "16")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        capacitor_1 = Capacitor(50 * 10 ^ -6, 500, "0.005")
    except TypeError:
        print('Ошибка: неправильные данные')
