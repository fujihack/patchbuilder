# make model=xf1 inject.bin
import os, json

models = [
    
]

model = os.listdir("fujihack/model")
print("Attempt compile:", model)
for m in model:
    name = m.split(".")[0]
    if name == "template":
        continue

    data = {
        "name": name,
        "main": "",
        "jump": ""
    }

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
