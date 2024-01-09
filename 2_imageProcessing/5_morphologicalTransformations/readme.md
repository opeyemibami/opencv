# Title: Smoothing Images / 2D Convolution (Image Filtering)

# Knowledge

- ## Brief explanation
  Morphological transformations are some simple operations based on the image shape

  It is normally performed on binary images
   
- ## Psuedocode / Major Steps

  Blur image: Image blurring is achieved by convolving the image with a low-pass filter kernel

  - import libraries
  - define image path
  - read image
  - set kernel size
  - do morphological transformations
  - visualize image
  - set waitkey

- ## Use cases and scenario
  - It is also useful in joining broken parts of an object.
  - Normally, in cases like noise removal, erosion is followed by dilation because, erosion removes white noises, but it also shrinks the object
  
- ## Techniques
  - Erosion: it erodes away the boundaries or size of foreground object
      The kernel slides through the image (as in 2D convolution). 
      A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
  - Dilation: it thickens the boundaries of foreground object
      A pixel element is '1' if at least one pixel under the kernel is '1'
  - Opening: Opening is just another name of erosion followed by dilation
      It is useful in joining broken parts of an object.
  - Closing: reverse of Opening i.e. Dilation followed by Erosion
      It is useful in closing small holes inside the foreground objects, or small black points on the object.
  - Morphological Gradient: It is the difference between dilation and erosion of an image
  - Top Hat: It is the difference between input image and Opening of the image.
  - Black Hat: It is the difference between the closing of the input image and input image.
- ## Alternatives Techniques
  - Bilateral Filtering: highly effective in noise removal while keeping edges sharp
      Bilateral filtering uses a Gaussian filter in space and Gaussian filter of intensity which is a function of pixel difference.
      So it preserves the edges since pixels at edges will have large intensity variation.
