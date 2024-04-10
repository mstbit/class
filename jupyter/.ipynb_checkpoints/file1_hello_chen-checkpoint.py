# ##### writing a file
# ### file handling can be error-prone so we use try statement
# ### to handle exceptions  

# ##### open(), write(), close() #####
<<<<<<<< HEAD:jupyter/hello_Miller.py
file = open('02_file1_write_hello_Miller.txt', 'w')   # 'w': write mode
========
file = open('file1_hello_chen.txt', 'w')   # 'w': write mode
>>>>>>>> d919a03d8b009c62b7a2d5ff2e276bfdeb3567f5:jupyter/.ipynb_checkpoints/file1_hello_chen-checkpoint.py
try:
    file.write('file1_hello_chen.py')
finally:
    file.close()
