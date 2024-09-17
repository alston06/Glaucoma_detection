# Wearable Glaucoma Detection Device

## Project Overview
This project aims to develop a wearable and portable tonometer designed to measure Intraocular Pressure (IOP) non-invasively. The device, which resembles a VR headset, rests comfortably on the eyes and provides an accurate and stable way to detect glaucoma, without the need for external headrests or skilled medical professionals. By incorporating innovative technologies such as eye state detection and iris tracking, this project addresses challenges related to IOP measurement and glaucoma progression.

## Problem We Are Solving
Traditional tonometers require skilled technicians and external head/chinrests to maintain accurate eye positioning, limiting portability and accessibility. Additionally, corneal thickness variation affects the accuracy of IOP readings.
### Key Challenges:
Ensuring correct device-eye distance for accurate IOP measurement.
Addressing variations in corneal thickness that lead to inaccurate measurements.
### Proposed Solutions:
We aim to enhance the tonometer by incorporating ultrasound technology for improved accuracy in corneal thickening measurement. This ensures proper probe positioning, reduces reading variability, and offers a non-invasive method for assessing both IOP and corneal structure.

## Code Components:

### 1. Eye State Detection (Open/Closed)
This component detects whether the patient's eyes are open or closed using dlib and OpenCV. The Eye Aspect Ratio (EAR) is used to determine the eye state, which is vital for ensuring the device is correctly positioned on the eye.
#### Key Features:
Detects eye openness/closedness to trigger measurements.
Uses facial landmarks to locate and track eyes.
Updates are only when the eye state changes, ensuring a real-time response.

### 2. Iris Detection & Tracking
The second component focuses on detecting the position of the iris within the eye. OpenCV’s Hough Circle Transform identifies the center and radius of the iris. This helps to ensure accurate eye positioning during the IOP measurement process.
#### Key Features:
Detects iris location using Hough Circle Transform.
Tracks and outputs iris center coordinates, ensuring the device remains centered on the eye during the measurement process.

### 3. Switching Between Eye Cameras
This feature enables switching between the left and right eye cameras, providing flexibility for bilateral analysis.

## How the System Works:
Eye Detection: The system continuously monitors the patient's eye state to confirm when the eyes are open. The system can proceed with IOP measurements once the eyes are detected as open.
Iris Detection: The position of the iris is identified to ensure the device is aligned correctly for accurate measurement.
Switchable Cameras: The system alternates between left and right eye inputs for comprehensive analysis.

## Benefits of the Device
Non-Invasive & Portable: The device provides a comfortable, non-contact method to measure IOP, allowing for self-monitoring without the need for specialized equipment.
Early Detection: Enables early detection and continuous monitoring of glaucoma progression through real-time IOP readings.
Rural Accessibility: Improves accessibility for patients in remote locations, reducing the need for hospital visits.
Cost-Efficiency: Reduces the overall cost of glaucoma management by enabling at-home monitoring, and reducing reliance on expensive hospital-based tests.

## Future Work
Ultrasound Integration: Adding ultrasound technology to further improve accuracy by providing direct corneal thickness measurements.
Data Sharing & Analysis: Enabling remote sharing of IOP readings with healthcare providers for ongoing monitoring.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors
Alston
Janis
