
import streamlit as st

import streamlit as st

# Function to display treatment information for each injury
def show_treatment(injury):
    st.write(f"**Treatment for {injury}:**")
    st.image(get_image_url(injury), caption=f"Image of {injury}")
    if injury == "Burns":
        st.write("1. Remove the heat source.")
        st.write("2. Cool the burn with cool or lukewarm running water for 20 minutes.")
        st.write("3. Cover the burn with a sterile dressing.")
    elif injury == "Cuts and Scrapes":
        st.write("1. Clean the wound with soap and water.")
        st.write("2. Apply an antibiotic ointment.")
        st.write("3. Cover with a sterile bandage.")
    elif injury == "Sprains and Strains":
        st.write("1. Rest the injured area.")
        st.write("2. Ice the area to reduce swelling.")
        st.write("3. Compress the area with a bandage.")
        st.write("4. Elevate the injured area.")
    elif injury == "Snake Bite":
        st.write("1. Keep the person calm and still.")
        st.write("2. Keep the bitten area at or slightly below the level of the heart.")
        st.write("3. Wash the bite with soap and water.")
        st.write("4. Get medical help immediately.")
    elif injury == "Heart Attack":
        st.write("1. Call emergency services (911).")
        st.write("2. Chew and swallow aspirin if not allergic.")
        st.write("3. Begin CPR if the person is unconscious.")
        st.write("4. Hand position: Two hands centered on the chest.") 
        st.write("5. Body position: Shoulders directly over hands; elbows locked.")
        st.write("6. Depth: At least 2 inches.")
        st.write("7. Rate: 100 to 120 per minute.")
        st.write("8. Allow chest to return to normal position after each compression.")
    elif injury == "Head Injury":
        st.write("1. Apply pressure to stop any bleeding.")
        st.write("2. Keep the person still and calm.")
        st.write("3. Apply ice to reduce swelling.")
        st.write("4. Seek medical attention immediately.")
    elif injury == "Broken or Fractured Bone":
        st.write("1. Immobilize the injured area.")
        st.write("2. Apply ice to reduce swelling.")
        st.write("3. Elevate the injured area.")
        st.write("4. Seek medical attention immediately.")
    elif injury == "Severe Bleeding":
        st.write("1. Apply direct pressure to the wound.")
        st.write("2. Elevate the wound above the heart.")
        st.write("3. Apply pressure to pressure points if bleeding doesn't stop.")
        st.write("4. Seek medical help immediately.")
    elif injury == "Fainting":
        st.write("1. Lay the person flat and raise their legs.")
        st.write("2. Check their airway and breathing.")
        st.write("3. Loosen any tight clothing.")
        st.write("4. When they regain consciousness, help them sit up slowly.")

# Function to get image URL based on the injury
def get_image_url(injury):
    image_urls = {
        "Burns": "https://i.pinimg.com/736x/d5/f6/1d/d5f61d3c7551c12dcbe5921ca8ed3b11.jpg",
        "Cuts and Scrapes": "https://my.clevelandclinic.org/-/scassets/images/org/health/articles/25079-abrasion",
        "Sprains and Strains": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgdmwzkZyJjbWNG8jvkz-La2A2DHYgtRKMYfpIGd6xNQ&s",
        "Snake Bite": "https://jssuni.edu.in/jssaher/cpm-pic/picjsscp/images/snake-bite-diffrences.jpg",
        "Heart Attack": "https://www.asterhospitals.in/sites/default/files/2021-09/Dashboard_952_heartattack_9_20.jpg",
        "Head Injury": "https://cdn.vectorstock.com/i/1000v/96/49/head-injury-vector-46779649.jpg",
        "Broken or Fractured Bone": "https://media.istockphoto.com/id/692165588/photo/man-massaging-painful-wrist-on-a-white-background-pain-concept.jpg?s=612x612&w=0&k=20&c=uOa1TCKpKwx3Q52e1Zg27h_cH10jJSiKCGM0l6dcMKY=",
        "Severe Bleeding": "https://www.baptisthealthsystem.com/images/global/newsroom-ccb/infographics/when-does-bleeding-need-emergency-care/bleeding-er-care-02.jpg",
        "Fainting": "https://t3.ftcdn.net/jpg/05/80/22/36/360_F_580223666_d1y8aLXkS5DbQWrM8jNtskmb5w1WeWh8.jpg"
    }
    return image_urls.get(injury, "")

# App Title
st.title("First Aid Help App")
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            color: #ffffff;
            text-shadow: 2px 2px #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display buttons for different types of injuries side by side
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Burns", key="Burns"):
        show_treatment("Burns")

with col2:
    if st.button("Cuts and Scrapes", key="Cuts and Scrapes"):
        show_treatment("Cuts and Scrapes")

with col3:
    if st.button("Sprains and Strains", key="Sprains and Strains"):
        show_treatment("Sprains and Strains")

with col1:
    if st.button("Snake Bite", key="Snake Bite"):
        show_treatment("Snake Bite")

with col2:
    if st.button("Heart Attack", key="Heart Attack"):
        show_treatment("Heart Attack")

with col3:
    if st.button("Head Injury", key="Head Injury"):
        show_treatment("Head Injury")

with col1:
    if st.button("Broken or Fractured Bone", key="Broken or Fractured Bone"):
        show_treatment("Broken or Fractured Bone")

with col2:
    if st.button("Severe Bleeding", key="Severe Bleeding"):
        show_treatment("Severe Bleeding")

with col3:
    if st.button("Fainting", key="Fainting"):
        show_treatment("Fainting")

# Clear button to clear all selections
if st.button("Clear All", key="Clear"):
    st.experimental_rerun()

# Apply gradient background color
st.markdown(
    """
    <style>
        body {
            background-color: #4e54c8;
            background-image: linear-gradient(315deg, #4e54c8 0%, #8f94fb 74%);
        }
        .stButton>button {
            background-color: #ffa500;
            color: #ffffff;
        }
        .stButton>button:hover {
            background-color: #ff6347;
        }
    </style>
    """,
    unsafe_allow_html=True
)
