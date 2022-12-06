from PIL import Image
import os

class Compressor :

    def __init__(self, path) :
        print("init")
        self.path = path

    
    def start(self) :
        self.optimize()


    def list_files(self) :

        list_all_files = list()

        for filename in os.listdir(self.path) :

            name, extension = os.path.splitext(self.path + filename)

            file = {
                "name": name.split("/")[-1],
                "ext": extension
            }

            list_all_files.append(file)

        return list_all_files
        

    def optimize(self) :
        files = self.list_files()

        for file in files :

            if file["ext"] in [".jpg", ".png", ".jpeg"] :
                picture = Image.open(self.path + file["name"] + file["ext"])
                picture.save(self.path + "compressed_" + file["name"] + file["ext"], optimize=True, quality=60)
                print(f"compressed file -> {file['name'] + file['ext']}")
            


if __name__ == "__main__" :

    compressor = Compressor("C:/Users/rodrigo/Downloads/")
    compressor.start()
