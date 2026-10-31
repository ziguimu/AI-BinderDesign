import pandas as pd


inp="summaries/05_all_confidence.csv"
out="summaries/07_best_models.csv"


df=pd.read_csv(inp)


rows=[]


for (species,system,method),group in df.groupby(
    ["species","system","method"]
):

    # ipTM最高
    best_iptm=group.sort_values(
        "ipTM",
        ascending=False
    ).iloc[0]


    # pTM最高
    best_ptm=group.sort_values(
        "pTM",
        ascending=False
    ).iloc[0]


    rows.append([
        species,
        system,
        method,
        "best_ipTM",
        best_iptm["model"],
        best_iptm["ipTM"],
        best_iptm["pTM"],
        best_iptm["source"]
    ])


    rows.append([
        species,
        system,
        method,
        "best_pTM",
        best_ptm["model"],
        best_ptm["ipTM"],
        best_ptm["pTM"],
        best_ptm["source"]
    ])


result=pd.DataFrame(
    rows,
    columns=[
        "species",
        "system",
        "method",
        "criterion",
        "model",
        "ipTM",
        "pTM",
        "source"
    ]
)


result.to_csv(
    out,
    index=False
)


print("saved",out)
print("rows",len(result))
