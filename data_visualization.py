import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file read karna
df = pd.read_csv("sales_data.csv")

# Data print karna
print(df)

# Style set karna
sns.set_style("whitegrid")

# Graph size
plt.figure(figsize=(10,6))

# Sales graph
sns.lineplot(
    x="Month",
    y="Sales",
    data=df,
    marker="o",
    label="Sales"
)

# Profit graph
sns.lineplot(
    x="Month",
    y="Profit",
    data=df,
    marker="o",
    label="Profit"
)

# Title
plt.title("Monthly Sales and Profit Analysis")

# Axis names
plt.xlabel("Month")
plt.ylabel("Amount")

# Month names rotate
plt.xticks(rotation=45)

# Layout
plt.tight_layout()

# Image save
plt.savefig("sales_analysis.png")

# Show graph
plt.show()