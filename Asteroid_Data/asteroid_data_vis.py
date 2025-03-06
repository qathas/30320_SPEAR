import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the asteroid data
df = pd.read_csv("asteroids_full_data.csv")

# Set style for seaborn
sns.set_style("darkgrid")

# 🔹 1. Histogram: Asteroid Diameter Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["diameter"], bins=30, kde=True, color="skyblue")
plt.xlabel("Diameter (m)")
plt.ylabel("Count")
plt.title("Distribution of Asteroid Diameters (25m-250m)")
plt.show()

# 🔹 2. Histogram: Absolute Magnitude (Brightness)
plt.figure(figsize=(8,5))
sns.histplot(df["absolute_magnitude"], bins=30, kde=True, color="orange")
plt.xlabel("Absolute Magnitude (H)")
plt.ylabel("Count")
plt.title("Distribution of Absolute Magnitudes")
plt.show()

# 🔹 3. Pie Chart: Potentially Hazardous vs. Non-Hazardous
plt.figure(figsize=(6,6))
df["is_potentially_hazardous"].value_counts().plot.pie(autopct="%1.1f%%", colors=["green", "red"])
plt.title("Percentage of Potentially Hazardous Asteroids")
plt.ylabel("")  # Hide y-label for clarity
plt.show()

# 🔹 4. Histogram: Eccentricity Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["eccentricity"].dropna(), bins=30, kde=True, color="purple")
plt.xlabel("Eccentricity")
plt.ylabel("Count")
plt.title("Distribution of Orbital Eccentricities")
plt.show()

# 🔹 5. Scatter Plot: Semi-Major Axis vs. Diameter
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["semi_major_axis"], y=df["diameter"], alpha=0.5, color="blue")
plt.xlabel("Semi-Major Axis (AU)")
plt.ylabel("Diameter (m)")
plt.title("Asteroid Size vs. Distance from Sun")
plt.show()

# 🔹 6. Histogram: Orbital Inclination
plt.figure(figsize=(8,5))
sns.histplot(df["inclination"].dropna(), bins=30, kde=True, color="red")
plt.xlabel("Inclination (°)")
plt.ylabel("Count")
plt.title("Distribution of Orbital Inclinations")
plt.show()
