from googletrans import Translator

def translate_lines(lines):
    translator = Translator()
    return [translator.translate(line, src='hi', dest='en').text for line in lines]
