from gtts import gTTS

from PyPDF2 import PdfReader
from gtts.lang import tts_langs


def get_text(_filename, _start_page=0, _end_page=0):
    if '.pdf' not in _filename:
        _filename = _filename + '.pdf'
    reader = PdfReader(_filename)
    number_of_pages = len(reader.pages)
    if _end_page == 0:
        _end_page = number_of_pages
    if _start_page == _end_page:
        _end_page += 1
    if not _start_page < _end_page <= number_of_pages:
        print('Incorrect number of pages')
        return None

    _text = []

    for page_number in range(_start_page, _end_page):
        _text.append(reader.pages[page_number].extract_text())

    _text = remove_newlines(_text)

    return ' '.join(_text)


def remove_newlines(lst):
    return [s.replace('\n', ' ') for s in lst]


def get_audio(_text, _output_file, _lang):
    if '.mp3' not in _output_file:
        _output_file = _output_file + '.mp3'
    try:
        audio = gTTS(text=_text, lang=_lang)

        audio.save(_output_file)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pdf_to_parse = input('Enter the path to pdf file (blank for pdf_to_parse): ') or 'pdf_to_parse'
    print(pdf_to_parse)
    start_page = int(input('Enter the page number of the first page to parse (blank for 0): ') or 0)
    end_page = int(input('Enter the page number of the last page to parse (blank for last page): ') or 0)

    lang = input('Enter the language of the pdf file(uk, en etc.) (blank for uk): ') or 'uk'
    output_file = input('Enter the path to output file (blank for message): ') or 'message'

    text = get_text(pdf_to_parse, start_page, end_page)
    if text:
        get_audio(text, output_file, lang)

    # Uncomment to get all language shortcuts printed
    # print(tts_langs())
