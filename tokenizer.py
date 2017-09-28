import re

TEXT = """Kami      belajar tanpa lelah.
Kami& Tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa#muda.
Itu karena kami ingin kelak istri dan anak kami bahagia."""

def tokenize(text):
    text = text.upper() # membuat text menjadi kapital semua
    text = re.sub(r'[^a-z0-9 -]', ' ', text, flags = re.IGNORECASE|re.MULTILINE) # selain karakter a-z 0-9 itu diganti menjadi spasi (kosong)
    text = re.sub(r'( +)', ' ', text, flags= re.IGNORECASE|re.MULTILINE) # ( +) spasi yang lebih dari satu, diubah menjadi satu spasi saja
    tokens = text.split(" ") 
    return tokens

print(tokenize(TEXT))
		