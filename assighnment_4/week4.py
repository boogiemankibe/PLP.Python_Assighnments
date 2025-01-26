# File Read & Write Challenge 🖋️: Create a program that reads a file and
# writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and 
# handle errors if it doesn’t exist or can’t be read.
file=input('name of the file to be read:')
new_file=input('name of the file you want to modify to:')
content=input('give the content you want to append to the new file:')
def file_handling(file,new_file,content):
  try:
   with open(file,'r') as file:
    content=file.read()
   with open(new_file,'wa') as file:
    new_file.write(file)
    new_file.append(content)
  except FileNotFoundError:
   print('ensure you give the correct name of the file or complete path to the file')
  except IOError:
   print('the file cannot be read or written')
file_handling(file,new_file,content)