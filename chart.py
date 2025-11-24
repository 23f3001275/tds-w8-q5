# ------------------------------
# Customer Analytics Boxplot Visualization
# Author: 23f3001275@ds.study.iitm.ac.in
# Purpose: Boxplot of Purchase Amounts by Customer Segment
# ------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1) ----- Generate synthetic business data -----
np.random.seed(42)

segments = ["Budget", "Standard", "Premium", "Luxury"]

data = {
    "Segment": np.random.choice(segments, 500, p=[0.35, 0.40, 0.18, 0.07]),
    "Purchase_Amount": np.concatenate([
        np.random.normal(40, 10, 175),    # Budget buyers
        np.random.normal(80, 20, 200),    # Standard buyers
        np.random.normal(160, 35, 90),    # Premium buyers
        np.random.normal(350, 80, 35)     # Luxury buyers
    ])
}

df = pd.DataFrame(data)

# 2) ----- Professional Seaborn styling -----
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("viridis", n_colors=len(segments))  # match segment length

# 3) ----- Create the boxplot -----
plt.figure(figsize=(5.12, 5.12))   # 512px * 512px @100dpi

sns.boxplot(
    data=df,
    x="Segment",
    y="Purchase_Amount",
    hue="Segment",          # remove warning by setting hue
    palette=palette,
    dodge=False,            # ensure one box per segment
    legend=False            # hide legend since x and hue are same
)

# ----- Titles and labels with sufficient padding -----
plt.title("Purchase Amount Distribution by Customer Segment",
          fontsize=14, fontweight="bold", pad=20)
plt.xlabel("Customer Segment", labelpad=12)
plt.ylabel("Purchase Amount ($)", labelpad=12)

plt.tight_layout()  # prevent truncation

# 4) ----- Save EXACT 512x512 image -----
plt.savefig("chart.png", dpi=100)  # 5.12 in * 100 dpi = 512px exactly
plt.close()
