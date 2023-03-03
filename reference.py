class Music:
    @staticmethod
    def play():
        print("*playing music*")
    
    def stop(self):
        print("stop playing")

if __name__ == "__main__":

    Music.play()

    obj = Music()
    obj.stop()

