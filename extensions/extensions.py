
def main():
    file_name = input("File name: ")
    print(extension(file_name))

def extension(file):

    extension = file[file.rfind("."):].strip().lower()
    
    match extension:
        case ".gif":
            return "image/gif"
        case ".jpeg":
            return "image/jpeg"
        case ".jpg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
