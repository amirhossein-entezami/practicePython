# with open("test.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()
    
    
with open("test.txt", mode="a") as file: # a -> append , w -> write
    file.write("\nnew text.")
    
# test
# test
# test
# test
# test
# test