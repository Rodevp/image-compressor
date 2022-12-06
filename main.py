from PIL import Image
import os

class Compressor :

    def __init__(self, path) :
        print("init")
        self.path = path

    
    def start(self) :
        self.list_files()


    def list_files(self) :

        print(f"**list files in your download folder*")
        print()
        for filename in os.listdir(self.path) :
            print(filename)





if __name__ == "__main__" :

    compressor = Compressor("C:/Users/rodrigo/Downloads")
    compressor.start()
