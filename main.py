class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        if celsius < -273.15:  # Абсолютний нуль
            raise ValueError("Недопустиме значення температури")
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        if fahrenheit < -459.67:  # Абсолютний нуль
            raise ValueError("Недопустиме значення температури")
        return (fahrenheit - 32) * 5/9


converter = TemperatureConverter()

try:
    celsius = float(input("Введіть температуру в градусах Цельсія: "))
    fahrenheit = converter.celsius_to_fahrenheit(celsius)
    print(f"{celsius} градусів Цельсія = {fahrenheit} градусів Фаренгейта")
except ValueError as e:
    print("Помилка:", e)

try:
    fahrenheit = float(input("Введіть температуру в градусах Фаренгейта: "))
    celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} градусів Фаренгейта = {celsius} градусів Цельсія")
except ValueError as e:
    print("Помилка:", e)