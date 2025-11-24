📘 Face & Eye Detection Using OpenCV

A simple Computer Vision project that performs real-time face and eye detection using a webcam. This project uses OpenCV's built-in **Haar Cascade Classifiers** to detect human faces and eyes in live video streams. It is lightweight, easy to understand, and suitable for beginners.

---

📌 **Project Overview**

Face and eye detection is one of the fundamental applications in Computer Vision. In this project, a webcam feed is captured and frames are processed in real-time to identify:

* Human faces
* Eyes inside each face
* Number of faces currently detected

This project demonstrates how OpenCV can be used to perform image processing, object detection, and real-time video analysis.

---

🎯 **Objectives**

* Capture live video using a webcam
* Detect faces using Haar Cascade classifier
* Detect eyes within the detected face region
* Display bounding boxes around detected objects
* Show the number of faces in the frame
* Allow screenshot capturing
* Provide a simple, clear implementation of CV concepts

---

🧩 **Features**

✔ Real-time face detection
✔ Eye detection inside each face
✔ Face count displayed on the screen
✔ Press **‘s’** to save a screenshot
✔ Press **‘q’** to quit
✔ Lightweight and beginner-friendly

---

📂 **Project Structure**

```
cv-face-eye-detection/
│
├── src/
│   └── face_eye_detection.py
│
├── screenshots/
│   └── (saved screenshots go here)
│
├── recordings/
│   └── (optional screen recordings)
│
└── README.md
```

---

🛠️ **Technologies Used**

* **Python 3**
* **OpenCV (cv2)**
* Haar Cascade XML files (bundled within OpenCV)

---

📦 **Installation Instructions**

### 1. Install Python dependencies

```bash
pip install opencv-python
```

### 2. Run the project

```bash
python src/face_eye_detection.py
```

Make sure your webcam is connected.

---

▶️ **How It Works**

1. Access webcam using `cv2.VideoCapture()`
2. Convert each frame to grayscale
3. Use Haar Cascade models to detect:

   * Faces
   * Eyes inside face regions
4. Draw rectangles on detected regions
5. Display updated live feed continuously
6. Wait for keyboard commands:

   * **'q'** → Quit
   * **'s'** → Save screenshot

---

🧠 **Algorithm (Simplified)**

```
START
Open webcam
Load Haar Cascade models
Loop:
    Read frame
    Convert frame to grayscale
    Detect faces in the frame
    For each face:
        Detect eyes
        Draw rectangles
    Display face count
    Show frame
    If 's' pressed → Save screenshot
    If 'q' pressed → Exit loop
Release camera
Close windows
END
```

---


🧪 **Testing & Output**

Test the program by:

* Moving your face in front of the camera
* Checking if rectangle boxes appear
* Pressing **‘s’** to capture screenshots
* Adding the screenshots to your GitHub repo

---

📝 **Future Enhancements (Optional)**

You can extend this project by adding:

* Smile detection
* Face recognition
* Object tracking
* Mask detection
* Emotion detection
* Save detection results to a file

---

👨‍💻 **Author**

Debashish Biswas 
22MIM10017

---

