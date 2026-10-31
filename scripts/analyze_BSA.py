import os
import csv
import freesasa


indir = "analysis_structures"
out = "summaries/13_BSA_analysis.csv"


rows = []


for root, dirs, files in os.walk(indir):

    for f in files:

        if not f.endswith(".pdb"):
            continue

        path = os.path.join(root, f)

        try:

            structure = freesasa.Structure(path)

            result = freesasa.calc(structure)

            sasa = result.totalArea()

            rows.append([
                f,
                sasa,
                path
            ])

            print("done", f)


        except Exception as e:

            print("fail", f, e)



with open(out, "w", newline="") as fp:

    writer = csv.writer(fp)

    writer.writerow([
        "file",
        "complex_SASA",
        "source"
    ])

    writer.writerows(rows)


print("saved", out)
print("rows", len(rows))
