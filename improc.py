import numpy as numpy
import numpy.random
import scipy as scipy

import cv2 as cv2

def duality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people-(numpy.ones(dim)*128);
 b=(b>1)*255;
 return b;

def dualityr(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people-(numpy.ones(dim)*128);
 b=(b>1)*255;
 c=b[:,:,0];
 b[:,:,0]=b[:,:,1];
 b[:,:,1]=c;
 return b;

def dualityav(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people-(numpy.ones(dim)*numpy.median(image_in_all_the_people));
 b=(b>1)*numpy.median(image_in_all_the_people)*2;
 return b;

def dualityrav(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people-(numpy.ones(dim)*numpy.median(image_in_all_the_people));
 b=(b>1)*numpy.median(image_in_all_the_people)*2;
 b=(b>1)*255;
 c=b[:,:,0];
 b[:,:,0]=b[:,:,1];
 b[:,:,1]=c;
 return b;

def duality_up(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>106)*255 );

 return b;

def duality_down(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>149)*255 );

 return b;

def triad(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>85) & (image_in_all_the_people<170))*127+(image_in_all_the_people>=170)*255;

 return b;

def triadav(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 a=numpy.median(image_in_all_the_people)/2;
 c=a=(numpy.median(image_in_all_the_people))+(numpy.median(image_in_all_the_people)/2);
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>a) & (image_in_all_the_people<c))*85+(image_in_all_the_people>=c)*170;

 return b;




def triadbl(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>92) & (image_in_all_the_people<213))*128+(image_in_all_the_people>=213)*213;

 return b;

def triadb(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>128) & (image_in_all_the_people<213))*128+(image_in_all_the_people>=213)*213;

 return b;

def quality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>64) & (image_in_all_the_people<128))*64+ ((image_in_all_the_people>=128) & (image_in_all_the_people<192))*128+(image_in_all_the_people>=192)*192;

 return b;

def qualityb(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>128) & (image_in_all_the_people<160))*128+ ((image_in_all_the_people>=160) & (image_in_all_the_people<192))*160+(image_in_all_the_people>=192)*192;

 return b;

def qualitybl(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>96) & (image_in_all_the_people<160))*128+ ((image_in_all_the_people>=160) & (image_in_all_the_people<192))*160+(image_in_all_the_people>=192)*192;

 return b;

def pentality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>51) & (image_in_all_the_people<102))*51+ ((image_in_all_the_people>=102) & (image_in_all_the_people<153))*102+ ((image_in_all_the_people>=153) & (image_in_all_the_people<204))*153+ +(image_in_all_the_people>=204)*204;

 return b;

def hexality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>43) & (image_in_all_the_people<86))*43+ ((image_in_all_the_people>=86) & (image_in_all_the_people<128))*86+ ((image_in_all_the_people>=128) & (image_in_all_the_people<170))*128+ ((image_in_all_the_people>=170) & (image_in_all_the_people<213))*170+(image_in_all_the_people>=213)*213;

 return b;

def heptality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>32) & (image_in_all_the_people<64))*32+ ((image_in_all_the_people>=62) & (image_in_all_the_people<96))*64+((image_in_all_the_people>=96) & (image_in_all_the_people<128))*96+((image_in_all_the_people>=128) & (image_in_all_the_people<160))*128+((image_in_all_the_people>=160) & (image_in_all_the_people<192))*160+(image_in_all_the_people>=192)*192;

 return b;
def octality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>32) & (image_in_all_the_people<64))*32+ ((image_in_all_the_people>=62) & (image_in_all_the_people<96))*64+((image_in_all_the_people>=96) & (image_in_all_the_people<128))*96+((image_in_all_the_people>=128) & (image_in_all_the_people<160))*128+((image_in_all_the_people>=160) & (image_in_all_the_people<192))*160+((image_in_all_the_people>=192) & (image_in_all_the_people<224))*192+(image_in_all_the_people>=224)*224;

 return b;


def octalityav(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>32) & (image_in_all_the_people<64))*32+ ((image_in_all_the_people>=62) & (image_in_all_the_people<96))*64+((image_in_all_the_people>=96) & (image_in_all_the_people<128))*96+((image_in_all_the_people>=128) & (image_in_all_the_people<160))*128+((image_in_all_the_people>=160) & (image_in_all_the_people<192))*160+((image_in_all_the_people>=192) & (image_in_all_the_people<224))*192+(image_in_all_the_people>=224)*224;

 return b;


def octalityb(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>128) & (image_in_all_the_people<144))*128+ ((image_in_all_the_people>=144) & (image_in_all_the_people<160))*144+((image_in_all_the_people>=160) & (image_in_all_the_people<176))*160+((image_in_all_the_people>=176) & (image_in_all_the_people<192))*176+((image_in_all_the_people>=192) & (image_in_all_the_people<208))*192+((image_in_all_the_people>=208) & (image_in_all_the_people<224))*208+((image_in_all_the_people>=224) & (image_in_all_the_people<240))*224+(image_in_all_the_people>=240)*240;

 return b;


def octalityb2(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>64) & (image_in_all_the_people<128))*64+((image_in_all_the_people>=128) & (image_in_all_the_people<144))*128+ ((image_in_all_the_people>=144) & (image_in_all_the_people<160))*144+((image_in_all_the_people>=160) & (image_in_all_the_people<176))*160+((image_in_all_the_people>=176) & (image_in_all_the_people<192))*176+((image_in_all_the_people>=192) & (image_in_all_the_people<208))*192+((image_in_all_the_people>=208) & (image_in_all_the_people<224))*208+((image_in_all_the_people>=224) & (image_in_all_the_people<240))*224+(image_in_all_the_people>=240)*240;

 return b;

def octalityb3(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>64) & (image_in_all_the_people<128))*32+((image_in_all_the_people>=128) & (image_in_all_the_people<160))*92+((image_in_all_the_people>=160) & (image_in_all_the_people<176))*160+((image_in_all_the_people>=176) & (image_in_all_the_people<192))*176+((image_in_all_the_people>=192) & (image_in_all_the_people<208))*192+((image_in_all_the_people>=208) & (image_in_all_the_people<224))*208+((image_in_all_the_people>=224) & (image_in_all_the_people<240))*224+(image_in_all_the_people>=240)*240;

 return b;



def hexadecimality(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>16)&(image_in_all_the_people<32))*16+ ((image_in_all_the_people>=32)& (image_in_all_the_people<48))*32+ ((image_in_all_the_people>=48) & (image_in_all_the_people<64))*48+((image_in_all_the_people>=64) & (image_in_all_the_people<80))*64+((image_in_all_the_people>=80) & (image_in_all_the_people<96))*80 +((image_in_all_the_people>=96) & (image_in_all_the_people<112))*96+((image_in_all_the_people>=112) & (image_in_all_the_people<128))*112+((image_in_all_the_people>=128) & (image_in_all_the_people<144))*128+((image_in_all_the_people>=144) & (image_in_all_the_people<160))*144+((image_in_all_the_people>=160) & (image_in_all_the_people<176))*160+((image_in_all_the_people>=176) & (image_in_all_the_people<192))*176+((image_in_all_the_people>=192) & (image_in_all_the_people<208))*192+((image_in_all_the_people>=208) & (image_in_all_the_people<224))*208+((image_in_all_the_people>=224) & (image_in_all_the_people<240))*224+(image_in_all_the_people>=240)*240;
 return b;

def hexadecimalityms(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>16)&(image_in_all_the_people<64))*2+ ((image_in_all_the_people>=64)& (image_in_all_the_people<96))*4+ ((image_in_all_the_people>=96) & (image_in_all_the_people<128))*8+((image_in_all_the_people>=128) & (image_in_all_the_people<138))*64+((image_in_all_the_people>=138) & (image_in_all_the_people<148))*80 +((image_in_all_the_people>=148) & (image_in_all_the_people<158))*96+((image_in_all_the_people>=158) & (image_in_all_the_people<168))*112+((image_in_all_the_people>=168) & (image_in_all_the_people<178))*128+((image_in_all_the_people>=178) & (image_in_all_the_people<188))*144+((image_in_all_the_people>=188) & (image_in_all_the_people<198))*160+((image_in_all_the_people>=198) & (image_in_all_the_people<208))*176+((image_in_all_the_people>=208) & (image_in_all_the_people<218))*192+((image_in_all_the_people>=218) & (image_in_all_the_people<228))*208+((image_in_all_the_people>=228) & (image_in_all_the_people<238))*224+(image_in_all_the_people>=238)*240;
 return b;

def hexadecimalitym(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>16)&(image_in_all_the_people<64))*16+((image_in_all_the_people>=64) & (image_in_all_the_people<96))*32+((image_in_all_the_people>=96) & (image_in_all_the_people<128))*48+((image_in_all_the_people>=128) & (image_in_all_the_people<144))*128+((image_in_all_the_people>=144) & (image_in_all_the_people<160))*144+((image_in_all_the_people>=160) & (image_in_all_the_people<176))*160+((image_in_all_the_people>=176) & (image_in_all_the_people<192))*176+((image_in_all_the_people>=192) & (image_in_all_the_people<208))*192+((image_in_all_the_people>=208) & (image_in_all_the_people<224))*208+((image_in_all_the_people>=224) & (image_in_all_the_people<240))*224+(image_in_all_the_people>=240)*240;
 return b;

def hexadecimalitymp(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=numpy.zeros(dim)+((image_in_all_the_people>16)&(image_in_all_the_people<64))*8+ ((image_in_all_the_people>=64)& (image_in_all_the_people<96))*16+ ((image_in_all_the_people>=96) & (image_in_all_the_people<128))*32+((image_in_all_the_people>=128) & (image_in_all_the_people<138))*64+((image_in_all_the_people>=138) & (image_in_all_the_people<148))*80 +((image_in_all_the_people>=148) & (image_in_all_the_people<158))*96+((image_in_all_the_people>=158) & (image_in_all_the_people<168))*112+((image_in_all_the_people>=168) & (image_in_all_the_people<178))*128+((image_in_all_the_people>=178) & (image_in_all_the_people<188))*144+((image_in_all_the_people>=188) & (image_in_all_the_people<198))*160+((image_in_all_the_people>=198) & (image_in_all_the_people<208))*176+((image_in_all_the_people>=208) & (image_in_all_the_people<218))*192+((image_in_all_the_people>=218) & (image_in_all_the_people<228))*208+((image_in_all_the_people>=228) & (image_in_all_the_people<238))*224+(image_in_all_the_people>=238)*240;

 return b;

def pixify(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people;
 for i in range (0,dim[0],2):
  for j in range (0, dim[1],2):
    b[min((i+1),dim[0]-1),j,:]=image_in_all_the_people[i,j,:]; 
    b[i,min((j+1),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[min((i+1),dim[0]-1),min((j+1),dim[1]-1),:]=image_in_all_the_people[i,j,:];
 return b;

def pixify3(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people;
 for i in range (0,dim[0],3):
  for j in range (0, dim[1],3):
    b[min((i+1),dim[0]-1),j,:]=image_in_all_the_people[i,j,:];
    b[min((i+2),dim[0]-1),j,:]=image_in_all_the_people[i,j,:]; 
    b[i,min((j+1),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[i,min((j+2),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[min((i+1),dim[0]-1),min((j+1),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[min((i+2),dim[0]-1),min((j+2),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[min((i+2),dim[0]-1),min((j+1),dim[1]-1),:]=image_in_all_the_people[i,j,:];
    b[min((i+1),dim[0]-1),min((j+2),dim[1]-1),:]=image_in_all_the_people[i,j,:];
 return b;


def pixify_av(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people);
 b=image_in_all_the_people;
 for i in range (0,dim[0],2):
  for j in range (0, dim[1],2):
    b[i,j,:]=(image_in_all_the_people[i,j,:]+image_in_all_the_people[min((i+1),dim[0]-1),j,:]+image_in_all_the_people[i,min((j+1),dim[1]-1),:]+image_in_all_the_people[min((i+1),dim[0]-1),min((j+1),dim[1]-1),:]); 
    b[min((i+1),dim[0]-1),j,:]=b[i,j,:]; 
    b[i,min((j+1),dim[1]-1),:]=b[i,j,:];
    b[min((i+1),dim[0]-1),min((j+1),dim[1]-1),:]=b[i,j,:];
 return b;

def istogram2(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people)
 if numpy.size(dim)==2:
  ist=numpy.zeros(256)
  for a in range (0,255):
   ist[a]=numpy.count_nonzero(image_in_all_the_people==((a-1)*numpy.ones(dim)))/(dim[0]*dim[1])
  return ist;
 else:
  return 0

def istogram_eq(image_in_all_the_people):
 dim=numpy.shape(image_in_all_the_people)
 im_out=numpy.zeros(dim)
 if numpy.size(dim)==2:
  
  istog=istogram2(image_in_all_the_people);
  for a in range (0,255):
   im_out=im_out+(image_in_all_the_people==((a-1)*numpy.ones(dim)))*(numpy.sum(istog[0:a]));
 elif numpy.size(dim)==3:
  istog1=istogram2(image_in_all_the_people[:,:,0]);
  
  for a in range (0,255):
   im_out[:,:,0]=im_out[:,:,0]+((image_in_all_the_people[:,:,0])==((a)*numpy.ones([dim[0],dim[1]])))*(numpy.sum(istog1[0:a]));

  istog2=istogram2(image_in_all_the_people[:,:,1]);
  for a in range (0,255):
   im_out[:,:,1]=im_out[:,:,1]+((image_in_all_the_people[:,:,1])==((a)*numpy.ones([dim[0],dim[1]])))*(numpy.sum(istog2[0:a]));

  istog3=istogram2(image_in_all_the_people[:,:,2]);
  for a in range (0,255):
   im_out[:,:,2]=im_out[:,:,2]+((image_in_all_the_people[:,:,2])==((a)*numpy.ones([dim[0],dim[1]])))*(numpy.sum(istog3[0:a]));

 return im_out*255
