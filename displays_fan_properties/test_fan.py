from fan import Fan

fan1 = Fan(Fan.FAST, 10, "Yellow", True)
fan2 = Fan(Fan.MEDIUM, 5, "Blue", False)

print("\nFAN PROPERTIES")

colors = {
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Reset": "\033[0m"
}

print("\nFAN1:")
print(f"Speed : {fan1.get_speed()}")
print(f"Radius : {fan1.get_radius()}")
color1 = fan1.get_color().capitalize()
print(f"Color : {colors.get(color1, '')}{color1}{colors['Reset']}")
print(f"Status : {"ON" if fan1.get_on() else "OFF"}")

print("\nFAN2:")
print(f"Speed : {fan2.get_speed()}")
print(f"Radius : {fan2.get_radius()}")
color2 = fan2.get_color().capitalize()
print(f"Color : {colors.get(color2, '')}{color2}{colors['Reset']}")
print(f"Status : {"ON" if fan2.get_on() else "OFF"}")