# make model=xf1 inject.bin
import os, json, re

models = [
    
]

model = os.listdir("fujihack/model")
print("Attempt compile:", model)
for m in model:
    name = m.split(".")[0]
    if name == "template" || name == "stub":
        continue

    data = {
        "name": name,
        "main": "",
        "jump": "",
        "code": ""
    }

    # Figure out better solution later?
    f = open("fujihack/model/" + name + ".h", "r")
    matches = data["code"] = re.search(r"#define MODEL_CODE \"([0-9]+)\"", f.read())
    if matches == None:
        data["code"] = ""
    else:
        data["code"] = matches.group(1)

    os.system("cd fujihack; make clean")

    if os.system("cd fujihack; make model=" + name + " file=main.S inject.bin") == 0:
        os.system("cp fujihack/inject.bin main-" + name + ".bin")
        data["main"] = "main-" + name + ".bin"

    os.system("cd fujihack; make clean")

    if os.system("cd fujihack; make model=" + name + " file=jump.S inject.bin") == 0:
        os.system("cp fujihack/inject.bin jump-" + name + ".bin")
        data["jump"] = "main-" + name + ".bin"

    models.append(data)

    f = open("data.js", "w")
    f.write(json.dumps(models))
    f.close()
