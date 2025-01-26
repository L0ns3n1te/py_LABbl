class Capacitor:
    def __init__(self, capacitance: float, voltage_rating: float, charge: float = 0.0):
        """
        Инициализация конденсатора.

        :param capacitance: Емкость конденсатора в фарадах (должна быть положительной).
        :param voltage_rating: Допустимое напряжение в вольтах (должно быть положительным).
        :param charge: Заряд на конденсаторе в кулонах (должен быть не меньше 0).

        :raises ValueError: Если емкость или допустимое напряжение не положительны или заряд меньше 0 или больше
        максимального возможного значения.
        """
        if 0 <= charge <= capacitance * voltage_rating and capacitance > 0 and voltage_rating > 0:
            self.capacitance = capacitance  # в фарадах
            self.voltage_rating = voltage_rating  # в вольтах
            self.charge = charge
        elif capacitance <= 0:
            raise ValueError("Емкость должна быть положительной!")
        elif voltage_rating <= 0:
            raise ValueError("Допустимое напряжение должно быть положительным!")
        elif charge < 0:
            raise ValueError("Заряд должен быть неотрицательным!")
        elif charge > capacitance * voltage_rating:
            raise ValueError("Заряд не должен превышать максимальное возможное значение!")

    def to_charge(self, voltage: float) -> None:
        """
        Зарядка конденсатора.

        :param voltage: Напряжение в вольтах, при котором происходит зарядка.

        :raises ValueError: Если напряжение больше, чем допустимое для конденсатора.

        :return: Заряд, накопленный в конденсаторе в кулонах.

        >>> capacitor = Capacitor(0.001, 10)
        >>> capacitor.to_charge(5)
        """
        if voltage > self.voltage_rating:
            raise ValueError(f"Напряжение не должно превышать {self.voltage_rating} В!")

        # Q = C * V
        self.charge = self.capacitance * voltage

    def energy_stored(self, voltage: float) -> float:
        """
        Вычисление энергии, сохраненной в конденсаторе.

        :param voltage: Напряжение в вольтах, при котором вычисляется энергия.

        :raises ValueError: Если напряжение больше, чем допустимое для конденсатора.

        :return: Энергия в джоулях.

        >>> capacitor = Capacitor(0.001, 10)
        >>> capacitor.energy_stored(5)
        0.0125
        """
        if voltage > self.voltage_rating:
            raise ValueError(f"Напряжение не должно превышать {self.voltage_rating} В!")

        # W = 0.5 * C * V^2
        return 0.5 * self.capacitance * voltage ** 2


class Wireless_Headphones:
    def __init__(self, brand: str, model: str, impedance: float, charge_level: int = 0):
        """
        Инициализация беспроводных наушников.

        :param brand: Бренд наушников (должен быть строкой).
        :param model: Модель наушников (должна быть строкой).
        :param impedance: Импеданс наушников в омах (должен быть положительным).
        :param charge_level: Уровень заряда наушников в процентах (по умолчанию 0, должен быть между 0 и 100).

        :raises ValueError: Если импеданс не положителен или уровень заряда выходит за допустимые пределы.
        """
        if impedance > 0 and 0 <= charge_level <= 100:
            self.brand = brand
            self.model = model
            self.impedance = impedance  # в омах
            self.charge_level = charge_level
        elif impedance <= 0:
            raise ValueError("Импеданс должен быть положительным!")
        elif 0 < charge_level or charge_level > 100:
            raise ValueError("Уровень заряда должен быть между 0 и 100!")

    def connect(self, device: str) -> str:
        """
        Подключение наушников к устройству.

        :param device: Устройство, к которому подключаются наушники (должно быть строкой).

        :return: Строка, подтверждающая подключение.

        >>> headphones = Wireless_Headphones("Edifier", "W820NB Plus", 32)
        >>> headphones.connect("Vivo Y31(2021)")
        'Наушники Edifier W820NB Plus подключены к Vivo Y31(2021).'
        """
        return f"Наушники {self.brand} {self.model} подключены к {device}."

    def charge(self, amount: int) -> None:
        """
        Зарядка наушников.

        :param amount: Количество заряда для добавления в процентах (должно быть положительным).

        :raises ValueError: Если количество заряда не положительно, или перевышивает 100%.

        >>> headphones = Wireless_Headphones("Edifier", "W820NB Plus", 32)
        >>> headphones.charge(50)
        >>> headphones.charge_level
        50
        """
        if amount <= 0:
            raise ValueError("Количество заряда должно быть положительным.")
        if self.charge_level + amount > 100:
            raise ValueError("Уровень заряда не может превышать 100%.")

        self.charge_level += amount


class Battery:
    def __init__(self, type_: str, capacity: float, voltage: float, charge_level: int = 0):
        """
        Инициализация аккумулятора.

        :param type_: Тип аккумулятора.
        :param capacity: Емкость аккумулятора в миллиампер-часах (должна быть положительной).
        :param voltage: Напряжение аккумулятора в вольтах (должно быть положительным).
        :param charge_level: Уровень заряда аккумулятора в процентах (по умолчанию 0, должен быть между 0 и 100).

        :raises ValueError: Если емкость или напряжение не положительны, или уровень заряда вне диапазона.
        """
        if capacity <= 0:
            raise ValueError("Емкость должна быть положительной.")
        if voltage <= 0:
            raise ValueError("Напряжение должно быть положительным.")
        if not (0 <= charge_level <= 100):
            raise ValueError("Уровень заряда должен быть между 0 и 100.")

        self.type_ = type_
        self.capacity = capacity  # В ампер-часах
        self.voltage = voltage  # В вольтах
        self.charge_level = charge_level  # В процентах

    def charge(self, amount: int) -> None:
        """
        Зарядка аккумулятора.

        :param amount: Количество заряда для добавления в процентах (должно быть положительным).

        :raises ValueError: Если количество заряда не положительно, или перевышивает 100%.

        >>> battery = Battery("li-ion", 100, 12)
        >>> battery.charge(50)
        >>> battery.charge_level
        50
        """
        if amount <= 0:
            raise ValueError("Количество заряда должно быть положительным.")
        if self.charge_level + amount > 100:
            raise ValueError("Уровень заряда не может превышать 100%.")

        self.charge_level += amount

    def discharge(self, amount: int) -> None:
        """
        Разрядка аккумулятора.

        :param amount: Количество заряда для уменьшения в процентах (должно быть положительным).

        :raises ValueError: Если количество заряда не положительно, или превышает текущий уровень заряда.

        >>> battery = Battery("li-ion", 100, 12, 50)
        >>> battery.discharge(20)
        >>> battery.charge_level
        30
        """
        if amount <= 0:
            raise ValueError("Количество заряда должно быть положительным.")
        if amount > self.charge_level:
            raise ValueError("Уровень заряда не может быть отрицательным.")

        self.charge_level -= amount

    def get_power(self) -> float:
        """
        Получение доступной мощности в ваттах.

        :return: Доступная мощность в ваттах.

        >>> battery = Battery("Ni-Mh", 100, 12, 50)
        >>> battery.get_power()
        0.6
        """
        return round((self.charge_level / 100) * (self.capacity / 1000) * self.voltage, 15)
