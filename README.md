# Plant ML
Plant ML is an experiment exploring how machine learning and computer vision can be used to interact with natural elements. This project was developed within a two-day hackathon for the **bio techno art exhibition**. Raed more about the project [here](https://adeolao.carrd.co/#project-plantml-biotechno). 

<img src="images/final-project-1.gif" alt="A motorised plant scuplture controlled by hand gestures" width="300"/>

<img src="images/Instagram post - 3.png" alt="Poster of the bio techno art exhbition" width="300"/>

This project uses Python to call a tensorflow model to recoginse hand gestures (trained through Google's Teachable Machine) and send those outputs to Arduino to control a motor. 

![Diagram of how it works](images/plant_ml_diagram.png)

## Setup 

**What you need**:
- Python 3.8
- [Arduino IDE](https://www.arduino.cc/en/software) 
- Arduino board (UNO R3 is used in this project)
- Trained tensorflow image recignition model ([Google's Teachable Machine](https://teachablemachine.withgoogle.com/) is used to train)

### Code installation

**Install the requirements**: 

`pip install tensorflow tensorflowjs numpy opencv-python pyserial`

### Arduino setup

![Simulation snapshot of a 3 to 6 volts DC motor connected to an Arduino UNO R3 baord and 5V power supply](images/plant-ml_arduino_set_up.png?raw=true)

Upload the `plant_ml.ino` code to the Arduino board.

## Run the code

To run the project, run the following:

`python plant_ml.py`