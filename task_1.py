# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Account:
    def __init__(self, total_cash: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Счёт"

        :param total_cash: Общая сумма  денежных средств

        Пример:
        >>> acc = Account(50000000)
        """

        if not isinstance(total_cash, (int, float)):
            raise TypeError("Общая сумма  денежных средств должна быть типа int или float")
        if total_cash < 0:
            raise ValueError("Общая сумма денежных средств не может быть отрицательной")
        self.total_cash = total_cash



    def add_money_to_budget(self, money: Union[int,float]) -> None:
        """
        Добавление денег на счёт .
        :param money: Количество добавляемых средств

        Примеры:
        >>> acc = Account(5000000)
        >>> acc.add_money_to_budget(2000000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Денежная сумма должна быть обозначана типом  int или float")
        if money < 0:
            raise ValueError("Эта функциия добавляет деньги на счёт")
        ...

    def to_take_the_money(self, money: Union[int, float]) -> None:
        """
        Снятие наличных со счёта .

        :param money: Значение снимаемой сумы
        :raise ValueError: Если количество снимаемых средств больше лежачих на счету

        Примеры:
        >>> acc = Account(5000000)
        >>> acc.to_take_the_money(3000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Денежная сумма должна быть обозначана типом  int или float")
        ...

    def current_value(self) -> (int, float):
        """
        Функция которая показывает количество средств на счету

        :return Количество средств на счёте
        Примеры:
        >>> acc = Account(50000000)
        >>> acc.to_take_the_money(3000)
        >>> acc.current_value()
        """
        ...

class Powerbank:
    def __init__(self, max_charge: Union[int, float], current_charge: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Переносное зарядное устройство"

        :param max_charge: Объём батареи
        :param current_charge: Текущее значени заряда

        """

        if not isinstance(max_charge, (int, float)):
            raise TypeError("Значение ёмкости должно быть в int или float")
        if max_charge < 0:
            raise ValueError("Объём батареи не может быть отрицательным ")
        self.max_charge = max_charge

        if not isinstance(current_charge, (int, float)):
            raise TypeError("Значение заряда должно быть  int или float")
        if max_charge < current_charge:
            raise ValueError("Заряд батареи не может быть выше максимального")
        if current_charge < 0:
            raise ValueError("Заряд не может быть отрицательным")
        self.current_charge = current_charge

    def charge_device(self, device_capacity: Union[int, float]) -> bool:
        """
        Подключение устройства для зарядки

        param: device_capacity: Ёмкость батареи подключаемого утсройства

        return: Зарядится ли девайс на полную

        """
        if not isinstance(device_capacity, (int, float)):
            raise TypeError("Объём батареи должен быть задан  int или float")
        if device_capacity < 0:
            raise ValueError("Объём батареи устройства не может быть отрицательным")
        ...

    def charge_powerbank(self, charging_power: int) -> (int, float):
        """
        Функция которая ставит Powerbank на зарядку,  и расчитывает время до полной зарядки

        param: charging power: Мощность зарядного устройства

        return: Время до полной зарядки
        """
        if not isinstance(charging_power, (int, float)):
            raise TypeError("Мощность должна быть задана int или float ")
        if charging_power <= 0:
            raise ValueError("Мощность должна быть положительной")
        ...

class Cube:
    def __init__(self, length: Union[int, float], width: Union[int, float], height: Union[int,float]):
        """
              Создание и подготовка к работе объекта "Куб"

              :param length: Длина многогранника
              :param width: Ширина многогранника
              :param height: Высота многогранника

              Пример:
              >>> Figure = Cube(5, 5.6, 10)
              """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть задана в int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть задана в int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть задана в int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def cube_volume(self) -> (int, float):
        """
        Функция которая считает обЪём куба

        return: Значение объёма
        Пример:
        >>> figure = Cube(5, 5.6, 10)
        >>> figure.cube_volume()
        """
        ...

    def cube_surface_area(self) -> (int, float):
        """
        Функция которая считает площадь поверхности куба

        return: Значение площади поверхности
        Пример:
        >>> figure = Cube(5, 5.6, 10)
        >>> figure.cube_surface_area()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
