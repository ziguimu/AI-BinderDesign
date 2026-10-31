import os
import glob
import json
import csv


files = glob.glob(
    "prediction_controls/Boltz/**/*.json",
    recursive=True
)+glob.glob(
    "prediction_controls_mouse/Boltz/**/*.json",
    recursive=True
)


rows=[]


for f in files:

    if "confidence_" not in f:
        continue


    with open(f) as x:
        d=json.load(x)


    path=f.split("/")


    species="mouse" if "mouse" in f else "human"


    if "7D12" in f or "7d12" in f:
        system="7D12"
    elif "EGF" in f:
        system="EGF"
    elif "cetuximab" in f:
        system="cetuximab"
    else:
        system="unknown"



    rows.append([
        species,
        system,
        "Boltz",
        d.get("confidence_score"),
        d.get("ptm"),
        d.get("iptm"),
        d.get("complex_plddt")*100,
        d.get("complex_iplddt")*100,
        d.get("complex_pde"),
        d.get("complex_ipde"),
        f
    ])



with open(
    "summaries/02_boltz_confidence_correct.csv",
    "w",
    newline=""
) as out:

    w=csv.writer(out)

    w.writerow([
        "species",
        "system",
        "method",
        "confidence",
        "pTM",
        "ipTM",
        "complex_pLDDT",
        "interface_pLDDT",
        "complex_pDE",
        "interface_pDE",
        "source"
    ])

    w.writerows(rows)


print("done",len(rows))
