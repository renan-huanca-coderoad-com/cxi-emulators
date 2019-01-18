import json
import sys

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)
    # print("---")
    for e in data["events"]:
        print("object_id: %s, epclist_size: %d" % (e["id"], len(e["epcList"])))
        if(len(e["epcList"]) > 6):
            # print e["epcList"]
            filename = "%s.txt" % e["id"]
            file = open(filename,"w")
            file.write(json.dumps(e["epcList"], indent=4, sort_keys=True));
            file.close()
