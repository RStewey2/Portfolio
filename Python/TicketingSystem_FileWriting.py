#Create Work Tickets from user input as output files
import time

user_input = { "cit_name":"Joe Smith"
, "cit_address":"123 Main St"
, "cit_phone":"111-867-5309"
, "damage_type": "muffler"
,"damage_cost":"$600"
,"pot_size": "5"
,"pot_address":"246 Elm Ave"
,"pot_location": "street"
}

user_input["work_order"] = user_input["cit_address"]+"-"+str(time.time()).replace('.','')
user_input["report_name"] = user_input["cit_name"]+"-"+str(time.time()).replace('.','')


if int(user_input["pot_size"])>= 9:
    pot_priority = "high"
elif int(user_input["pot_size"])>= 5:
    pot_priority =  "medium"
else:
    pot_priority = "low"

## address lookup to apply district based off address
pot_district = "downtown"

print("***Damage Report***\n")
print("Name: " + user_input["cit_name"])
print("Address: " + user_input["cit_address"])
print("Phone: " + user_input["cit_phone"])
print("Damage Type: " + user_input["damage_type"])
print("Damage Cost: " + user_input["damage_cost"]+"\n")
print("==============\n")
print("***Work Order***\n")
print("Work Order:" + user_input["work_order"])
print("Priority: " + user_input["cit_name"])
print("District: " + pot_district)
print("Address: " + user_input["pot_address"])
print("Location: " + user_input["pot_location"])
dmgTitle = 'DMG_RPT_'+str(user_input["cit_name"])+'.txt'
with open(dmgTitle,'w') as f:
    f.write("Damage Report: \n")
    for key in ["cit_name","cit_address","cit_phone","damage_type","damage_cost"]:
        f.write(key + ": "+ str(user_input[key])+"\n")
    f.close()

wrkTitle = 'WRK_ORDR_'+str(user_input["work_order"])+'.txt'
with open(wrkTitle,'w') as f:
    f.write("Work Order: \n")
    for key in ["cit_name","cit_address","cit_phone","damage_type","damage_cost"]:
        f.write(key + ": "+ str(user_input[key])+"\n")
    f.close()
## below set by separate function to identify and assign crew, equipment, and status through work order system
fullfilment = {"Repair Crew": "28",
"Crew Size": "3",
"Equipment": "Standard",
"Status": "Work in progress",
"Work Hours": "TBD",
"Materials Used": "TBD",
"Cost of Repair": "TBD"}

with open(wrkTitle,'a') as f:
    f.write("\nFulfillment: \n")
    print("\nFullfillment: \n")
    for key in fullfilment:
        print(key + ": "+ str(fullfilment[key]))
        f.write(key + ": "+ str(fullfilment[key])+"\n")
    f.close()