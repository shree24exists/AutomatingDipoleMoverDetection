# Automated Zooniverse Flipbook Processing

This is a small personal project where I downloaded and processed 4-frame WISE flipbooks from the Backyard Worlds: Planet 9 project on Zooniverse.
The goal is to learn basic astronomy data handling, organize image sequences, and create GIFs for later use in simple detection / ML experiments.

This project is purely educational and not commercial.

## What the Project Does
- Takes raw JPEG images (downloaded manually)
- Organizes them into folders of 4 images each (one “book”)
- Renames them consistently as frame0 → frame3
- Converts each 4-frame book into a GIF for easy viewing

## Folder Structure
Images        raw images (1.jpeg, 2.jpeg, ...)
books         auto-organized sets of 4 frames
gifs          GIF flipbooks
organize.py    # groups raw images into book folders
gif_maker.py   # converts 4 frames into one GIF

## Scripts
### organize.py
- Reads and sorts all JPEGs
- Groups them in sets of 4
- Creates folders like book_001, book_002, ...
- Saves frames as frame0.jpeg → frame3.jpeg

### gif_maker.py
- Opens each book folder
- Loads the 4 frames using Pillow
- Creates an animated GIF
- Saves it in the gifs/ folder

## Note on Coding
Most of the scripting help, debugging, and environment setup was done with assistance from ChatGPT, while the dataset preparation, idea, workflow, and manual downloading were done by me.

## Status
- 128 images processed
- 32 GIFs generated
- Dataset ready for future work (detection/ML)
