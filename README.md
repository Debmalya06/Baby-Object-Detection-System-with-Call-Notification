# Baby Object Detection System

## Overview
The **Baby Object Detection System** is a real-time monitoring application that detects if a baby's face is obstructed or if an object is present near the baby. The system uses **OpenCV** for face detection and **Twilio** for alert notifications. The frontend is built with **Streamlit**, allowing users to start and stop detection with a simple UI.

## Features
- **Real-time Face Detection** using OpenCV.
- **Alerts via Twilio Calls** when a face is obstructed for more than 5 seconds.
- **Start/Stop Button Control** through Streamlit.
- **Supports Laptop/Webcam and IP Camera**.

## Project Structure
```
Baby Object Detect/
│── app.py              # Streamlit frontend
│── detection.py        # Face detection logic
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
```

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/baby-object-detect.git
   cd baby-object-detect
   ```

2. **Create and Activate Virtual Environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application
1. **Start the Streamlit App**
   ```sh
   streamlit run app.py
   ```
2. **Use the Web Interface** to start/stop detection.

## Dependencies
The project requires the following Python libraries:
- `opencv-python`
- `streamlit`
- `twilio`
- `numpy`

Install them using:
```sh
pip install -r requirements.txt
```

## Configuration
- Update **Twilio Credentials** (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, `YOUR_PHONE_NUMBER`) in `detection.py`.
- To use an **IP Camera**, update the `ip_camera_url` variable in `detection.py`.

## How It Works
1. **Click the "Start Detection" button** to start monitoring.
2. **If a face is detected**, a green rectangle is drawn.
3. **If the face is covered for more than 5 seconds**, a Twilio call alert is triggered.
4. **Click the "Stop Detection" button** to stop monitoring.

## Contribution
Feel free to contribute! Fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

---
👶 **Baby Object Detection System - Keeping Your Little One Safe!** 🚀
## Here is the sample page image
![image](https://github.com/user-attachments/assets/1cdbd16b-d155-4dde-8713-4ef6c750f722)


