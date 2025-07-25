# 3d-to-2d-projection

Learning camera geometry and depth through projection math and NumPy

This project focuses on learning and implementing depth estimation from 2D images using computer vision and machine learning. It is split into three phases to gradually build up understanding and capabilities.

Each phase contains its own src and data folders. Code is written in standalone Python files with inline comments.

Goals:

- Learn the basics of depth estimation and projection
- Understand how pretrained models are loaded and used
- Build toward more customized or task-specific algorithms

Tech stack:

- Python
- PyTorch
- OpenCV
- timm (for loading model backbones)

To run a file, use the command:

python phase1/src/infer_depth.py

To install dependencies:

pip install torch torchvision opencv-python timm

License: MIT
