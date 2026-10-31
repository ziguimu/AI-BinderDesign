import pandas as pd


boltz=pd.read_csv(
    "summaries/02_boltz_confidence_correct.csv"
)

colab=pd.read_csv(
    "summaries/04_colabfold_confidence.csv"
)


boltz["model"] = (
    boltz["source"]
    .str.split("/")
    .str[-1]
    .str.replace(".json","")
)


boltz["method"]="Boltz"


# 统一列
boltz_out=boltz[
[
"species",
"system",
"method",
"model",
"pTM",
"ipTM",
"complex_pLDDT",
"interface_pLDDT",
"complex_pDE",
"interface_pDE",
"source"
]
]


colab["complex_pLDDT"]=""
colab["interface_pLDDT"]=""
colab["complex_pDE"]=""
colab["interface_pDE"]=""


colab_out=colab[
[
"species",
"system",
"method",
"model",
"pTM",
"ipTM",
"complex_pLDDT",
"interface_pLDDT",
"complex_pDE",
"interface_pDE",
"source"
]
]


all=pd.concat(
[
boltz_out,
colab_out
],
ignore_index=True
)


all.to_csv(
"summaries/05_all_confidence.csv",
index=False
)


print(
"done",
len(all)
)
