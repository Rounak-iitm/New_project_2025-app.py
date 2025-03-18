import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.DataFrame({
    "Employee_ID": [1, 2, 3, 4],
    "Name": ["Alice Smith", "Bob Johnson", "Charlie Rose", "David Brown"],
    "Department": ["Sales", "Production", "HR", "IT"],
    "Sales": [5000, 3000, 2000, 4000],
    "Region": ["North", "South", "East", "West"],
    "Image": ["https://via.placeholder.com/100",
              "https://via.placeholder.com/100",
              "https://via.placeholder.com/100",
              "https://via.placeholder.com/100"]
})

# Title and Sidebar
st.title("Employee Dashboard")
st.sidebar.title("Filters")

# Sidebar filters
selected_department = st.sidebar.multiselect("Select Department", options=df["Department"].unique(), default=df["Department"].unique())
selected_region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())

# Filter data based on selections
filtered_df = df[(df["Department"].isin(selected_department)) & (df["Region"].isin(selected_region))]

# Display filtered data
st.write("Filtered Data:")
st.dataframe(filtered_df)

# Pie Chart: Sales by Department
st.subheader("Sales Distribution by Department")
fig1, ax1 = plt.subplots()
colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33"]
filtered_df.groupby("Department")["Sales"].sum().plot.pie(autopct="%1.1f%%", colors=colors, ax=ax1)
ax1.set_ylabel("")
ax1.set_facecolor("black")
ax1.title.set_color("white")
st.pyplot(fig1)

# Bar Chart: Total Sales by Region
st.subheader("Total Sales by Region")
fig2, ax2 = plt.subplots()
sns.barplot(x="Region", y="Sales", data=filtered_df, palette="viridis", ax=ax2)
ax2.set_facecolor("black")
ax2.title.set_color("white")
ax2.xaxis.label.set_color("white")
ax2.yaxis.label.set_color("white")
ax2.tick_params(colors="white")
st.pyplot(fig2)

# Display Employee Images
st.subheader("Employee Images")
for _, row in filtered_df.iterrows():
    st.image(row["Image"], caption=f"{row['Name']} ({row['Department']})", width=100)
