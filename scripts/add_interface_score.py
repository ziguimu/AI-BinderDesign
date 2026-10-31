import pandas as pd


df = pd.read_csv(
    "summaries/09_benchmark_final.csv"
)


def get_score(row):

    if row["method"] == "Boltz":
        return row["ipTM"]

    elif row["method"] == "ColabFold":
        # 从04表补充pDockQ
        return None


df_cf = pd.read_csv(
    "summaries/04_colabfold_confidence.csv"
)


# 建立ColabFold model映射
dockq_map = dict(
    zip(
        df_cf["model"],
        df_cf["pDockQ"]
    )
)


scores=[]


for _,row in df.iterrows():

    if row["method"]=="Boltz":

        scores.append(
            row["ipTM"]
        )

    else:

        scores.append(
            dockq_map.get(
                row["model"],
                None
            )
        )


df["interface_score"]=scores


out="summaries/11_interface_score.csv"

df.to_csv(
    out,
    index=False
)


print("saved",out)
print("rows",len(df))
