import numpy
import scipy
import cv2

def greenscreen(image_in_all_the_people, background):
 d_im=numpy.shape(image_in_all_the_people);
 d_bg=numpy.shape(background);
 if(d_im==d_bg):
  a=numpy.zeros(d_im);
  a[:,:,0]=(image_in_all_the_people[:,:,0]<50)&(image_in_all_the_people[:,:,1]>240)&(image_in_all_the_people[:,:,2]<50);
  a[:,:,1]=(image_in_all_the_people[:,:,0]<50)&(image_in_all_the_people[:,:,1]>240)&(image_in_all_the_people[:,:,2]<50);
  a[:,:,2]=(image_in_all_the_people[:,:,0]<50)&(image_in_all_the_people[:,:,1]>240)&(image_in_all_the_people[:,:,2]<50);

  c=numpy.zeros(d_im);
  c[:,:,0]=(image_in_all_the_people[:,:,0]>=50)|(image_in_all_the_people[:,:,1]<=240)|(image_in_all_the_people[:,:,2]>=50);
  c[:,:,1]=(image_in_all_the_people[:,:,0]>=50)|(image_in_all_the_people[:,:,1]<=240)|(image_in_all_the_people[:,:,2]>=50);
  c[:,:,2]=(image_in_all_the_people[:,:,0]>=50)|(image_in_all_the_people[:,:,1]<=240)|(image_in_all_the_people[:,:,2]>=50);
  f=numpy.multiply(c,image_in_all_the_people);
  f[:,:,1]=f[:,:,1]-numpy.multiply((f[:,:,1]>100)&(f[:,:,2]<50)&(f[:,:,0]<50),f[:,:,1]*250);
  b=numpy.zeros(d_im)+numpy.multiply(a,background)+f;
  
 else:
  b=image_in_all_the_people;
 return b;
