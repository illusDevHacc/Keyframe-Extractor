def compress(file_names,zipname):
    import zipfile
    from colorama import Fore

    compression = zipfile.ZIP_DEFLATED

    zf = zipfile.ZipFile(zipname, mode="w")
    
    try:
        lenight = len(file_names)
        counter=1
        for file_name in file_names:
            zf.write(file_name,compress_type=compression)
            print(Fore.BLUE+ f"{counter}/{lenight} files compressed")
            counter += 1


    except FileNotFoundError:
        print("File Not Found")
    finally:
        
        zf.close()