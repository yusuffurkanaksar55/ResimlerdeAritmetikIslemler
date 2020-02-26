import cv2
import numpy as np

def main():
   resim=cv2.imread("blox.jpg")
   resim1=cv2.imread("orange.jpg")
   a_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
   
   yukseklik,en,kanal=resim.shape
   print(yukseklik,en,kanal)
   ROI=resim1[0:yukseklik,0:en]#ÇIKTISI-->>DİĞER RESİMDEN ALDIĞIMIZ BOYUTLARI DİĞER RESİME UYGUN HALE GETİRİYORUZ
   cv2.imshow("Change",ROI)
   cv2.imshow("Blok",resim)
   cv2.imshow("Portakal",resim1)
   ret,mask=cv2.threshold(a_gri,10,100,cv2.THRESH_BINARY)#ÇIKTISI-> 10PİKSEL ÜZERİ GRİLERİ 255E GÖTÜR
   cv2.imshow("Mask",mask)
   
   mask_inver=cv2.bitwise_not(mask)#BİTLERİN TERSİNİ ALIR.ÇIKTISI-->RENK DEĞİŞİKLİĞİĞ
   cv2.imshow("Maskın Tersi",mask_inver)
   portakal_arka=cv2.bitwise_and(ROI,ROI,mask=mask_inver)
   cv2.imshow("Portakalarka",portakal_arka)
   



if __name__=="__main__":
    main()






cv2.waitKey(0)
cv2.destroyAllWindows()




