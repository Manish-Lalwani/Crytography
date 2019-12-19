#crytography

from cryptography.fernet import Fernet 
#==============
#generating key 
generated_key =Fernet.generate_key()

with open('key.key','wb') as fp : 
	fp.write(generated_key)

print("Key has been generated successfully")
