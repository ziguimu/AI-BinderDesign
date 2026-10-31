#!/usr/bin/env python3

import csv


INPUT = "summaries/20_Boltz_benchmark_summary.csv"

OUT_TOTAL = "summaries/21_Benchmark_total_summary.csv"

OUT_THRESHOLD = "summaries/22_Benchmark_threshold_summary.csv"



# =========================
# benchmark thresholds
# =========================

IPTM_TH = 0.65

IPSAE_TH = 0.70

PAE_TH = 15.0

CONTACT_TH = 30



# =========================
# class definition
# =========================

def classify(system):

    if "7D12" in system:
        return "negative"

    if system.startswith("mEGFR"):
        return "mouse_positive"

    if "EGF" in system:
        return "human_positive"

    if "cetuximab" in system:
        return "human_positive"

    return "unknown"



def to_float(x):

    try:
        return float(x)
    except:
        return 0.0



# =========================
# load
# =========================

with open(INPUT,newline="") as f:

    rows=list(csv.DictReader(f))



print("loaded rows:",len(rows))



# =========================
# total table
# =========================

total=[]


for r in rows:


    out={}

    out["species"]=r["species"]

    out["system"]=r["system"]

    out["repeat"]=r["repeat"]

    out["model"]=r["model"]

    out["class"]=classify(
        r["system"]
    )


    out["ipTM"]=r["ipTM"]

    out["ipSAE_8A"]=r["ipSAE_8A"]

    out["PAE"]=r["interface_PAE_mean"]

    out["contacts"]=r["contacts_8A"]

    out["pDockQ2"]=r["pDockQ2"]


    total.append(out)



with open(
    OUT_TOTAL,
    "w",
    newline=""
) as f:

    w=csv.DictWriter(
        f,
        fieldnames=total[0].keys()
    )

    w.writeheader()

    w.writerows(total)



# =========================
# threshold summary
# =========================


summary={}



for r in total:


    s=r["system"]


    if s not in summary:

        summary[s]={

            "system":s,

            "class":r["class"],

            "total":0,

            "ipTM_pass":0,

            "ipSAE_pass":0,

            "PAE_pass":0,

            "contacts_pass":0,

            "all_pass":0

        }



    x=summary[s]


    x["total"]+=1


    iptm = (
        to_float(r["ipTM"])
        >= IPTM_TH
    )


    ipsae = (
        to_float(r["ipSAE_8A"])
        >= IPSAE_TH
    )


    pae = (
        to_float(r["PAE"])
        <= PAE_TH
    )


    contact = (
        to_float(r["contacts"])
        >= CONTACT_TH
    )



    if iptm:
        x["ipTM_pass"]+=1


    if ipsae:
        x["ipSAE_pass"]+=1


    if pae:
        x["PAE_pass"]+=1


    if contact:
        x["contacts_pass"]+=1


    if (
        iptm
        and ipsae
        and pae
        and contact
    ):
        x["all_pass"]+=1



with open(
    OUT_THRESHOLD,
    "w",
    newline=""
) as f:


    fields=[
        "system",
        "class",
        "total",
        "ipTM_pass",
        "ipSAE_pass",
        "PAE_pass",
        "contacts_pass",
        "all_pass"
    ]


    w=csv.DictWriter(
        f,
        fieldnames=fields
    )

    w.writeheader()

    w.writerows(
        summary.values()
    )



print("done")

print(OUT_TOTAL)

print(OUT_THRESHOLD)
