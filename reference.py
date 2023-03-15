class Music:
    @staticmethod
    def play():
        print("*playing music*")
    
    def stop(self):
        print("stop playing")

# Check dictionary 
dic = {'a':1, 'c':2}
dic['b']  = 3


if __name__ == "__main__":

    print(dic.items())

    for key, val in dic.items():
        print(key)
