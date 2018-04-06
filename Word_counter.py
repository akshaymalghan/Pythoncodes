#Calculate the number of words in the document.


file = open('testfile.txt','r') 
data  = file.read()

num=len(data.split())
print('The number of words in document =',(num))

file.close()