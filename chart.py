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
palette = sns.color_palette("viridis")

# 3) ----- Create the boxplot -----
plt.figure(figsize=(5.12, 5.12))   # 5.12 inches * 100 dpi = 512 pixels
sns.boxplot(data=df, x="Segment", y="Purchase_Amount", palette=palette)

plt.title("Purchase Amount Distribution by Customer Segment", fontsize=16, fontweight="bold")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# 4) ----- Save EXACT 512x512 image -----
plt.savefig("chart.png", dpi=100)  # 5.12 in * 100 dpi = EXACT 512 px
plt.close()
