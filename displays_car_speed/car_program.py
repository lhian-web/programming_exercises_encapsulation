from car import Car
import time

car = Car(1993, "Toyota Supra")

print("Ready...")
print("3...")
time.sleep(0.5)
print("2...")
time.sleep(0.5)
print("1...")
time.sleep(0.5)
print("GO!\n")

print("ACCELERATING!")
for i in range(5):
    car.accelerate()
    print(f"Accelerating... Current speed: {car.get_speed()} km/h")

print("\nBRAKING!")
for i in range(5):
    car.brake()
    print(f"Braking... Current speed: {car.get_speed()} km/h")

print("\nCar stopped.")