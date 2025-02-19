# Plant ML
Plant ML is an experiment exploring how machine learning and computer vision can be used to interact with natural elements. This project was developed within a two-day hackathon for the **bio techno art exhibition**. Raed more about the project [here](https://adeolao.carrd.co/#project-plantml-biotechno). 



| <img src="images/final-project-1.gif" alt="A motorised plant scuplture controlled by hand gestures" width="300"/>  | | <img src="images/Instagram post - 3.png" alt="Poster of the bio techno art exhbition" width="400"/> |
| :---: | --------- | :---: |
| The final project | | The bio techno art exhibition poster |

This project uses Python to call a tensorflow model to recoginse hand gestures (trained through Google's Teachable Machine) and send those outputs to Arduino to control a motor. 

![Diagram of how it works](images/plant_ml_diag.png)

## Setup 

**What you need**:
- Python 3.8
- [Arduino IDE](https://www.arduino.cc/en/software) 
- Arduino board (UNO R3 is used in this project)
- Trained tensorflow image recignition model ([Google's Teachable Machine](https://teachablemachine.withgoogle.com/) is used to train)
- A 3V-6V DC motor
- A dual 16-pin motor driver IC (The L293D is used in this project)
- Power supply (set at 5V)

### Code installation & setup

**Install the requirements**: 

`pip install tensorflow tensorflowjs numpy opencv-python pyserial`

To train your own model, created a new project on [Teachable Machine](https://teachablemachine.withgoogle.com/train):

- Select the type *Image Model*.
- Capture pictures of your hand open (Class 0), hand closed (Class 1) and of a background/doing nothing (Class 2)
- Select "Train model" and export a Tensorflow model 
- Add the exported Tensorflow model (`keras_model.h5`) to the `plant_ml_model/` folder.

If you want to play around with the model (i.e. add more or different classes), remember to adjust `plant_ml.py` and `plant_ml.ino` and to match the classes and number of classes. 

### Arduino setup

To set up the Arduino UNO, please follow the following diagram to correctly set up the motor: 
![Simulation snapshot of a 3 to 6 volts DC motor connected to an Arduino UNO R3 baord and 5V power supply](images/plant-ml_arduino_set_up.png?raw=true)

Upload the `plant_ml.ino` code to the Arduino board.

## Run the code

To run the project, run the following:

`python plant_ml.py`

Enjoy! 
