# DIP Lab 

A Python (algorithms) + Streamlit (UI/ UX) web app implementing Digital Image Processing from scratch using Numpy. 

## Overview

This project implements core DIP algorithms (spatial filtering, edge detection, restoration , segmentation) without relying on high-level CV libraries for actual processing - OpenCV are used only for image I/O.

## Features 

- [ ] Spatial domain operations 
- [ ] Edge detection
- [ ] Image restoration
- [ ] Image segmentation 
- [ ] Interactive Streamlit UI


## Usage 

\`\`\`bash  
streamlit run app.py  
\`\`\`

##  Project Structure
DIP-LAB/
├── algorithms/           # Core image processing logic
│   ├── __init__.py
│   ├── edge_detection.py
│   ├── segmentation.py
│   └── spatial.py
├── examples/             # Usage examples and demonstrations
├── tests/                # Test suites
│   └── __init__.py
├── utils/                # Helper functions and utilities
├── venv/                 # Virtual environment
├── .gitignore            # Git ignore file
├── app.py                # Main application entry point
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
└── test1.py              # Test script

## LICENSE
