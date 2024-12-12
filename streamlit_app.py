import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
st.set_page_config(layout="wide")
# Set the title of the app
st.title("File Upload Example")

# Add file uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    # Read and display the content of the uploaded Python file
    file_content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", file_content, height=300)

if uploaded_file is not None:
    # Save the uploaded file to the local directory
    with open(f"uploaded_file.py", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File saved successfully!")

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Set up the Streamlit app title
st.title("Interactive Animated Scatter Plot: Ad Click Analysis")

# Simulate Data Preparation (based on your dataset)
# Example: Animate data over "Timestamp" for better insights
n_points = 50  # Number of data points to simulate
frames = 10  # Number of animation frames
data = {
    "Daily Time Spent on Site": np.random.uniform(50, 70, n_points),
    "Income": np.random.uniform(40000, 60000, n_points),
    "Age": np.random.randint(18, 60, size=n_points),
    "Clicked on Ad": np.random.choice([0, 1], n_points),
    "frame": np.random.randint(0, frames, size=n_points),
}

# Create a DataFrame from simulated data
df = pd.DataFrame(data)

# Use Plotly Express to create an animated scatter plot
fig = px.scatter(
    df,
    x="Daily Time Spent on Site",
    y="Income",
    size="Age",  # Bubble size corresponds to age
    color="Clicked on Ad",  # Different colors for clicked/not clicked
    animation_frame="frame",  # Animation frames
    title="Ad Interaction Based on Site Usage and Income",
    labels={
        "Daily Time Spent on Site": "Time Spent (minutes)",
        "Income": "Income ($)",
    },
)

# Display the animation in Streamlit
st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import numpy as np
import time

# Set up the Streamlit app title
st.title("Real-Time Line Chart: Age vs. Daily Internet Usage")

# Sidebar widgets
progress_bar = st.sidebar.progress(0)  # Progress bar
status_text = st.sidebar.empty()  # Empty widget for text updates

# Load your dataset (replace with actual data loading if file is available)
# Simulated data for demonstration
n_points = 100  # Total data points
data = {
    "Age": np.random.randint(18, 60, size=n_points),
    "Daily Internet Usage": np.random.uniform(100, 300, size=n_points),
}
df = pd.DataFrame(data)

# Initialize the chart with the first row
initial_data = df.iloc[:1]
chart = st.line_chart(initial_data.set_index("Age"))

# Update the chart row by row with a progress bar
for i in range(1, len(df)):
    new_row = df.iloc[i : i + 1]  # Get the next row
    chart.add_rows(new_row.set_index("Age"))  # Update the chart
    status_text.text(f"{i}/{len(df)} Rows Processed")  # Update status
    progress_bar.progress(i / len(df))  # Update progress bar
    time.sleep(0.05)  # Simulate processing delay

# Clear the progress bar
progress_bar.empty()

# Add a rerun button
st.button("Re-run")


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load or simulate a dataset
# For demonstration, let's generate a synthetic dataset
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "Daily Time Spent on Site": np.random.uniform(30, 120, n_samples),
    "Age": np.random.randint(18, 70, n_samples),
    "Income": np.random.randint(20000, 150000, n_samples),
    "Daily Internet Usage": np.random.uniform(50, 300, n_samples),
    "Ad Topic Line": [f"Ad Line {i}" for i in range(n_samples)],
    "Male": np.random.choice([0, 1], n_samples),
    "Country": np.random.choice(["USA", "UK", "India", "Germany", "France"], n_samples),
    "Timestamp": pd.date_range("2023-01-01", periods=n_samples, freq="H"),
    "Clicked on Ad": np.random.choice([0, 1], n_samples)
})

# Sidebar sliders and filters
st.sidebar.title("Filter Options")
age_filter = st.sidebar.slider("Age Range", 18, 70, (18, 70))
income_filter = st.sidebar.slider("Income Range", 20000, 150000, (20000, 150000))
time_spent_filter = st.sidebar.slider("Daily Time Spent on Site", 30, 120, (30, 120))
internet_usage_filter = st.sidebar.slider("Daily Internet Usage", 50, 300, (50, 300))

# Filter dataset
filtered_data = data[
    (data["Age"] >= age_filter[0]) & (data["Age"] <= age_filter[1]) &
    (data["Income"] >= income_filter[0]) & (data["Income"] <= income_filter[1]) &
    (data["Daily Time Spent on Site"] >= time_spent_filter[0]) & (data["Daily Time Spent on Site"] <= time_spent_filter[1]) &
    (data["Daily Internet Usage"] >= internet_usage_filter[0]) & (data["Daily Internet Usage"] <= internet_usage_filter[1])
]

# Display filtered data
st.title("Filtered Data")
st.dataframe(filtered_data)

# Display summary stats
st.sidebar.subheader("Summary Statistics")
st.sidebar.text(f"Total Entries: {len(filtered_data)}")

# Interactive plots
st.title("Visualizations")

# Plot 1: Histogram of Age
st.subheader("Age Distribution")
fig, ax = plt.subplots()
ax.hist(filtered_data["Age"], bins=15, color="skyblue", edgecolor="black")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
ax.set_title("Age Distribution")
st.pyplot(fig)

# Plot 2: Scatterplot of Daily Time Spent on Site vs Income
st.subheader("Daily Time Spent on Site vs Income")
fig, ax = plt.subplots()
scatter = ax.scatter(
    filtered_data["Daily Time Spent on Site"],
    filtered_data["Income"],
    c=filtered_data["Clicked on Ad"],
    cmap="coolwarm",
    alpha=0.7
)
ax.set_xlabel("Daily Time Spent on Site")
ax.set_ylabel("Income")
ax.set_title("Daily Time Spent on Site vs Income")
legend1 = ax.legend(*scatter.legend_elements(), title="Clicked on Ad")
ax.add_artist(legend1)
st.pyplot(fig)

# Plot 3: Count of Clicked on Ad by Gender
st.subheader("Clicked on Ad by Gender")
gender_counts = filtered_data.groupby("Male")["Clicked on Ad"].value_counts().unstack().fillna(0)
fig, ax = plt.subplots()
gender_counts.plot(kind="bar", stacked=True, ax=ax, color=["salmon", "lightgreen"])
ax.set_xlabel("Gender (0 = Female, 1 = Male)")
ax.set_ylabel("Count")
ax.set_title("Clicked on Ad by Gender")
st.pyplot(fig)

# Add unique keys to buttons
st.button("Re-run", key="rerun_button_main")




import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from io import BytesIO
from matplotlib.animation import PillowWriter
import tempfile
import os

# Simulated Dataset
np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "Daily Time Spent on Site": np.random.uniform(30, 120, n_samples),
    "Age": np.random.randint(18, 70, n_samples),
    "Income": np.random.randint(20000, 150000, n_samples),
    "Daily Internet Usage": np.random.uniform(50, 300, n_samples),
    "Ad Topic Line": [f"Ad Line {i}" for i in range(n_samples)],
    "Male": np.random.choice([0, 1], n_samples),
    "Country": np.random.choice(["USA", "UK", "India", "Germany", "France"], n_samples),
    "Timestamp": pd.date_range("2023-01-01", periods=n_samples, freq="H"),
    "Clicked on Ad": np.random.choice([0, 1], n_samples)
})

# Streamlit UI with organized sidebar
st.title("Motion Visualization: Trends Over Time")
st.sidebar.header("Animation Settings")

# Filter by country selection
st.sidebar.subheader("Select Country")
selected_country = st.sidebar.selectbox("Choose Country", options=data["Country"].unique())

# Animation settings
st.sidebar.subheader("Select Animation Parameters")
max_frames = st.sidebar.slider("Number of Frames", min_value=10, max_value=100, value=50)

# Filter dataset based on country selection
filtered_data = data[data["Country"] == selected_country]
filtered_data = filtered_data[filtered_data["Clicked on Ad"] == 1].sort_values(by="Timestamp")

# Prepare data for animation
time_steps = filtered_data["Timestamp"].unique()[:max_frames]
grouped_data = filtered_data.groupby("Timestamp")[["Daily Time Spent on Site", "Daily Internet Usage"]].mean()

# Create Animation
fig, ax = plt.subplots(figsize=(10, 6))
x_data, y1_data, y2_data = [], [], []

def animate(frame):
    ax.clear()
    current_time = time_steps[frame]
    x_data.append(current_time)
    y1_data.append(grouped_data.loc[current_time, "Daily Time Spent on Site"])
    y2_data.append(grouped_data.loc[current_time, "Daily Internet Usage"])

    ax.plot(x_data, y1_data, label="Daily Time Spent on Site", color="blue", marker="o")
    ax.plot(x_data, y2_data, label="Daily Internet Usage", color="green", marker="o")

    ax.set_title("Dynamic Trends Over Time", fontsize=16)
    ax.set_xlabel("Timestamp", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.legend(loc="upper left")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True)

ani = FuncAnimation(fig, animate, frames=len(time_steps), interval=200)

# Create a temporary file for the animation
with tempfile.NamedTemporaryFile(delete=False, suffix='.gif') as tmp_file:
    tmp_path = tmp_file.name
    writer = PillowWriter(fps=10)
    ani.save(tmp_path, writer=writer)

# Display the animation in Streamlit
st.image(tmp_path, caption="Trends of Daily Time Spent on Site and Internet Usage Over Time")

# Optionally, clean up the temporary file after use
os.remove(tmp_path)



# MAP 
import folium
import streamlit as st
import pandas as pd
import requests

# Example dataset with country and additional data (Replace this with your full dataset)
data = {
    "Country": [
        "Zimbabwe", "Vietnam", "USA", "Uruguay", "Turkey", "Thailand", 
        "Spain", "South Africa", "Singapore", "Russia", "Portugal", 
        "Pakistan", "Netherlands", "Mexico", "Malaysia", "Japan", "Germany", "France", "Egypt", "Croatia", "China"
    ],
    "Clicked on Ad": [
        5, 10, 150, 20, 35, 45, 60, 30, 80, 95, 70, 
        30, 55, 45, 50, 200, 150, 300, 120, 65, 100
    ]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Load GeoJSON data (for world countries boundaries)
geo_url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
geo_data = requests.get(geo_url).json()

# Merge your data with the GeoJSON based on 'Country' column
# This assumes the country names in your DataFrame match those in the GeoJSON file

# Create a folium map centered around the world
m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")

# Add the choropleth layer to the map
folium.Choropleth(
    geo_data=geo_data,
    name="choropleth",
    data=df,
    columns=["Country", "Clicked on Ad"],  # Map 'Clicked on Ad' to visualize on the map
    key_on="feature.properties.name",  # Match the 'name' property in GeoJSON with the 'Country' in DataFrame
    fill_color="YlGnBu",  # Color scale (you can change it)
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Total Clicks on Ads by Country"
).add_to(m)

# Optional: Add GeoJSON features for additional customization
folium.features.GeoJson(
    geo_data,
    name="geojson"
).add_to(m)

# Add layer control to toggle layers (optional)
folium.LayerControl().add_to(m)

# Save the map to an HTML file
map_html = "choropleth_map_with_clicks.html"
m.save(map_html)

# Display the map in Streamlit
st.title("Choropleth Map of Clicks on Ads by Country")
st.markdown("This map visualizes the total number of clicks on ads by country using Folium and Streamlit.")
st.components.v1.html(open(map_html, "r").read(), height=600)
