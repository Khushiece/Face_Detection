<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Detection using Haar Cascade Algorithm</title>
</head>
<body>
    <h1>Introduction</h1>
    <p>This project demonstrates a simple implementation of face detection using the Haar Cascade frontal face algorithm provided by OpenCV. The Haar Cascade method is a popular technique for detecting objects in images and has been extensively used for face detection.</p>

    <h1>Prerequisites</h1>
    <ul>
        <li>Python (>=3.0)</li>
        <li>OpenCV (>=3.4.2)</li>
    </ul>

    <h1>Installation</h1>
    <ol>
        <li>Install Python from <a href="https://www.python.org/">python.org</a>.</li>
        <li>Install OpenCV library using pip:</li>
    </ol>
    <code>pip install opencv-python</code>

    <h1>Usage</h1>
    <ol>
        <li>Clone this repository to your local machine.</li>
        <li>Download the haarcascade_frontalface_default.xml file from the OpenCV GitHub repository or use the provided path to the XML file in the code.</li>
        <li>Run the Python script face_detection.py.</li>
    </ol>

    <h1>Code Overview</h1>
    <p><strong>face_detection.py:</strong> This Python script performs face detection using the Haar Cascade algorithm. It captures video from the default camera, detects faces in real-time, and draws rectangles around the detected faces.</p>

    <h1>Instructions</h1>
    <ol>
        <li>Run the script face_detection.py.</li>
        <li>Ensure that your camera is properly connected and accessible.</li>
        <li>The application will display the live video feed with detected faces outlined by green rectangles.</li>
        <li>Press 'q' to exit the application.</li>
    </ol>

    <h1>Notes</h1>
    <ul>
        <li>The accuracy of face detection may vary based on factors such as lighting conditions, face angles, and camera quality.</li>
        <li>Adjust the parameters of the detectMultiScale function (such as scaleFactor and minNeighbors) for optimal performance according to your requirements.</li>
    </ul>

    <h1>References</h1>
    <ul>
        <li>OpenCV Documentation: <a href="https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html">Cascade Classifier</a></li>
        <li>OpenCV GitHub Repository: <a href="https://github.com/opencv/opencv/tree/master/data/haarcascades">haarcascades</a></li>
    </ul>
</body>
</html>
