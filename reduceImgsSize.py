
"""
Import module
"""
import os
from PIL import Image

"""
Declarare variabile globale
"""
inputUrl = input
outputUrl = output
nrOfPixels = 1000

class resizePhotos(object):
    """Clasa pentru redimensionare imagini"""

    def __init__(self, url, outUrl, pixels):
        """
        Construieste o instanta a clasei.
        :param url: calea de input catre imagini
        :param outUrl: calea de output unde vor fi salvate pozele
        :param pixels: (integer) numarul de pixeli la care va fi redimensionata poza
        """
        self.url = url
        self.outUrl = outUrl
        self.pixels = pixels
        for self.photo in os.listdir(self.url):
            print "Prelucrare imagine: " + self.photo + " ............"
            """
            Instanta a clase Image. Pentru fiecare poza se vor obtine informatiile exif.
            Se realizeaza calculul matematic pentru redimensionare la numarul de pixeli precizat.
            Se foloseste metoda .save() pentru a salva noua imagine la locatia precizata.
            """
            self.img = Image.open(self.url+"\\"+self.photo)
            self.exif_data = self.img.info['exif']
            self.wpercent = (self.pixels/float(self.img.size[0]))
            self.hsize = int((float(self.img.size[1]*float(self.wpercent))))
            self.image = self.img.resize((self.pixels,self.hsize), Image.ANTIALIAS)
            self.image.save(self.outUrl+"\\"+self.photo, exif = self.exif_data)

if __name__ == "__main__":
    x = resizePhotos(inputUrl, outputUrl, nrOfPixels)


