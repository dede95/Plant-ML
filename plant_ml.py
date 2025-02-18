import tensorflow as tf
import numpy as np
import cv2
import serial
import time
import os
CWD = os.getcwd()

# 🚀 Load the local Teachable Machine model
MODEL_PATH = f"{CWD}/plant_ml_model/keras_model.h5"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model Loaded Successfully")
except Exception as e:
    print(f"⚠️ Model Loading Failed: {e}")
    exit()

# 🎛️ Image Size (Adjust if needed)
IMG_SIZE = (224, 224)

# 🎛️ Serial Communication with Arduino
SERIAL_PORT = "/dev/cu.usbmodem14201"  # Adjust based on your system
BAUD_RATE = 9600

try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)  # Increased timeout for stability
    time.sleep(2)  # Allow time for Arduino to initialize
    print(f"✅ Connected to Arduino on {SERIAL_PORT}")
except Exception as e:
    print(f"⚠️ Could not open serial port: {e}")
    arduino = None

def classify_frame(frame):
    """Preprocess frame & classify using the model."""
    try:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        resized_frame = cv2.resize(frame_rgb, IMG_SIZE)
        normalized_frame = resized_frame / 255.0  # Normalize (0 to 1)
        input_tensor = np.expand_dims(normalized_frame, axis=0)  # Reshape to (1, 224, 224, 3)

        predictions = model.predict(input_tensor)
        class_index = np.argmax(predictions)  # Get the predicted class index
        return class_index
    except Exception as e:
        print(f"⚠️ Classification Error: {e}")
        return None

# 📷 Start Webcam Capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("⚠️ Camera Error: Unable to access the webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Camera Error: Could not capture frame")
        break

    # Flip frame horizontally (optional, for correct orientation)
    frame = cv2.flip(frame, 1)

    # Classify Frame
    class_index = classify_frame(frame)
    if class_index is not None:
        print(f"🔍 Predicted Class: {class_index}")

        # Send class index to Arduino
        if arduino:
            command = f"{class_index}\n"  # Convert to string format
            arduino.write(command.encode("utf-8"))  # Send data
            arduino.flush()  # Clear buffer to prevent overflow
            
            # ✅ Wait for Arduino to confirm receipt
            response = arduino.readline().decode("utf-8").strip()
            if response:
                print(f"✅ Arduino Response: {response}")

            time.sleep(0.3)  # Small delay to prevent overflow

    # Show Webcam Feed
    cv2.imshow("Webcam - Gesture Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
    print("✅ Serial Connection Closed")
