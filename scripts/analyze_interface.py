import os
import csv
from Bio.PDB import PDBParser, NeighborSearch

pdb_dir = "analysis_structures"

out = "summaries/08_interface_analysis.csv"


def get_residue_contacts(structure, cutoff=5.0):

    atoms = list(structure.get_atoms())

    ns = NeighborSearch(atoms)

    residues = {}

    contacts = 0

    for atom in atoms:
        res1 = atom.get_parent()
        chain1 = res1.get_parent().id

        nearby = ns.search(
            atom.coord,
            cutoff,
            level="A"
        )

        for atom2 in nearby:

            res2 = atom2.get_parent()
            chain2 = res2.get_parent().id

            if chain1 != chain2:

                key1 = (
                    chain1,
                    res1.id[1]
                )

                key2 = (
                    chain2,
                    res2.id[1]
                )

                residues[key1] = 1
                residues[key2] = 1

                contacts += 1

    return len(residues), contacts


parser = PDBParser(QUIET=True)


rows=[]


for root,dirs,files in os.walk(pdb_dir):

    for f in files:

        if not f.endswith(".pdb"):
            continue

        path=os.path.join(root,f)

        try:
            s=parser.get_structure(
                f,
                path
            )

            nres,ncontacts = get_residue_contacts(s)

            rows.append(
                [
                    f,
                    nres,
                    ncontacts,
                    path
                ]
            )

        except Exception as e:
            print("skip",f,e)


with open(out,"w",newline="") as fp:

    w=csv.writer(fp)

    w.writerow(
        [
            "file",
            "interface_residues",
            "contacts",
            "source"
        ]
    )

    w.writerows(rows)


print("done",len(rows))
