import json
f = open("compute.json", "r")
text = f.read()
print("----------------------------------------"+str(text)+"-----------------------------------------------")
text = text.replace("'", '"')
text = text.replace("True", "true")
text = text.replace("False", "false")
# data = json.dumps(text)

print("\n\n\n"+str(text))