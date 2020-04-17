
import hashlib
import itertools

	#generating all permutations possible
def input_generator(input_string_bits):
	print("==================================================")
	print("Executing Input generator Function \n\n")
	i=0
	ascii_list = []
	for i in range(0,128):
		ascii_list.append(i)

	keyword_list = [chr(x) for x in ascii_list]
	permuted_keywords_list =[''.join(i) for i in itertools.permutations(keyword_list,input_string_bits )]
	print("Number of Permutations generated: ",len(permuted_keywords_list))

	return permuted_keywords_list




	#Generating Hashes for the permutations
def hash_generator(permuted_keywords_list):
	print("==================================================")
	print("Executing hash_generator Function \n\n")
	hashed_permuted_keywords_list = [hashlib.sha256(x.encode('utf-8')  )for x in permuted_keywords_list]

	return hashed_permuted_keywords_list



def hash_compare(hashed_permuted_keywords_list,no_of_bits):
	print("==================================================")
	print("Executing hash_compare Function \n\n")
	compare_iterations = 0
	found_flag = -1
	hashed_permuted_keywords_list_stripped = [x.digest()[:no_of_bits] for x in hashed_permuted_keywords_list]
	hashed_permuted_keywords_list_stripped_str = []
	
	for a, b in itertools.combinations(hashed_permuted_keywords_list_stripped, 2):
		if a == b:
			found_flag =1
			break

		else:
			compare_iterations +=1
			if compare_iterations%100000==0:
				print("{} Comparison done".format(compare_iterations))
	
	if found_flag == 1:
		print(a,b)
		print("Collission found")
		location_finder(a,hashed_permuted_keywords_list_stripped)

	else:
		print("Collission not found")

	return hashed_permuted_keywords_list_stripped




def location_finder(a,hashed_permuted_keywords_list_stripped):
	print("==================================================")
	print("Executing location finder\n\n")
	i=-1
	for x in hashed_permuted_keywords_list_stripped:
		i +=1
		if x==a:
			print("index is:",i,"	and    ",end=" ")
			print("Element is:",str(hashed_permuted_keywords_list_stripped[i]))







if __name__ == '__main__':

	no_of_bits =int( input("Enter hash bits to be compared: ") )
	no_of_places = int( input("Enter no of places: ") )

	permuted_keywords_list = input_generator(no_of_places)

	hashed_permuted_keywords_list=hash_generator(permuted_keywords_list)
	hashed_permuted_keywords_list_stripped =hash_compare(hashed_permuted_keywords_list,no_of_bits)
	

