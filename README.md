# OpenCV Image & Video Filters

A Python project demonstrating various image and video processing techniques using OpenCV.

## Features

- Video capture and processing
- Image manipulation and filtering
- Real-time image effects including:
  - Grayscale conversion
  - Gaussian blur
  - Canny edge detection
  - Image dilation
- Image resizing and cropping
- Drawing shapes and text on images
- Multi-image display functionality

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/opencv-image-videos-filters.git
cd opencv-image-videos-filters
```

2. Install the required packages:
```bash
pip install opencv-python numpy
```

## Project Structure

```
.
├── main.py         # Main application file
├── res/            # Resources directory
│   ├── test.mp4    # Sample video file
│   └── img.png     # Sample image file
├── README.md
└── .gitignore
```

## Usage

The project contains several functions for different image processing operations:

1. Video Processing:
```python
python main.py
```
This will start the video processing demo. Press 'q' to exit.

2. Image Processing:
To switch to image processing mode, uncomment the `open_img()` line and comment out `open_video()` in main.py.

## Functions

- `open_video()`: Process video input with real-time filters
- `open_img()`: Apply various filters to static images
- `crop_img()`: Demonstrate image cropping and resizing
- `create_img()`: Create custom images with shapes and text
- `stack_image()`: Utility function to display multiple images

## Controls

- Press 'q' to exit video processing mode
- Press any key to close image windows in image processing mode


