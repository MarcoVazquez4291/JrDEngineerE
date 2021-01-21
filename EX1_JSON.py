# Ok so for this i know that the first thing i have to do is import the json library
# import json
# import csv

# Once I have imported the json library, I load the data that im going to use and store it in a variable which me and everyone reading the code can easily remember
# data = '''{
#     "profile_id": "1f5833f4e027e0a127f1161450370fa6370a8f5e",
#     "registry_location": "mx",
#     "full_name": "Juan Perez",
#     "document": [
#         {
#             "type": "house|work|school",
#             "address": {
#                 "full_address": "Benito Juarez #35, colonia Arboledas, Queretaro, Santiago de Queretaro, Mexico CP. 76000",
#                 "address_line_1": "Benito Juarez #35",
#                 "address_line_2": "colonia Arboledas",
#                 "city": "Nuevo Toledo",
#                 "foad": "Toledo",
#                 "soad": "",
#                 "postal_code": "76000",
#                 "country": "Mexico",
#                 "phone": ["4420000001","4420000000"],
#                 "fax": [],
#                 "email": ["example@domain.mx"]
#             },
#             "number": "",
#             "description": ""
#         }
#       ],
#     "status": "",
#     "ad_hoc": []
# }'''

# info = json.loads(data)

# print(info)  <- test to see if everything was working correctly
# Next, just to again make sure everything is working like it is supposed to, i retrieve the profile id (simply because it's the first value)

# pid = info["profile_id"]
# print('Profile id: ', pid)

# And the same to make sure I can access the dictionary

# WorkAdress = info["document"][0]["address"]["full_address"]
# print('Work Adress: ', WorkAdress)

# So by now i just wanted to see how to retrieve the data that i want, nex't step is to create the function
# At this point I had to search how to save the json as csv, and found a youtube video explaining
# After adapting some of the code and looking at how i retrieved the information this is what i came up with

import json
import csv

#with open('/home/user/Documents/candidates_documents/') as f:
with open('./example.json') as f:
    addid = f.read()

#check if everything is fine, it is retrieving a string
#print(addid) 

# Conver it to json
addid = json.loads(addid)
# print(json.dumps(addid, indent=2)) looks good
# print(type(addid)) return a dictionary and i was expecting a list, so i had to search on stackoverflow

with open('addid.csv', 'w') as f:
    writer = csv.DictWriter(f, addid.keys())
    writer.writeheader()

    for key, value in addid.items():
        f_id = addid['profile_id']
        f_address = addid["document"][0]["address"]["full_address"]
        print(f_id, f_address)
        writer.writerow(addid)
        # print(key, value) tried multiple print statements, had to see what was going on
        # im not sure why it's printing the same thing multiple times 
        # (I think its because of the .keys(), I think about reading the documentationbut i'm running out of time)