
import json
#1
data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_json = json.dumps(data)
with open('data_json.json','w') as f:
    json.dump(data_json,f)
    data_json.replace(" \\ ",'')

print(data_json)
#2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba_json2 = json.loads(talaba_json)

print(f"Talabning ismi {talaba_json2['ism']}, Familiyasi {talaba_json2['familiya']}")
#2.2

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba_json2_2 = json.loads(talaba_json)

ism  = talaba_json2_2['ism']
familiya = talaba_json2_2['familiya']


print(f"Ism-> {ism}, Familiya ->{familiya}")


#3
with open('ism.json','w') as file1:
    json.dump(ism,file1)

with open('familiya.json','w') as file2:
    json.dump(familiya,file2)
