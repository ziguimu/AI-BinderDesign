import json
import glob
import csv
import os


systems = {
    "7D12_human":
    "Boltz/7D12_human/result/boltz_results_7D12/predictions/7D12",

    "EGF_human":
    "Boltz/EGF_human/result/boltz_results_EGF/predictions/EGF",

    "cetuximab_human":
    "Boltz/cetuximab_human/result/boltz_results_cetuximab/predictions/cetuximab"
}


rows=[]


for system,path in systems.items():

    files=sorted(
        glob.glob(
            path+"/confidence_*.json"
        )
    )

    for f in files:

        with open(f) as x:
            d=json.load(x)


        model=os.path.basename(f)\
            .replace("confidence_","")\
            .replace(".json","")


        rows.append({

            "system":system,

            "model":model,

            "confidence_score":
                d["confidence_score"],

            "pTM":
                d["ptm"],

            "ipTM":
                d["iptm"],

            "protein_ipTM":
                d["protein_iptm"],

            "complex_pLDDT":
                round(d["complex_plddt"]*100,2),

            "interface_pLDDT":
                round(d["complex_iplddt"]*100,2),

            "complex_pDE":
                d["complex_pde"],

            "interface_pDE":
                d["complex_ipde"]

        })


out="Boltz_human_controls_summary.csv"


with open(out,"w",newline="") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print("Finished:",out)
print("Models:",len(rows))
