import numpy
import cv2
import improc

def prnt_img (image_name):
 image_in_all_the_people=cv2.imread(image_name,0)
 dim=numpy.shape(image_in_all_the_people)
 image_is_all_the_people=improc.istogram_eq(image_in_all_the_people)
 image_is_hex=improc.quality(image_is_all_the_people)
 image_in_hex=improc.quality(image_in_all_the_people)
 #print(image_is_hex)
 #print(image_in_hex)
 middle_noise=numpy.random.rand(dim[0],dim[1])
 #matrices
 ml0=numpy.zeros(dim)+(image_in_hex==0)
 ml64=numpy.zeros(dim)+(image_in_hex==64)
 ml128=numpy.zeros(dim)+(image_in_hex==128)
 ml192=numpy.zeros(dim)+(image_in_hex==192)


 ml0_is=numpy.zeros(dim)+(image_is_hex==0)
 ml64_is=numpy.zeros(dim)+(image_is_hex==64)
 ml128_is=numpy.zeros(dim)+(image_is_hex==128)
 ml192_is=numpy.zeros(dim)+(image_is_hex==192)

 
 f_im64=numpy.multiply(numpy.array(ml64),numpy.array((middle_noise>0.2)))

 f_im128=numpy.multiply(numpy.array(ml128),numpy.array((middle_noise>0.2)))
 f_im128_i=numpy.multiply(numpy.array(ml128),numpy.array(((middle_noise<=0.2))))
 f_im192=numpy.multiply(numpy.array(ml192),numpy.array((middle_noise>0)))




 f_im64_is=numpy.multiply(numpy.array(ml64_is),numpy.array((middle_noise>0.2)))

 f_im128_is=numpy.multiply(numpy.array(ml128_is),numpy.array(((middle_noise>0.2))))

 f_im128_i_is=numpy.multiply(numpy.array(ml128_is),numpy.array(((middle_noise<=0.2))))

 f_im192_is=numpy.multiply(numpy.array(ml192_is),numpy.array((middle_noise>0)))


 im_out=numpy.zeros(dim)+(f_im64)*64+(f_im128_i)*128+(f_im128+f_im192)*255
 im_out_is=numpy.zeros(dim)+(f_im64_is)*64+(f_im128_i_is)*128+(f_im128_is+f_im192_is)*255

 if image_name[(len(image_name)-4)]==".":
  imn=image_name[0:(len(image_name)-4)]
 else:
  imn=image_name[0:(len(image_name)-5)]

 im1_name=imn+"print.jpg"
 im2_name=imn+"print_ist.jpg"

 cv2.imwrite(im1_name,im_out)
 cv2.imwrite(im2_name,im_out_is)



