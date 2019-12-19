#file_decryptor

import os
from cryptography.fernet import Fernet
#input
data_file_flag = 0
while data_file_flag ==0: 
	encrypted_file_loc =input("Enter location of encrypted file :").strip(' "" ') #for stripping quotation marks so that whitespaces canbe taken and then strip
	print("Entered file location is: ",encrypted_file_loc)
	
	if( os.path.exists(encrypted_file_loc) ):
		data_file_flag =1
	else:
		print("Entered file location does not exist")


key_file_loc_flag = 0
while key_file_loc_flag == 0 :
	key_file_loc = input("enter location of key :").strip(' "" ')
	print("Entered key file location is :",key_file_loc)

	if( os.path.exists(key_file_loc) ):
		key_file_loc_flag =1
	else:
		print("Entered key file location does not exist")



#getting key
with open(key_file_loc,'rb') as fp :
	key = fp.read()

#decryption
with open(encrypted_file_loc,'rb') as fp:
	encrypted_data = fp.read()

fernet_obj = Fernet(key)
decrypted_data = fernet_obj.decrypt(encrypted_data)


with open('decrypted_file.txt','wb') as fp:
	fp.write(decrypted_data)


print("File has been decrypted successfully")
