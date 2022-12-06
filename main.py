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
                "name": name,
                "ext": extension
            }

            list_all_files.append(file)

        return list_all_files
        

    def optimize(self) :
        files = self.list_files()

        for file in files :
            print(f"{file}")


if __name__ == "__main__" :

    compressor = Compressor("C:/Users/rodrigo/Downloads")
    compressor.start()
