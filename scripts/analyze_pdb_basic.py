import os
import csv
from Bio.PDB import PDBParser


inputs=[
    "analysis_structures/Boltz",
    "analysis_structures/ColabFold"
]


rows=[]

parser=PDBParser(QUIET=True)


for folder in inputs:

    method=os.path.basename(folder)

    for f in os.listdir(folder):

        if not f.endswith(".pdb"):
            continue

        path=os.path.join(folder,f)

        structure=parser.get_structure(
            "x",
            path
        )

        chains={}
        
        for model in structure:
            for chain in model:
                residues=[
                    r for r in chain
                    if r.id[0]==" "
                ]

                chains[chain.id]=len(residues)


        rows.append([
            method,
            f,
            ";".join(chains.keys()),
            ";".join(map(str,chains.values())),
            sum(chains.values())
        ])


with open(
    "summaries/03_structure_basic.csv",
    "w",
    newline=""
) as out:

    w=csv.writer(out)

    w.writerow([
        "method",
        "file",
        "chains",
        "chain_lengths",
        "total_residues"
    ])

    w.writerows(rows)


print("done",len(rows))
