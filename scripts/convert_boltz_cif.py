import os
import glob
import csv
from Bio.PDB import MMCIFParser, PDBIO


outdir = "analysis_structures/Boltz"
os.makedirs(outdir, exist_ok=True)

files = (
    glob.glob("prediction_controls/Boltz/**/*.cif", recursive=True)
    +
    glob.glob("prediction_controls_mouse/Boltz/**/*.cif", recursive=True)
)

rows=[]

for cif in sorted(files):

    parser = MMCIFParser(QUIET=True)

    structure = parser.get_structure(
        "boltz",
        cif
    )

    if "mouse" in cif:
        species="mouse"
    else:
        species="human"


    if "7D12" in cif or "7d12" in cif:
        system="7D12"
    elif "cetuximab" in cif:
        system="cetuximab"
    elif "EGF" in cif:
        system="EGF"
    else:
        system="unknown"


    if "repeat_" in cif:

        repeat=cif.split("repeat_")[1].split("/")[0]
        tag=f"{species}_{system}_repeat{repeat}"

    elif "/result/" in cif:

        tag=f"{species}_{system}_result"

    else:

        name=os.path.basename(cif).replace(".cif","")
        model=name.split("model_")[-1]
        tag=f"{species}_{system}_model{model}"


    outfile=os.path.join(
        outdir,
        tag+".pdb"
    )


    io=PDBIO()
    io.set_structure(structure)
    io.save(outfile)


    rows.append([
        outfile,
        species,
        system,
        "Boltz",
        cif
    ])


with open(
    "analysis_structures/Boltz_manifest.csv",
    "w",
    newline=""
) as f:

    writer=csv.writer(f)

    writer.writerow([
        "file",
        "species",
        "system",
        "method",
        "source"
    ])

    writer.writerows(rows)


print("Converted:",len(rows))
