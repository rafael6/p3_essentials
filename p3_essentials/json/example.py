import json

with open("data") as json_data:
    data = json.load(json_data)
    print(data["Employee"])  # Employee is the first key, everything else value

    for i in data["Employee"]:
        print(i["name"])  # The value for each item key "name"

        if "manager" in i:  # Only if key "manager" exists
            fo = open(i["id"]+"_"+i["name"]+".txt","w")
            fo.write(i["name"] + "     " + i["manager"] + "    " + i["city"])
            fo.close()

