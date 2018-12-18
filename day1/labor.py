import os

print(os.listdir('.'))

os.chdir(r'c:\Users\student\chatbot\day1')

print(os.getcwd())

fileList = list(os.listdir('.'))

for i in fileList:
    os.rename(i,i[6:])