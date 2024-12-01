from zipfile import ZipFile

with ZipFile('tmp/Hello.zip') as zip_file:
    print(zip_file.namelist())
    text = zip_file.read("hello world.txt")
    print(text)
    zip_file.extract("hello world.txt", path="tmp")
