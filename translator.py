import googletrans
from googletrans import Translator


def translate(word, dest):
    translator = Translator()
    x = translator.translate(word, dest=dest)
    return x.text

if __name__ == "__main__":
    #print(googletrans.LANGUAGES)
    translator = Translator()
    x = translator.translate("how are you", cur="en", dest="es")
    print(x)