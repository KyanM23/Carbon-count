import streamlit as st
import wikipedia

st.title("How the Calculator Works")

st.markdown('<div class = "button-container">', unsafe_allow_html = True)
if st.button("Home Page"):
    st.switch_page("CarbonCount.py")
st.markdown('</div>', unsafe_allow_html = True)

st.text("Our calculator uses nationally recognized data from the United States Environmental Protection Agency to calculate average "
"emissions from vehicles. \n \n \n For cars: the number of miles is multipled by ~411 \n For buses: the number of miles is multipled by ~290 \n"
"For trains: the number of miles is multipled by ~180 \n When walking or running, your carbon output is essentially zero. \n "
"For planes: the number of miles is multipled by ~24,176")

st.divider()

st.subheader("How Do We Find Your Distance? \n \n")

st.text("Using the two location points you select, we find the latitude and longitude coordinates and find the distance using a method called the Haversine Formula.")

st.subheader("Haversine Formula")

try:
    summary = wikipedia.summary("Haversine_formula", sentences=2)
    st.markdown(f"> \"{summary}\"")  # Display in blockquote (quotation format)
    st.markdown(f"[Read more on Wikipedia](https://en.wikipedia.org/wiki/Haversine_formula)")
except:
    st.error("Couldn't fetch Wikipedia content. Click [here](https://en.wikipedia.org/wiki/Haversine_formula).")

col1, col2 = st.columns(2)
with col1:
    st.image("download.png", caption="Haversine Formula Visualization", use_container_width=True)
with col2:
    st.image("image.png", caption="Haversine Distance Equation", use_container_width=True)

st.text("Image source: Wikipedia - Haversine formula")

st.divider()




