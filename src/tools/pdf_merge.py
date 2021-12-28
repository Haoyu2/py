from pathlib import Path
from rich import print
from PyPDF2 import PdfFileMerger

if __name__ == '__main__':
    HOME = Path.home()
    data = HOME / 'Downloads' / 'cs210-exam1'

    folders =  [ file for file in data.iterdir() if file.is_dir()]
    files = [file for folder in folders for file in folder.iterdir()]

    print(str(files[0]))
    print(str(files[0].absolute()))
    print(type(str(files[0].absolute())))
    merger = PdfFileMerger()
    for pdf in files: merger.append(open(pdf, 'rb'))
    #
    merger.write(open(data / 'all.pdf', 'wb'))
    merger.close()


