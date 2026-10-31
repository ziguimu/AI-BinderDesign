import pandas as pd


df=pd.read_csv(
    "summaries/11_interface_score.csv"
)


summary=df.groupby(
    [
        "species",
        "system",
        "method"
    ]
).agg(
    mean_interface_score=(
        "interface_score",
        "mean"
    ),
    std_interface_score=(
        "interface_score",
        "std"
    ),
    n_models=(
        "interface_score",
        "count"
    )
).reset_index()


summary.to_csv(
    "summaries/12_interface_score_summary.csv",
    index=False
)


print(summary)
print("saved")
