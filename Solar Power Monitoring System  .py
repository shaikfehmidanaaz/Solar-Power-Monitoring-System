# Solar Power Monitoring System
# Python Project for EEE Students

class SolarPowerMonitor:

    def __init__(self, voltage, current, battery_voltage,
                 battery_capacity):
        self.voltage = voltage
        self.current = current
        self.battery_voltage = battery_voltage
        self.battery_capacity = battery_capacity

    # Calculate solar power
    def calculate_power(self):
        return self.voltage * self.current

    # Calculate energy generated
    def calculate_energy(self, hours):
        power = self.calculate_power()
        return (power * hours) / 1000  # kWh

    # Estimate battery percentage
    def battery_percentage(self):
        # Example: 10V = 0%, 14V = 100%
        percentage = ((self.battery_voltage - 10) / 4) * 100

        if percentage < 0:
            percentage = 0
        elif percentage > 100:
            percentage = 100

        return percentage

    # Display monitoring information
    def display(self, hours):

        power = self.calculate_power()
        energy = self.calculate_energy(hours)
        battery = self.battery_percentage()

        print("\n======================================")
        print("      SOLAR POWER MONITORING SYSTEM")
        print("======================================")

        print(f"Solar Voltage       : {self.voltage:.2f} V")
        print(f"Solar Current       : {self.current:.2f} A")
        print(f"Solar Power         : {power:.2f} W")
        print(f"Operating Time      : {hours:.2f} hours")
        print(f"Energy Generated    : {energy:.2f} kWh")

        print(f"Battery Voltage     : "
              f"{self.battery_voltage:.2f} V")

        print(f"Battery Capacity    : "
              f"{self.battery_capacity:.2f} Ah")

        print(f"Battery Level       : "
              f"{battery:.1f}%")

        print("\n----------- SYSTEM STATUS -----------")

        if power > 0:
            print("Solar Panel Status  : GENERATING POWER")
        else:
            print("Solar Panel Status  : NO POWER")

        if battery >= 80:
            print("Battery Status      : HIGH")
        elif battery >= 40:
            print("Battery Status      : NORMAL")
        else:
            print("Battery Status      : LOW")

        print("======================================")


# Get input from user

voltage = float(input("Enter Solar Voltage (V): "))
current = float(input("Enter Solar Current (A): "))
battery_voltage = float(input("Enter Battery Voltage (V): "))
battery_capacity = float(input("Enter Battery Capacity (Ah): "))
hours = float(input("Enter Operating Time (hours): "))

# Validate input

if voltage < 0 or current < 0:
    print("Voltage and current cannot be negative.")

elif battery_voltage < 0 or battery_capacity <= 0:
    print("Invalid battery values.")

elif hours < 0:
    print("Operating time cannot be negative.")

else:
    monitor = SolarPowerMonitor(
        voltage,
        current,
        battery_voltage,
        battery_capacity
    )

    monitor.display(hours)
