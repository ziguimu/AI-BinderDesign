import os
import glob
import json
import csv


rows=[]


files = glob.glob(
    "prediction_controls/**/*.json",
    recursive=True
)+glob.glob(
    "prediction_controls_mouse/**/*.json",
    recursive=True
)


for f in files:

    if "confidence_" not in f and "_scores_" not in f:
        continue

    try:
        with open(f) as fh:
            data=json.load(fh)
    except:
        continue


    row={}

    row["source"]=f


    if "confidence_" in f:
        row["method"]="Boltz"

        row["confidence"]=data.get(
            "confidence_score",
            data.get("confidence")
        )

        row["pTM"]=data.get("ptm",data.get("pTM"))
        row["ipTM"]=data.get("iptm",data.get("ipTM"))

        row["pLDDT"]=data.get(
            "complex_plddt",
            data.get("complex_pLDDT")
        )

        row["interface_pLDDT"]=data.get(
            "interface_plddt",
            data.get("interface_pLDDT")
        )


    elif "_scores_" in f:

        row["method"]="ColabFold"

        row["confidence"]=data.get(
            "ranking_confidence"
        )

        row["pTM"]=data.get(
            "ptm"
        )

        row["ipTM"]=data.get(
            "iptm"
        )

        row["pLDDT"]=data.get(
            "plddt"
        )


    name=f.lower()

    if "mouse" in name or "megfr" in name:
        row["species"]="mouse"
    else:
        row["species"]="human"


    if "7d12" in name:
        row["system"]="7D12"
    elif "egf" in name:
        row["system"]="EGF"
    elif "cetuximab" in name:
        row["system"]="cetuximab"
    else:
        row["system"]="unknown"


    rows.append(row)


os.makedirs("summaries",exist_ok=True)

with open(
    "summaries/01_confidence_all.csv",
    "w",
    newline=""
) as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
            "species",
            "system",
            "method",
            "confidence",
            "pTM",
            "ipTM",
            "pLDDT",
            "interface_pLDDT",
            "source"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)


print("saved",len(rows))
