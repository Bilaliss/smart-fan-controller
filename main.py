import time
import random

def read_temperature():
    # Simula lettura da un sensore
    return round(random.uniform(20.0, 40.0), 2)

def fan_control(temp):
    if temp < 25:
        return "OFF"
    elif temp < 30:
        return "LOW"
    elif temp < 35:
        return "MEDIUM"
    else:
        return "HIGH"

if __name__ == "__main__":
    while True:
        temperature = read_temperature()
        fan_state = fan_control(temperature)
        print(f"Temperatura: {temperature}°C → Ventola: {fan_state}")
        time.sleep(2)
