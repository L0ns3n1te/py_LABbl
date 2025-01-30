class Battery:
    def __init__(self, capacity: float, voltage: float) -> None:
        """
        Инициализирует аккумулятор с заданной ёмкостью и напряжением.

        :param capacity: Ёмкость аккумулятора в миллиампер-часах (мА*ч)
        :param voltage: Напряжение аккумулятора в вольтах (В)
        """
        self._capacity = capacity  # Защита от прямого доступа к атрибуту
        self._voltage = voltage

    def __str__(self) -> str:
        """
        Возвращает строковое представление аккумулятора.
        """
        return f"Battery(Capacity: {self._capacity} мА*ч, Voltage: {self._voltage} В)"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление аккумулятора.
        """
        return f"Battery(capacity={self._capacity}, voltage={self._voltage})"

    def get_energy(self) -> float:
        """
        Вычисляет энергию в ватт-часах (Вт*ч) аккумулятора.

        :return: Энергия в ватт-часах
        """
        return round((self._capacity / 1000) * self._voltage, 16)  # Энергия = ёмкость * напряжение


class CylindricalBattery(Battery):
    def __init__(self, capacity: float, voltage: float, diameter: float, height: float) -> None:
        """
        Инициализирует цилиндрический аккумулятор с заданной ёмкостью, напряжением, диаметром и высотой.

        :param capacity: Ёмкость аккумулятора в миллиампер-часах (мА*ч)
        :param voltage: Напряжение аккумулятора в вольтах (В)
        :param diameter: Диаметр аккумулятора в миллиметрах (мм)
        :param height: Высота аккумулятора в миллиметрах (мм)
        """
        super().__init__(capacity, voltage)
        self.diameter = diameter
        self.height = height

    def __str__(self) -> str:
        """
        Возвращает строковое представление цилиндрического аккумулятора.
        """
        return (f"CylindricalBattery(Capacity: {self._capacity} мА*ч, Voltage: {self._voltage} В, "
                f"Diameter: {self.diameter} мм, Height: {self.height} мм)")

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление цилиндрического аккумулятора.
        """
        return (f"CylindricalBattery(capacity={self._capacity}, voltage={self._voltage}, "
                f"diameter={self.diameter}, height={self.height})")

    def get_energy(self) -> float:
        """
        Перегруженный метод для вычисления энергии в ватт-часах (Вт*ч) с учётом формы аккумулятора.

        :return: Энергия в ватт-часах
        """
        return super().get_energy()


class FlatBattery(Battery):
    def __init__(self, capacity: float, voltage: float, width: float, length: float, height: float) -> None:
        """
        Инициализирует плоский аккумулятор с заданной ёмкостью, напряжением, шириной и длиной.

        :param capacity: Ёмкость аккумулятора в миллиампер-часах (мА*ч)
        :param voltage: Напряжение аккумулятора в вольтах (В)
        :param width: Ширина аккумулятора в миллиметрах (мм)
        :param length: Длина аккумулятора в миллиметрах (мм)
        :param height: Высота аккумулятора в миллиметрах (мм)
        """
        super().__init__(capacity, voltage)
        self.width = width
        self.length = length
        self.height = height

    def __str__(self) -> str:
        """
        Возвращает строковое представление плоского аккумулятора.
        """
        return (f"FlatBattery(Capacity: {self._capacity} мА*ч, Voltage: {self._voltage} В, "
                f"Width: {self.width} мм, Length: {self.length} мм, Height: {self.height} мм)")

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление плоского аккумулятора.
        """
        return (f"FlatBattery(capacity={self._capacity}, voltage={self._voltage}, "
                f"width={self.width}, length={self.length}, height={self.height})")

    def get_energy(self) -> float:
        """
        Перегруженный метод для вычисления энергии в ватт-часах (Вт*ч) с учётом формы аккумулятора.

        :return: Энергия в ватт-часах
        """
        return super().get_energy()
