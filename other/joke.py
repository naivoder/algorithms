"""
knock knock...
    who's there?
thisfile...
    'thisfile' who?
thisfile is a joke!

"""
import time

def knockKnock():
    startDelivery = time.time()
    print("I would talk about computer science...")
    comedicTiming = time.time() - startDelivery
    while comedicTiming < 3:
        comedicTiming = time.time() - startDelivery
        pass
    print("but it makes my motherboard!")

if __name__=="__main__":
    knockKnock()
