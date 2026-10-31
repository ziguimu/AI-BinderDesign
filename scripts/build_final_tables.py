import pandas as pd


# ======================
# 1 raw table
# ======================

raw = pd.read_csv(
    "summaries/11_interface_score.csv"
)

raw.to_csv(
    "summaries/FINAL_raw_benchmark.csv",
    index=False
)


# ======================
# 2 mean statistics
# ======================

method = pd.read_csv(
    "summaries/10_method_summary.csv"
)

score = pd.read_csv(
    "summaries/12_interface_score_summary.csv"
)


mean = method.merge(
    score,
    on=[
        "species",
        "system",
        "method"
    ],
    how="left"
)


mean.to_csv(
    "summaries/FINAL_mean_statistics.csv",
    index=False
)


# ======================
# 3 threshold table
# ======================

threshold = pd.DataFrame({

"metric":[
"pTM",
"ipTM",
"interface_score",
"interface_residues",
"contacts",
"interface_pLDDT"
],

"benchmark_range":[
"0.63-0.96",
"0.20-0.95",
"0.12-0.95",
"29-126",
"508-2726",
"83-98"
],

"minimum_candidate":[
">=0.65",
">=0.30",
">=0.40",
">=30",
">=500",
">=80"
],

"high_confidence":[
">=0.85",
">=0.75",
">=0.75",
">=50",
">=800",
">=90"
],

"description":[
"global fold confidence",
"interface confidence",
"unified interface score",
"number of interacting residues",
"atomic contacts",
"interface local confidence"
]

})


threshold.to_csv(
    "summaries/FINAL_threshold_criteria.csv",
    index=False
)


print("DONE")
print("raw rows:",len(raw))
print("mean rows:",len(mean))
print("threshold rows:",len(threshold))
