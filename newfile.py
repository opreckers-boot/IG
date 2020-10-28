import instagram_exploreas ie
import json
result = ie.user: nama = input("Masukkan nama IG: ")
print ("Nama IG :", nama)
print ("")
parsed_data=json.dump(result,  indent = 4,
											sort_keys = true)
print(parsed_data[15:400])