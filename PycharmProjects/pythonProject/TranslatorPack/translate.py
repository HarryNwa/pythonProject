
from translate import Translator

text = "How are you?"

translate = Translator(to_lang='ja')
translation = Translator.translate(text)

print(translation)