#!/usr/bin/env python3

import csv
import os


CONF_FILE = "summaries/19_Boltz_confidence.csv"
PAE_FILE = "summaries/16_interface_PAE_Boltz.csv"
IPSAE_FILE = "summaries/18_ipSAE_Boltz.csv"
PDOCK_FILE = "summaries/17_pDockQ2_Boltz_v2.csv"

OUT = "summaries/20_Boltz_benchmark_summary.csv"



def read_csv(path):

    with open(path, newline="") as f:
        return list(csv.DictReader(f))



def clean_system(x):

    if not x:
        return ""

    return x.replace("_human","")



def clean_model(x):

    if not x:
        return ""

    x = os.path.basename(x)


    for s in [
        "confidence_",
        "pae_",
        "ipSAE_",
        "pDockQ2_"
    ]:
        x = x.replace(s,"")


    for s in [
        ".json",
        ".npz",
        ".cif"
    ]:
        x = x.replace(s,"")


    return x



def make_key(system, repeat, model):

    return (
        clean_system(system),
        repeat,
        clean_model(model)
    )



def path_to_key(path):

    parts = path.split("/")

    system = ""
    repeat = "result"


    for p in parts:


        # human controls
        if p.endswith("_human"):
            system = p


        # mouse EGFR controls
        if p.startswith("mEGFR_") and "_model_" not in p:
            system = p


        if p.startswith("repeat_"):
            repeat = p


    return make_key(
        system,
        repeat,
        path
    )



def build_map(data):

    result = {}


    for r in data:


        if "cif" in r:

            key = path_to_key(
                r["cif"]
            )


        elif "system" in r and "model" in r:

            key = make_key(
                r["system"],
                r["repeat"],
                r["model"]
            )


        else:
            continue


        result[key] = r


    return result



# =========================
# load
# =========================

conf = read_csv(CONF_FILE)

pae = read_csv(PAE_FILE)

ipsae = read_csv(IPSAE_FILE)

pdock = read_csv(PDOCK_FILE)



pae_map = build_map(pae)

ipsae_map = build_map(ipsae)

pdock_map = build_map(pdock)



print("PAE keys:", len(pae_map))
print("ipSAE keys:", len(ipsae_map))
print("pDock keys:", len(pdock_map))



# =========================
# merge
# =========================

rows = []


for r in conf:


    key = make_key(
        r["system"],
        r["repeat"],
        r["model"]
    )


    out = {


        "species":
        r["species"],


        "system":
        r["system"],


        "repeat":
        r["repeat"],


        "model":
        r["model"],


        "pTM":
        r["pTM"],


        "ipTM":
        r["ipTM"],


        "complex_pLDDT":
        r["complex_pLDDT"],


        "interface_pLDDT":
        r["interface_pLDDT"],


        "interface_PAE_mean":
        "",


        "interface_PAE_min":
        "",


        "interface_PAE_max":
        "",


        "ipSAE_4A":
        "",


        "ipSAE_8A":
        "",


        "ipSAE_12A":
        "",


        "ipSAE_min":
        "",


        "contacts_8A":
        "",


        "pDockQ2":
        ""

    }


    if key in pae_map:

        x = pae_map[key]

        out["interface_PAE_mean"] = x.get(
            "interface_PAE_mean",
            ""
        )

        out["interface_PAE_min"] = x.get(
            "interface_PAE_min",
            ""
        )

        out["interface_PAE_max"] = x.get(
            "interface_PAE_max",
            ""
        )


    if key in ipsae_map:

        x = ipsae_map[key]

        out["ipSAE_4A"] = x.get(
            "ipSAE_4A",
            ""
        )

        out["ipSAE_8A"] = x.get(
            "ipSAE_8A",
            ""
        )

        out["ipSAE_12A"] = x.get(
            "ipSAE_12A",
            ""
        )

        out["ipSAE_min"] = x.get(
            "ipSAE_min",
            ""
        )

        out["contacts_8A"] = x.get(
            "contacts_8A",
            ""
        )


    if key in pdock_map:

        x = pdock_map[key]

        out["pDockQ2"] = x.get(
            "pDockQ2",
            ""
        )


    rows.append(out)



# =========================
# write
# =========================


fields = list(rows[0].keys())


with open(
    OUT,
    "w",
    newline=""
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=fields
    )

    writer.writeheader()

    writer.writerows(rows)



print(
    "done:",
    len(rows),
    "rows"
)

print(OUT)
