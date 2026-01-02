# Virtual Hand Mouse

Control your computer mouse using hand gestures through a webcam.  
This project uses OpenCV, MediaPipe, and PyAutoGUI to track your index finger and convert its movement into mouse movement, and to perform a mouse click when the thumb and index finger pinch together.

---

## ✨ Features

- Real-time hand tracking using **MediaPipe Hands**.
- Move the mouse cursor using the **index fingertip**.
- Perform a **left click** by pinching the **thumb** and **index finger** together.
- A purple rectangle defines the **control region**, so you do not need to move your hand to the very edges of the camera frame.
- Basic smoothing to reduce cursor shaking.

---

## 🧰 Technologies

- **Python**
- **OpenCV** – capture video from the webcam and draw on frames.
- **MediaPipe Hands** – detect and track 21 hand landmarks.
- **PyAutoGUI** – control the system mouse (move and click).
- **math** – compute distance between landmarks for gesture detection.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/phongilm20/Virtual-Hand-Mouse.git
cd Virtual-Hand-Mouse
2. (Optional) Create a virtual environment
bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Linux / macOS
3. Install dependencies
bash
pip install opencv-python mediapipe pyautogui
If you add a requirements.txt later, you can change this to:

bash
pip install -r requirements.txt
🚀 How to Run
Assuming your main file is called virtual_mouse.py:

bash
python virtual_mouse.py
If your script has a different name, replace it accordingly.

🎮 Usage
Make sure your webcam is connected and not used by other applications.

Run the script. A window named "Virtual Mouse" will open, showing your webcam feed.

You will see a purple rectangle inside the frame:

This is the active control area.

Move your index finger inside this rectangle to move the mouse cursor across the entire screen.

Left click gesture:

Bring the thumb tip and index finger tip close together (pinch).

When the distance between them is below a threshold, a left click is triggered.

Press q to quit the application and close the window.

🎥 Demo
When you have a demo video, you can add it here.

Example for a YouTube link:

text
### Demo Video

[▶ Watch the demo video](https://www.youtube.com/your-demo-link-here)
Example for a screenshot or GIF:

text
### Screenshots


(Remember to place demo.png inside an images/ folder.)

⚙️ How It Works (Overview)
MediaPipe Hands returns 21 landmarks for each detected hand.

This project primarily uses:

Landmark 8 – index fingertip → mapped to screen coordinates to move the mouse cursor.

Landmark 4 – thumb tip → used with landmark 8 to detect a pinch (click gesture).

The index finger coordinates within the purple rectangle are:

Shifted by frame_reduction to ignore the margins.

Normalized to a range of 0–1 inside that rectangle.

Scaled up to the full screen width and height.

A smoothing factor is applied so the cursor does not jitter too much when the hand moves slightly.

🧪 Possible Improvements
Add extra gestures:

Right click (for example, using index + middle finger pinch).

Double click gesture.

Scroll by moving the hand up/down while holding a specific gesture.

Add configuration options for:

frame_reduction (control area size).

smoothening (smoothing strength).

Click distance threshold.

Display FPS and debugging information on the video feed.

👤 Author
Name: Your Name Here

GitHub: @phongilm20