import machine 
import time

# Define the ADC pin (A0)
adc_pin = machine.ADC(machine.Pin(13))

# Initialize the ADC object
adc_pin.atten(machine.ADC.ATTN_11DB)  # Set attenuation for 3.3V input
adc_pin.width(machine.ADC.WIDTH_12BIT)  # Set the resolution to 12 bits

def get_voltage():
    """
    Reads the ADC value and converts it to voltage.
    """
    raw_value = adc_pin.read()
    voltage = raw_value * (5 / 4095)  # 3.3V is the reference voltage, 4095 is the maximum value
    return voltage

def get_current():
    """
    Calculates the current based on the voltage reading.
    """
    voltage = get_voltage()
    current = (4.1- voltage)/ 0.185  # Adjust constants as needed
    return current

def main():
    """
    Main loop to continuously read and print voltage and current.
    """
    while True:
        voltage = get_voltage()
        current = get_current()

        print(f"Raw Voltage: {voltage:.2f} V")
        print(f"Motor Current: {current:.2f} mA")

        time.sleep(1)  # Wait for 1 second before reading again

if __name__ == "__main__":
    main()