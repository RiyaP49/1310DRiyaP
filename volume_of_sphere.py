Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> 
>>> def calculate_volume_of_sphere(radius):
...     volume = (4/3) * math.pi * (radius**3)
...     return volume
... 
>>> if __name__ == "__main__":
...     radius1 = 30
...     radius2 = 40
...     volume1 = calculate_volume_of_sphere(radius1)
...     volume2 = calculate_volume_of_sphere(radius2)
... 
...     
>>> print(f"Volume of sphere with radius {radius1} is {volume1}")
Volume of sphere with radius 30 is 113097.33552923254
>>> print(f"Volume of sphere with radius {radius2} is {volume2}")
Volume of sphere with radius 40 is 268082.573106329
