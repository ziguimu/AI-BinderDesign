#!/usr/bin/env python3

import os
import json
import csv
from glob import glob


ROOTS=[
    "prediction_controls/Boltz",
    "prediction_controls_mouse/Boltz"
]


OUT="summaries/19_Boltz_confidence.csv"


rows=[]


for root in ROOTS:

    for f in glob(
        root+"/**/confidence_*.json",
        recursive=True
    ):

        with open(f) as h:
            x=json.load(h)


        path=f.split("/")


        # 自动识别 species

        species="mouse" if "mouse" in f else "human"


        # system

        system="unknown"

        for p in path:

            if (
                p.endswith("_human")
                or p.startswith("mEGFR")
            ):
                system=p
                break



        # repeat

        repeat="result"

        for p in path:

            if p.startswith("repeat_"):
                repeat=p
                break



        model=os.path.basename(
            f
        ).replace(
            "confidence_",
            ""
        ).replace(
            ".json",
            ""
        )


        rows.append({

            "species":
                species,

            "system":
                system,

            "repeat":
                repeat,

            "model":
                model,

            "confidence_score":
                x.get("confidence_score"),

            "pTM":
                x.get("ptm"),

            "ipTM":
                x.get("iptm"),

            "complex_pLDDT":
                x.get("complex_plddt"),

            "interface_pLDDT":
                x.get("complex_iplddt"),

            "complex_pDE":
                x.get("complex_pde"),

            "complex_ipDE":
                x.get("complex_ipde"),

            "source":
                f

        })


os.makedirs(
    "summaries",
    exist_ok=True
)


with open(
    OUT,
    "w",
    newline=""
) as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print(
    "done:",
    len(rows),
    "models"
)

print(OUT)
