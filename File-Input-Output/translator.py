from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('trans.txt', 'r') as files:
        text = files.read()
        translation = translator.translate(text)
        with open('trans_ja.txt',mode='w', encoding='utf-8') as myfile2:
            myfile2.write(translation)
except FileNotFoundError as err:
    print(f'find not found: {err}')
except IOError as err:
    print(f'IOError: {err}')