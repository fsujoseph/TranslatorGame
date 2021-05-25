import googletrans
from googletrans import Translator


def translate(word, dest, cur='en'):
    translator = Translator()
    res = translator.translate(word, cur=cur, dest=dest)
    return res.text


if __name__ == "__main__":
    translator = Translator()
    x = translator.translate("how are you", cur="en", dest="es")
    print(x)
    print(googletrans.LANGUAGES)