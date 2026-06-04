from fan import Fan

fan1 = Fan(Fan.FAST, 10, "Yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "Blue", False)

print("\nFAN PROPERTIES")

print("\nFAN1:")
print(f"Speed : {fan1.get_speed()}")
print(f"Radius : {fan1.get_radius()}")
print(f"Color : {fan1.get_color()}")
print(f"Status : {"ON" if fan1.get_on() else "OFF"}")

print("\nFAN2:")
print(f"Speed : {fan2.get_speed()}")
print(f"Radius : {fan2.get_radius()}")
print(f"Color : {fan2.get_color()}")
print(f"Status : {"ON" if fan2.get_on() else "OFF"}")