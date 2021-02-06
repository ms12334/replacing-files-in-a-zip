import zipfile

# check if it's a zip file
print(zipfile.is_zipfile('test.zip'))

with open('eggs1.txt') as fin:
    f = fin.read()
    with zipfile.ZipFile('test.zip','w') as myzip:
        with myzip.open('eggs2.txt','w') as fout:
            fout.write(f.encode())
    
