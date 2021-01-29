import pywhatkit as pw
name = input('Enter the path of the image:\n')
pw.image_to_ascii_art(name,output_file=f'{name}_ascii_art.txt')
input('done..')
