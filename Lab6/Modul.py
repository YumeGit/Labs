import math

def calculate_circle_area(radius):
    """
    Рассчитывает площадь круга по заданному радиусу.
    
    Аргументы:
    radius (float): Радиус круга.
    
    Возвращает:
    float: Площадь круга.
    """
    return math.pi * radius**2

def calculate_circle_diameter(radius):
    """
    Рассчитывает диаметр круга по заданному радиусу.
    
    Аргументы:
    radius (float): Радиус круга.
    
    Возвращает:
    float: Диаметр круга.
    """
    return 2 * radius

def calculate_circle_radius(diameter):
    """
    Рассчитывает радиус круга по заданному диаметру.
    
    Аргументы:
    diameter (float): Диаметр круга.
    
    Возвращает:
    float: Радиус круга.
    """
    return diameter / 2

radius = float(input("Введите радиус круга: "))

diameter = calculate_circle_diameter(radius)
area = calculate_circle_area(radius)
calculated_radius = calculate_circle_radius(diameter)

print(f"Радиус: {radius}")
print(f"Диаметр: {diameter}")
print(f"Площадь круга: {area}")
print(f"Рассчитанный радиус (по диаметру): {calculated_radius}")
