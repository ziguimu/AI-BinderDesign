import os
import glob
import json
import csv


files = (
    glob.glob(
        "prediction_controls/Colabfold/**/*.json",
        recursive=True
    )
    +
    glob.glob(
        "prediction_controls_mouse/Colabfold/**/*.json",
        recursive=True
    )
)


rows=[]


for f in files:

    # only score json
    if "scores" not in os.path.basename(f):
        continue

    try:
        d=json.load(open(f))
    except:
        continue


    name=os.path.basename(f)


    # species
    if "mouse" in f:
        species="mouse"
    else:
        species="human"


    # system
    if "7D12" in f or "7d12" in f:
        system="7D12"
    elif "EGF" in f:
        system="EGF"
    elif "cetuximab" in f:
        system="cetuximab"
    else:
        system="unknown"


    # model info
    model=name.replace(".json","")


    pDockQ=""
    pDockQ2=""


    if "pdockq" in d:
        pDockQ=list(d["pdockq"].values())[0]

    if "pdockq2" in d:
        pDockQ2=list(d["pdockq2"].values())[0]


    rows.append([
        species,
        system,
        "ColabFold",
        model,
        d.get("ptm",""),
        d.get("iptm",""),
        pDockQ,
        pDockQ2,
        f
    ])



with open(
    "summaries/04_colabfold_confidence.csv",
    "w",
    newline=""
) as out:

    w=csv.writer(out)

    w.writerow([
        "species",
        "system",
        "method",
        "model",
        "pTM",
        "ipTM",
        "pDockQ",
        "pDockQ2",
        "source"
    ])

    w.writerows(rows)


print("done",len(rows))
