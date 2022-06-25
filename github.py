from pymongo import MongoClient
import time
import requests
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")  
db = conn.Registrations  
collection = db.licenseNumbers 
cursor = collection.find() 
for record in cursor:
    print(record)
#count=1 
my_dict = {}
# file handling
f = open("D:\Engineering design project\Implementation\output.txt", "r")
l = f.readlines()
for key in l:     
    if key in my_dict:
        count=my_dict.get(key)+1
        my_dict[key]=count
    else:
        my_dict[key]=1
    #print(i,end="")    

print(my_dict)
Keymax = max(zip(my_dict.values(), my_dict.keys()))[1]  
# extracting data from db
num = Keymax.strip()
for x in db.licenseNumbers.find({"Reg_no":num},{ "Phone_no":1 }):     
    res = str(int(x.get("Phone_no")))   
    print(res)

#API 
url = "https://www.fast2sms.com/dev/bulkV2"

payload = "sender_id=FSTSMS&message=You have been fined Rs 1000 for violating the traffic rules&language=english&route=p&numbers="+res
headers = {
    #This is my Auth Key and should not be revealed out.
'authorization': "##################################",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
print("test..")
f.close()

    
 
