import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# Streamlit UI
st.title("Interactive Distance Calculator")

st.write("Click on two points on the map: Start and End. The app will calculate the real-world distance.")

# Initialize session state for start & end points
if "points" not in st.session_state:
    st.session_state.points = []

# Create a Folium map centered at a default location
m = folium.Map(location=[37.7749, -122.4194], zoom_start=5)  # San Francisco as default

# Function to add markers dynamically
for point in st.session_state.points:
    folium.Marker(location=point, popup=f"Point: {point}").add_to(m)

# Capture user click event
map_data = st_folium(m, height=500, width=700)

# Process user clicks
if map_data and map_data["last_clicked"]:
    lat, lon = map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"]
    
    # Add the new point if we have less than 2 stored
    if len(st.session_state.points) < 2:
        st.session_state.points.append([lat, lon])

# Display selected points
if len(st.session_state.points) == 2:
    start, end = st.session_state.points

    st.write(f"**Start:** {start}")
    st.write(f"**End:** {end}")

    # Calculate real-world distance (Haversine formula)
    distance = geodesic(start, end).kilometers
    st.write(f"**Approximate Distance:** {distance:.2f} km")

    # Reset button
    if st.button("Reset"):
        st.session_state.points = []