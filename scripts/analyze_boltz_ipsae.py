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



def load_structure(cif):

    parser = MMCIFParser(
        QUIET=True
    )

    return parser.get_structure(
        "complex",
        cif
    )



def atom_distance(a1, a2):

    return np.linalg.norm(
        a1-a2
    )



def get_residue_pairs(
        receptor,
        ligand,
        cutoff):


    pairs=[]


    for r_res in receptor:

        r_atoms=[
            a.coord
            for a in r_res
        ]


        for l_res in ligand:

            l_atoms=[
                a.coord
                for a in l_res
            ]


            hit=False


            for ra in r_atoms:

                for la in l_atoms:

                    if atom_distance(
                        ra,
                        la
                    ) < cutoff:

                        hit=True
                        break

                if hit:
                    break


            if hit:

                pairs.append(
                    (
                        r_res.id[1]-1,
                        l_res.id[1]-1
                    )
                )


    return pairs



def find_pae(cif):

    filename=os.path.basename(
        cif
    )

    pae_name="pae_"+filename.replace(
        ".cif",
        ".npz"
    )


    root=os.path.dirname(cif)


    for r,_,files in os.walk(
        os.path.dirname(
            os.path.dirname(root)
        )
    ):

        if pae_name in files:

            return os.path.join(
                r,
                pae_name
            )


    return None



def calc_ipsae(
        pae,
        pairs,
        cutoff):


    if len(pairs)==0:

        return 0


    values=[]


    for i,j in pairs:

        if i < pae.shape[0] and j < pae.shape[0]:

            p=pae[i,j]


            # PAE confidence transform

            score=1/(1+p/cutoff)


            values.append(
                score
            )


    if not values:

        return 0


    return float(
        np.mean(values)
    )



rows=[]



for root in ROOTS:


    for cif in glob(
        root+"/**/*.cif",
        recursive=True
    ):


        structure=load_structure(
            cif
        )


        model=structure[0]


        chains=list(
            model
        )


        if len(chains)<2:
            continue


        receptor=chains[0]


        pae_file=find_pae(
            cif
        )


        if pae_file is None:
            continue


        pae=np.load(
            pae_file
        )["pae"]


        scores={}


        all_pairs={}


        for c in [4,8,12]:


            pairs=[]

            for ligand in chains[1:]:

                pairs.extend(
                    get_residue_pairs(
                        receptor,
                        ligand,
                        c
                    )
                )


            all_pairs[c]=pairs


            scores[c]=calc_ipsae(
                pae,
                pairs,
                c
            )



        rows.append({

            "cif":
                cif,

            "ipSAE_4A":
                scores[4],

            "ipSAE_8A":
                scores[8],

            "ipSAE_12A":
                scores[12],

            "ipSAE_min":
                min(
                    scores.values()
                ),

            "contacts_8A":
                len(
                    all_pairs[8]
                )

        })



outfile = (
    OUT+
    "/18_ipSAE_Boltz.csv"
)



with open(
    outfile,
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

print(outfile)
