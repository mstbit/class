# ##### writing a file
# ### file handling can be error-prone so we use try statement
# ### to handle exceptions  

# ##### open(), write(), close() #####
file = open('hello.txt', 'w')   # 'w': write mode
try:
    file.write('hello world')
finally:
    file.close()
