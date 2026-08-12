import chardet

def detect_file_encoding(file_path):
    # Dosyayı okuma ve encoding tespiti
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            confidence = result['confidence']

            return f"Dosyanın karakter kodlaması: {encoding}, Güven: {confidence*100:.2f}%"
    except FileNotFoundError:
        return "Dosya bulunamadı."
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

# Kullanıcıdan dosya adını al
file_name = input("Lütfen dosya adını ve uzantısını girin: ")

# Kodlama formatını öğren
print(detect_file_encoding(file_name))
