from gpiozero import MotionSensor, Buzzer, LED
from signal import pause
from time import sleep

# Initialize PIR sensor, buzzer, and LED
pir = MotionSensor(18, queue_len=1, sample_rate=10, threshold=0.5)  # Adjust queue_len & sample_rate for better accuracy
buzzer = Buzzer(23)  # Change GPIO pin as needed
led = LED(24)        # Change GPIO pin as needed

# Function to create a siren sound on the buzzer
def siren_alarm():
    for _ in range(5):  # Run the siren for a short duration
        buzzer.on()
        sleep(0.2)
        buzzer.off()
        sleep(0.2)

# Define functions for motion detection
def motion_function():
    print("Motion Detected!")
    led.on()
    siren_alarm()  # Play the siren sound

def no_motion_function():
    print(" Motion Stopped.")
    led.off()
    buzzer.off()

# Assign functions to PIR sensor
pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()
