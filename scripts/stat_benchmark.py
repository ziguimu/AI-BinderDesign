import pandas as pd


inp = "summaries/05_all_confidence.csv"
out = "summaries/06_benchmark_statistics.csv"


df = pd.read_csv(inp)


# 分组统计
result = df.groupby(
    [
        "species",
        "system",
        "method"
    ]
).agg(
    n_models=("model", "count"),

    mean_pTM=("pTM", "mean"),
    std_pTM=("pTM", "std"),

    mean_ipTM=("ipTM", "mean"),
    std_ipTM=("ipTM", "std"),

    mean_complex_pLDDT=("complex_pLDDT", "mean"),
    std_complex_pLDDT=("complex_pLDDT", "std"),

    mean_interface_pLDDT=("interface_pLDDT", "mean"),
    std_interface_pLDDT=("interface_pLDDT", "std"),

    mean_interface_pDE=("interface_pDE", "mean"),
    std_interface_pDE=("interface_pDE", "std")

).reset_index()


result.to_csv(
    out,
    index=False
)

print("saved:", out)
print("rows:", len(result))
