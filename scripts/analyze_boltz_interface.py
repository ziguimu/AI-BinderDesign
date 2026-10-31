#!/usr/bin/env python3

import os
import json
import csv
import numpy as np
from glob import glob


ROOTS = [
    "prediction_controls/Boltz",
    "prediction_controls_mouse/Boltz"
]

OUT = "summaries"

os.makedirs(OUT, exist_ok=True)



def load_json(path):
    with open(path) as f:
        return json.load(f)



def find_lengths(obj):
    """
    Recursively search chain lengths in Boltz record json
    """

    lengths = []

    def walk(x):

        if isinstance(x, dict):

            for k, v in x.items():

                if k.lower() in [
                    "length",
                    "num_residues",
                    "n_residues"
                ]:

                    if isinstance(v, int):
                        lengths.append(v)

                walk(v)


        elif isinstance(x, list):

            for item in x:
                walk(item)


    walk(obj)

    # remove duplicates but keep order
    out = []
    for x in lengths:
        if x not in out:
            out.append(x)

    return out



def calculate_interface_pae(pae, lengths):

    if len(lengths) < 2:
        return None


    receptor_len = lengths[0]

    ligand_len = sum(lengths[1:])


    interface = pae[
        0:receptor_len,
        receptor_len:receptor_len+ligand_len
    ]


    return {
        "mean": float(np.mean(interface)),
        "min": float(np.min(interface)),
        "max": float(np.max(interface)),
        "shape": str(interface.shape)
    }



rows = []



for root in ROOTS:

    pae_files = glob(
        root + "/**/pae_*.npz",
        recursive=True
    )


    for pae_file in pae_files:


        # 
        # .../boltz_results_xxx/predictions/xxx/pae_xxx.npz
        #
        prediction_dir = os.path.dirname(pae_file)

        boltz_result_dir = os.path.dirname(
            os.path.dirname(prediction_dir)
        )


        record_files = glob(
            boltz_result_dir
            + "/processed/records/*.json"
        )


        if not record_files:
            print(
                "No record:",
                pae_file
            )
            continue


        record = load_json(
            record_files[0]
        )


        pae = np.load(
            pae_file
        )["pae"]


        lengths = find_lengths(
            record
        )


        result = calculate_interface_pae(
            pae,
            lengths
        )


        if result is None:

            print(
                "Cannot determine chains:",
                pae_file,
                lengths
            )

            continue


        # metadata

        path_parts = pae_file.split("/")

        species = (
            "mouse"
            if "mouse" in pae_file or "mEGFR" in pae_file
            else "human"
        )


        system = [
            x for x in path_parts
            if x.startswith("mEGFR")
            or x in [
                "EGF_human",
                "7D12_human",
                "cetuximab_human"
            ]
        ]


        repeat = "result"

        for x in path_parts:

            if x.startswith("repeat_"):
                repeat = x


        rows.append({

            "species": species,

            "system":
                system[0]
                if system
                else "unknown",

            "repeat": repeat,

            "model":
                os.path.basename(
                    pae_file
                ),

            "chain_lengths":
                str(lengths),

            "interface_shape":
                result["shape"],

            "interface_PAE_mean":
                result["mean"],

            "interface_PAE_min":
                result["min"],

            "interface_PAE_max":
                result["max"],

            "pae_file":
                pae_file

        })



if len(rows) == 0:

    print(
        "No valid Boltz PAE records found"
    )

    exit()



outfile = (
    OUT
    + "/16_interface_PAE_Boltz.csv"
)


with open(
    outfile,
    "w",
    newline=""
) as f:


    writer = csv.DictWriter(
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

print(
    "output:",
    outfile
)
