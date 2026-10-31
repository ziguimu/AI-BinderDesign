import pandas as pd


df=pd.read_csv(
    "summaries/09_benchmark_final.csv"
)


summary=df.groupby(
    [
        "species",
        "system",
        "method"
    ]
).agg(
    mean_pTM=("pTM","mean"),
    mean_ipTM=("ipTM","mean"),
    mean_interface_pLDDT=("interface_pLDDT","mean"),
    mean_interface_pDE=("interface_pDE","mean"),
    mean_interface_residues=("interface_residues","mean"),
    mean_contacts=("contacts","mean"),
    n_models=("model","count")
).reset_index()


summary.to_csv(
    "summaries/10_method_summary.csv",
    index=False
)


print(summary)
print("saved")
