# Title: Applications of basic image processing 

# 1) Object Tracking using colorSpace convertion
- ## Brief explanation
   Tracking objects based on color is one of the quickest and easiest methods for tracking an object from one image frame to the next. 
   
   The speed of this technique makes it very attractive for near-realtime applications but due to its simplicity many issues exist that can cause the tracking to fail.
- ## Psuedocode / Major Steps
  - Take each frame from the video 
  - Convert from BGR to HSV colorspace
  - Threshold the HSV image for a range of color of interest for detection e.g green color
  - Extract the object color alone
  - Perform desired ops on the extract
