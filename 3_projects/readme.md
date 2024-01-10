# Title: Applications of basic image processing 

# 1) Object Tracking using colorSpace convertion
- ## Brief explanation
   Tracking objects based on color is one of the quickest and easiest methods for tracking an object from one image frame to the next. 
   
   The speed of this technique makes it very attractive for near-realtime applications but due to its simplicity many issues exist that can cause the tracking to fail.
- ## Psuedocode / Major Steps
  - Take each frame from the video 
  - Convert frame from BGR to HSV colorspace
  - Convert color of interest frame from BGR to HSV colorspace
  - Create a lower and upper limits of the color of interest for detection e.g green color
  - Create a mask HSV frame using the lower and upper limits as the thresholds 
  - Convert the mask into PIL Image format 
  - Get the bounding box 
  - Draw bounding box on the frame
- ## Todo
  - Imporove on the object tracker

# 2) Handwritten Note Processing
- ## Brief explanation
   Using the Adaptive thresholding works fine on the input image. 
   
   Act of trying morphological transformations combinations is intuitive too.n This produce closely related result to using adaptive threshold
- ## Psuedocode / Major Steps
  - Read image in grayscale
  - invert the image to have white foreground if needed
  - Try different morphological transformations
  - observe the best single transformation \
  - Apply Otsu thresholding 
  - Visualize result
  - Set waitkey

- ## Todo
  - Try morphological transformations combo sequentially