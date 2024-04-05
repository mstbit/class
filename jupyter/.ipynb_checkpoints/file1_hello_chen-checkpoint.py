# ##### writing a file
# ### file handling can be error-prone so we use try statement
# ### to handle exceptions  

# ##### open(), write(), close() #####
file = open('file1_hello_chen.txt', 'w')   # 'w': write mode
try:
    file.write('file1_hello_chen.py')
finally:
    file.close()
