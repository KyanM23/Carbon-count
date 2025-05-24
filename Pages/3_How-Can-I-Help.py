import streamlit as st

st.set_page_config(page_title="Fight Carbon Emissions", layout="centered")

# --- Header Section ---
st.title("🌍 How Can *You* Help the Fight Against Carbon Emissions?")
st.markdown("""
Welcome! Carbon emissions are one of the leading contributors to climate change.
Small changes in your daily life can make a **big impact**. Let’s explore how you can help.
""")

# --- Section: Lifestyle Changes ---
st.header("🚶‍♀️ Everyday Actions That Matter")
st.markdown("Here are a few powerful steps you can take today:")

actions = [
    "🚴 Switch to biking, walking, or public transport when possible",
    "💡 Use energy-efficient LED bulbs",
    "🛍️ Reduce single-use plastics and packaging",
    "🌱 Eat more plant-based meals",
    "🔌 Unplug electronics when not in use",
    "♻️ Recycle properly and compost organic waste"
]

selected_actions = st.multiselect("Select the actions you're already taking or would like to try:", actions)

if selected_actions:
    st.success(f"You're already thinking green! Great choices: {', '.join(selected_actions)}")

# --- Section: Learn More ---
st.header("📚 Learn & Share")
st.markdown("""
- Educate yourself and others on **carbon footprints**
- Support policies and leaders who prioritize sustainability
- Invest in green technologies or offset your emissions
""")

# --- Section: Interactive Quiz ---
st.header("🧠 Quick Quiz: What's Your Carbon Knowledge?")
with st.expander("Take a 1-minute quiz"):
    q1 = st.radio("Which sector emits the most greenhouse gases globally?", [
        "Transportation", "Industry", "Electricity and heat production", "Agriculture"
    ])
    q2 = st.radio("Which of these helps reduce carbon emissions?", [
        "Driving solo daily", "Installing solar panels", "Using disposable bags", "Eating more red meat"
    ])

    if st.button("Submit Quiz"):
        score = 0
        if q1 == "Electricity and heat production":
            score += 1
        if q2 == "Installing solar panels":
            score += 1

        st.info(f"🎉 You got {score}/2 correct!")
        if score < 2:
            st.write("Great effort! Every bit of learning helps you become a better Earth ally.")

# --- Section: Call to Action ---
st.header("🌱 Join the Movement")
st.markdown("""
Change starts with **awareness and action**. You don't need to be perfect — just consistent.
Share this page, talk about it, and start with one small habit this week.

_“The greatest threat to our planet is the belief that someone else will save it.” – Robert Swan_
""")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")