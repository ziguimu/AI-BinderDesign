import os
import csv
import math
from Bio.PDB import PDBParser


indir = "analysis_structures"
out = "summaries/15_interface_chemistry.csv"


# distance
def dist(a,b):
    return math.sqrt(
        sum(
            (a[i]-b[i])**2
            for i in range(3)
        )
    )


# donor atoms
donor_atoms = {
    "N",
    "O"
}


# hydrophobic residues
hydrophobic = {
    "ALA",
    "VAL",
    "LEU",
    "ILE",
    "MET",
    "PHE",
    "TRP",
    "TYR",
    "PRO"
}


acidic = {
    "ASP",
    "GLU"
}


basic = {
    "LYS",
    "ARG",
    "HIS"
}



parser = PDBParser(QUIET=True)


rows=[]



for root,dirs,files in os.walk(indir):

    for f in files:

        if not f.endswith(".pdb"):
            continue


        pdb=os.path.join(root,f)


        try:

            structure=parser.get_structure(
                "x",
                pdb
            )


            chains=list(structure[0])


            if len(chains)<2:
                continue


            receptor=chains[0]

            binder_atoms=[]
            receptor_atoms=[]


            for atom in receptor.get_atoms():
                receptor_atoms.append(atom)



            for chain in chains[1:]:
                for atom in chain.get_atoms():
                    binder_atoms.append(atom)



            hbonds=0
            salt=0
            hydro=0



            checked=set()



            for a in receptor_atoms:

                res1=a.get_parent()

                name1=res1.resname


                for b in binder_atoms:

                    d=dist(
                        a.coord,
                        b.coord
                    )


                    if d>5.0:
                        continue



                    res2=b.get_parent()

                    name2=res2.resname



                    pair=(
                        res1.id,
                        res2.id
                    )


                    if pair in checked:
                        continue

                    checked.add(pair)



                    # H bond
                    if d<=3.5:

                        if (
                            a.element in donor_atoms
                            and
                            b.element in donor_atoms
                        ):
                            hbonds+=1



                    # salt bridge

                    if d<=4.0:

                        if (
                            (
                                name1 in acidic
                                and
                                name2 in basic
                            )
                            or
                            (
                                name2 in acidic
                                and
                                name1 in basic
                            )
                        ):
                            salt+=1



                    # hydrophobic

                    if d<=5.0:

                        if (
                            name1 in hydrophobic
                            and
                            name2 in hydrophobic
                        ):
                            hydro+=1




            rows.append([
                f,
                hbonds,
                salt,
                hydro,
                pdb
            ])


            print("done",f)



        except Exception as e:

            print("fail",f,e)



with open(out,"w",newline="") as fp:

    writer=csv.writer(fp)

    writer.writerow([
        "file",
        "Hbond",
        "salt_bridge",
        "hydrophobic_contacts",
        "source"
    ])

    writer.writerows(rows)



print("saved",out)
print("rows",len(rows))
