import pandas as pd


raw=pd.read_csv(
"summaries/11_interface_score.csv"
)

bsa=pd.read_csv(
"summaries/14_BSA_real.csv"
)

chem=pd.read_csv(
"summaries/15_interface_chemistry.csv"
)


# 合并BSA
raw=raw.merge(
    bsa,
    left_on="pdb_file",
    right_on="file",
    how="left"
)


# 合并化学
raw=raw.merge(
    chem,
    left_on="pdb_file",
    right_on="file",
    how="left",
    suffixes=("","_chem")
)


raw.to_csv(
"summaries/FINAL_complete_raw.csv",
index=False
)


# 平均统计

group_cols=[
"species",
"system",
"method"
]


numeric=[
"pTM",
"ipTM",
"interface_pLDDT",
"interface_score",
"BSA",
"contacts",
"interface_residues"
]


mean=raw.groupby(group_cols)[numeric].mean().reset_index()


mean.to_csv(
"summaries/FINAL_complete_statistics.csv",
index=False
)


print("raw",len(raw))
print("mean",len(mean))


# 阈值

thresholds=pd.DataFrame({

"metric":[
"ipTM",
"pTM",
"interface_score",
"interface_pLDDT",
"BSA",
"contacts",
"interface_residues"
],

"recommended_cutoff":[
0.75,
0.80,
0.70,
85,
1000,
700,
30
],

"basis":[
"strong binder controls",
"fold confidence",
"interface confidence",
"AF confidence",
"typical protein binder interface",
"stable interface",
"minimum interface size"
]

})


thresholds.to_csv(
"summaries/FINAL_binder_thresholds.csv",
index=False
)


print("DONE")
