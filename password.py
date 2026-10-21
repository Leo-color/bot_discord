import random
def gen_pass():
     elements = "+-/*!&$#?=@<>" 
     password = "" 
     for i in range(10): 
        password += random.choice(elements)
        return password

