# Import necessary libraries
from gpiozero import LED, Button, MotionSensor, Buzzer 
import smtplib
from email.message import EmailMessage
from signal import pause
from time import sleep
from datetime import datetime
import threading

# Create objects to refer to the LED, the button, and the PIR sensor
led_status = LED(24)
button = Button(27)
pir = MotionSensor(18, queue_len=1, threshold=0.5)  # Improved sensitivity settings
buzzer=Buzzer(23)
# Email configuration
from_email_addr = "peteparker31800@gmail.com"
from_email_password = "iknb eigg yyri kina"
to_email_addr = "wishwadehi190@gmail.com"
email_subject = "[WARNING!] Intruder Alert!"

# Control variables
motion_sensor_status = False
email_cooldown = False

def siren_alarm():
    for _ in range(5):  # Run the siren for a short duration
        buzzer.on()
        sleep(0.2)
        buzzer.off()
        sleep(0.2)
# Function to send email in a separate thread
def send_email_thread():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    email_body = f"Motion was detected in your room at {current_time}!"
    
    try:
        # Create a message object
        msg = EmailMessage()
        # Set the email body
        msg.set_content(email_body)
        # Set sender and recipient
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        # Set your email subject
        msg['Subject'] = email_subject
        
        # Connect to server and send email
        print(f"[{current_time}] Connecting to email server...")
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email_addr, from_email_password)
            server.send_message(msg)
        
        print(f"[{current_time}] Email sent successfully!")
    except Exception as e:
        print(f"[{current_time}] Email error: {e}")

# Arm or disarm the PIR sensor
def arm_motion_sensor():
    global motion_sensor_status
    global email_cooldown
    
    if motion_sensor_status:
        motion_sensor_status = False
        led_status.off()
        buzzer.off()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Motion Sensor DEACTIVATED")
    else:
        motion_sensor_status = True
        email_cooldown = False
        led_status.on()
        siren_alarm()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Motion Sensor ACTIVATED")

# Handle motion detection and email sending
def handle_motion():
    global email_cooldown
    global motion_sensor_status
    
    if motion_sensor_status and not email_cooldown:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Motion Detected!")
        
        # Set cooldown to prevent email flooding
        email_cooldown = True
        
        # Send email in a separate thread to avoid blocking
        email_thread = threading.Thread(target=send_email_thread)
        email_thread.daemon = True
        email_thread.start()
        
        # Reset cooldown after delay
        def reset_cooldown():
            global email_cooldown
            sleep(30)  # 30 second cooldown between emails
            email_cooldown = False
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ready to detect motion again")
        
        cooldown_thread = threading.Thread(target=reset_cooldown)
        cooldown_thread.daemon = True
        cooldown_thread.start()

# Print startup message
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Motion detection system initialized")
print("Press the button to activate/deactivate the motion sensor")

# Assign button handler
button.when_pressed = arm_motion_sensor

# Assign motion handler
pir.when_motion = handle_motion

# Keep program running
pause()
