import os
import csv
import freesasa
from Bio.PDB import PDBParser, PDBIO, Select


indir="analysis_structures"
out="summaries/14_BSA_real.csv"


class ChainSelect(Select):

    def __init__(self, chains):
        self.chains=chains

    def accept_chain(self, chain):
        return chain.id in self.chains



def calc_sasa(pdb):

    s=freesasa.Structure(pdb)

    r=freesasa.calc(s)

    return r.totalArea()



def save_chain(pdb, chains, outp):

    parser=PDBParser(QUIET=True)

    structure=parser.get_structure(
        "x",
        pdb
    )

    io=PDBIO()
    io.set_structure(structure)

    io.save(
        outp,
        ChainSelect(chains)
    )



rows=[]


for root,dirs,files in os.walk(indir):

    for f in files:

        if not f.endswith(".pdb"):
            continue


        pdb=os.path.join(root,f)

        try:

            # complex
            complex_sasa=calc_sasa(pdb)


            tmp1="/tmp/receptor.pdb"
            tmp2="/tmp/binder.pdb"


            # 默认 A receptor
            # 其他链 binder

            parser=PDBParser(QUIET=True)

            structure=parser.get_structure(
                "x",
                pdb
            )

            chains=[
                c.id
                for c in structure[0]
            ]


            if len(chains)<2:
                continue


            receptor=[chains[0]]

            binder=chains[1:]


            save_chain(
                pdb,
                receptor,
                tmp1
            )

            save_chain(
                pdb,
                binder,
                tmp2
            )


            receptor_sasa=calc_sasa(tmp1)

            binder_sasa=calc_sasa(tmp2)


            bsa=(
                receptor_sasa
                +
                binder_sasa
                -
                complex_sasa
            )


            rows.append([
                f,
                receptor_sasa,
                binder_sasa,
                complex_sasa,
                bsa,
                pdb
            ])


            print("done",f)



        except Exception as e:

            print("fail",f,e)



with open(out,"w",newline="") as fp:

    w=csv.writer(fp)

    w.writerow([
        "file",
        "receptor_SASA",
        "binder_SASA",
        "complex_SASA",
        "BSA",
        "source"
    ])

    w.writerows(rows)



print("saved",out)
print("rows",len(rows))
