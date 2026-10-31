import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(
    "summaries/05_all_confidence.csv"
)


plt.figure(figsize=(8,5))


data=[
    df[df.method=="Boltz"]["ipTM"],
    df[df.method=="ColabFold"]["ipTM"]
]


plt.boxplot(
    data,
    tick_labels=[
        "Boltz",
        "ColabFold"
    ]
)


plt.ylabel("ipTM")

plt.title(
    "Interface confidence comparison"
)


plt.tight_layout()

plt.savefig(
    "summaries/ipTM_Boltz_vs_ColabFold.png",
    dpi=300
)

print("saved")
