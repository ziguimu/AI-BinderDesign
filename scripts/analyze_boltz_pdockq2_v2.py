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



def get_chain_atoms(chain):

    atoms=[]

    for res in chain:

        for atom in res:

            atoms.append(
                atom.coord
            )

    return np.array(atoms)



def get_interface_contacts(
        receptor,
        ligand,
        cutoff=8.0):

    rec_atoms=get_chain_atoms(
        receptor
    )

    lig_atoms=get_chain_atoms(
        ligand
    )


    if len(rec_atoms)==0 or len(lig_atoms)==0:
        return 0,0


    contacts=0
    interface_res=set()


    for res in receptor:

        hit=False

        for atom in res:

            d=np.linalg.norm(
                lig_atoms-atom.coord,
                axis=1
            )

            if np.any(d < cutoff):

                hit=True
                break


        if hit:

            contacts+=1
            interface_res.add(
                res.id[1]
            )


    return contacts, len(interface_res)



def get_pae_file(cif):

    name=os.path.basename(cif)

    pae_name="pae_"+name.replace(
        ".cif",
        ".npz"
    )

    root=os.path.dirname(
        cif
    )


    result=[]

    for r,_,files in os.walk(
        os.path.dirname(
            os.path.dirname(root)
        )
    ):

        if pae_name in files:

            result.append(
                os.path.join(
                    r,
                    pae_name
                )
            )


    if result:
        return result[0]

    return None



def interface_pae(
        pae,
        rec_len):

    return float(
        np.mean(
            pae[
                :rec_len,
                rec_len:
            ]
        )
    )



def calc_pdockq2(
        contacts,
        pae,
        size):


    if contacts==0:
        return 0.0


    # interface score
    x = (
        np.log(
            contacts+1
        )
        *
        size
        /
        (pae+1)
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


        ligand_atoms=chains[1:]


        total_contacts=0
        total_interface=0


        for lig in ligand_atoms:

            c,i=get_interface_contacts(
                receptor,
                lig
            )

            total_contacts+=c
            total_interface+=i



        pae_file=get_pae_file(
            cif
        )


        if pae_file is None:
            continue


        pae=np.load(
            pae_file
        )["pae"]


        rec_len=len(
            list(receptor.get_residues())
        )


        pae_value=interface_pae(
            pae,
            rec_len
        )


        score=calc_pdockq2(
            total_contacts,
            pae_value,
            total_interface
        )


        rows.append({

            "cif":
                cif,

            "receptor_chain":
                receptor.id,

            "ligand_chains":
                ",".join(
                    [x.id for x in ligand_atoms]
                ),

            "contacts":
                total_contacts,

            "interface_residues":
                total_interface,

            "interface_PAE":
                pae_value,

            "pDockQ2":
                score

        })



outfile=(
    OUT+
    "/17_pDockQ2_Boltz_v2.csv"
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
