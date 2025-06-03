# Hands-Free Keyboard

**Hands-Free Keyboard** is a simple webcam-based virtual keyboard that enables typing using simulated eye movement — no hands or physical input needed. This project demonstrates how computer vision can create alternative, accessible input methods.


## Features

- Simulated eye-gaze control by monitoring webcam brightness  
- On-screen 3-row virtual keyboard with all English alphabets  
- Auto-selection of keys after stable "gaze" for 2 seconds  
- Includes **Space** and **Backspace** keys for more natural typing  
- Real-time visual feedback highlighting the selected key  
- Requires only Python with OpenCV and NumPy (no extra installations)



## How It Works

The application captures video from your webcam and analyzes brightness in a specific region to simulate eye gaze direction. Based on this simulated gaze, the current selected key on the virtual keyboard changes. Holding the gaze steady on a key for a few seconds automatically types that key.

> **Note:** This project uses a simple simulation for eye control and does not perform actual eye tracking. It’s intended as a prototype or educational tool.



## Requirements

- Python 3.x  
- OpenCV (`opencv-python`)  
- NumPy

## Install dependencies with:

pip install opencv-python numpy

