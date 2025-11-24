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
np.random.seed(42)  # ensures reproducibility

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
sns.set_context("talk")  # presentation-level text scaling
palette = sns.color_palette("viridis")

# 3) ----- Create the boxplot -----
plt.figure(figsize=(8, 8))   # ensures 512x512 after dpi scaling
sns.boxplot(data=df, x="Segment", y="Purchase_Amount", palette=palette)

plt.title("Purchase Amount Distribution by Customer Segment", fontsize=16, fontweight="bold")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# 4) ----- Save chart EXACTLY 512 x 512 px -----
# dpi=64 → 8 inches * 64 dpi = 512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

plt.close()


