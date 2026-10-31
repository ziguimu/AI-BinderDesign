#!/usr/bin/env python3

import os
import csv
import numpy as np
from glob import glob
from Bio.PDB import MMCIFParser


ROOTS = [
    "prediction_controls/Boltz",
    "prediction_controls_mouse/Boltz"
]

OUT = "summaries"


os.makedirs(OUT, exist_ok=True)



def load_pae(cif_file):

    pae_file = cif_file.replace(
        ".cif",
        ""
    )

    # cif:
    # xxx_model_0.cif
    #
    # pae:
    # pae_xxx_model_0.npz

    folder = os.path.dirname(cif_file)

    name = os.path.basename(
        cif_file
    )

    pae_name = (
        "pae_"
        + name
        .replace("_model", "_model")
        .replace(".cif",".npz")
    )


    candidates = glob(
        folder + "/../*/*/"
        + pae_name
    )


    # fallback: recursive search
    if not candidates:

        candidates = glob(
            os.path.dirname(
                os.path.dirname(
                    folder
                )
            )
            +
            "/**/"
            +
            pae_name,
            recursive=True
        )


    if candidates:
        return candidates[0]


    return None



def get_contacts(
        cif_file,
        receptor="A",
        cutoff=8.0):


    parser = MMCIFParser(
        QUIET=True
    )

    structure = parser.get_structure(
        "complex",
        cif_file
    )


    model = structure[0]


    if receptor not in model:
        return 0


    chainA = model[receptor]


    ligand_atoms=[]

    for chain in model:

        if chain.id != receptor:

            for res in chain:

                for atom in res:

                    ligand_atoms.append(
                        atom.coord
                    )


    contacts=set()


    for res in chainA:

        hit=False

        for atom in res:

            d=np.linalg.norm(
                np.array(ligand_atoms)
                -
                atom.coord,
                axis=1
            )

            if np.any(d < cutoff):

                hit=True
                break


        if hit:

            contacts.add(
                res.id[1]
            )


    return len(contacts)



def interface_pae(pae):

    n = pae.shape[0]

    # first chain vs rest
    #
    # chain boundary unknown,
    # use half split as fallback

    mid=n//2

    x=pae[
        :mid,
        mid:
    ]

    return float(
        np.mean(x)
    )



def pdockq2(
        contacts,
        pae):


    if contacts == 0:
        return 0


    x = (
        np.log(
            contacts+1
        )
        *
        (1/(pae+1))
    )


    score = (
        0.724 /
        (
            1+
            np.exp(
                -0.052*(x-152.611)
            )
        )
        +
        0.018
    )


    return float(score)



rows=[]



for root in ROOTS:

    for cif in glob(
        root+"/**/*.cif",
        recursive=True
    ):


        pae_file = cif.replace(
            ".cif",
            ""
        )


        npz = glob(
            os.path.dirname(cif)
            +
            "/../**/pae*.npz",
            recursive=True
        )


        if not npz:
            continue


        pae=np.load(
            npz[0]
        )["pae"]


        contacts=get_contacts(
            cif
        )


        pae_mean=interface_pae(
            pae
        )


        score=pdockq2(
            contacts,
            pae_mean
        )


        rows.append({

            "cif":
                cif,

            "contacts":
                contacts,

            "interface_PAE":
                pae_mean,

            "pDockQ2":
                score

        })



with open(
    OUT+"/17_pDockQ2_Boltz.csv",
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
