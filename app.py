import streamlit as st

# Page settings
st.set_page_config(
    page_title="Disaster Damage Reporter",
    page_icon="🏚️",
    layout="wide"
)

# Header
st.title("🏚️ Disaster Damage Reporter")
st.write("Report damaged buildings and infrastructure to local authorities.")

# Upload image
uploaded_image = st.file_uploader(
    "Upload a photo of the damage",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

# Report details
location = st.text_input(
    "Location",
    placeholder="Enter address or area"
)

damage_type = st.selectbox(
    "Damage Type",
    [
        "Building Collapse",
        "Cracked Structure",
        "Road Damage",
        "Flood Damage",
        "Fire Damage",
        "Other"
    ]
)

description = st.text_area(
    "Description",
    placeholder="Describe the damage and situation..."
)

severity = st.slider(
    "Severity",
    min_value=1,
    max_value=10,
    value=5
)

# Submit button
if st.button("🚨 Submit Report"):
    if not uploaded_image:
        st.error("Please upload an image before submitting.")
    elif not location:
        st.error("Please enter a location.")
    else:
        st.success("Report captured successfully!")

        st.write("### Report Summary")
        st.write(f"**Location:** {location}")
        st.write(f"**Damage Type:** {damage_type}")
        st.write(f"**Severity:** {severity}/10")
        st.write(f"**Description:** {description}")
