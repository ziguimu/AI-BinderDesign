import pandas as pd
import os


conf = pd.read_csv(
    "summaries/05_all_confidence.csv"
)

interface = pd.read_csv(
    "summaries/08_interface_analysis.csv"
)


def find_pdb(row):

    species=row["species"]
    system=row["system"]

    prefix=""

    if species=="human":
        prefix="human_"
    else:
        prefix="mouse_"

    target=prefix+system


    for f in interface["file"]:

        if target.lower() in f.lower():

            return f

    return None



conf["pdb_file"] = conf.apply(
    find_pdb,
    axis=1
)


merged=conf.merge(
    interface,
    left_on="pdb_file",
    right_on="file",
    how="left"
)


out="summaries/09_benchmark_final.csv"

merged.to_csv(
    out,
    index=False
)


print("saved",out)
print("rows",len(merged))
