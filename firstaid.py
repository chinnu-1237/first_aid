pip install streamlit
import streamlit as st

def show_treatment(injury):
    if injury == "Burns":
        st.write("Treatment for Burns:")
        st.image("https://i.pinimg.com/736x/d5/f6/1d/d5f61d3c7551c12dcbe5921ca8ed3b11.jpg", caption="Image of Burns")
        st.write("1. Remove the heat source.")
        st.write("2. Cool the burn with cool or lukewarm running water for 20 minutes.")
        st.write("3. Cover the burn with a sterile dressing.")
    elif injury == "Cuts and Scrapes":
        st.write("Treatment for Cuts and Scrapes:")
        st.image("https://my.clevelandclinic.org/-/scassets/images/org/health/articles/25079-abrasion", caption="Image of Cuts and Scrapes")
        st.write("1. Clean the wound with soap and water.")
        st.write("2. Apply an antibiotic ointment.")
        st.write("3. Cover with a sterile bandage.")
    elif injury == "Sprains and Strains":
        st.write("Treatment for Sprains and Strains:")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgdmwzkZyJjbWNG8jvkz-La2A2DHYgtRKMYfpIGd6xNQ&s", caption="Image of Sprains and Strains")
        st.write("1. Rest the injured area.")
        st.write("2. Ice the area to reduce swelling.")
        st.write("3. Compress the area with a bandage.")
        st.write("4. Elevate the injured area.")
    elif injury == "Snake Bite":
        st.write("Treatment for Snake Bite:")
        st.image("https://jssuni.edu.in/jssaher/cpm-pic/picjsscp/images/snake-bite-diffrences.jpg", caption="Image of Snake Bite")
        st.write("1. Keep the person calm and still.")
        st.write("2. Keep the bitten area at or slightly below the level of the heart.")
        st.write("3. Wash the bite with soap and water.")
        st.write("4. Get medical help immediately.")
    elif injury == "Heart Attack":
        st.write("Treatment for Heart Attack:")
        st.image("https://www.asterhospitals.in/sites/default/files/2021-09/Dashboard_952_heartattack_9_20.jpg", caption="Image of Heart Attack")
        st.write("1. Call emergency services (911).")
        st.write("2. Chew and swallow aspirin if not allergic.")
        st.write("3. Begin CPR if the person is unconscious.")
    elif injury == "Head Injury":
        st.write("Treatment for Head Injury:")
        st.image("https://cdn.vectorstock.com/i/1000v/96/49/head-injury-vector-46779649.jpg", caption="Image of Head Injury")
        st.write("1. Apply pressure to stop any bleeding.")
        st.write("2. Keep the person still and calm.")
        st.write("3. Apply ice to reduce swelling.")
        st.write("4. Seek medical attention immediately.")
    elif injury == "Broken or Fractured Bone":
        st.write("Treatment for Broken or Fractured Bone:")
        st.image("https://media.istockphoto.com/id/692165588/photo/man-massaging-painful-wrist-on-a-white-background-pain-concept.jpg?s=612x612&w=0&k=20&c=uOa1TCKpKwx3Q52e1Zg27h_cH10jJSiKCGM0l6dcMKY=", caption="Image of Broken or Fractured Bone")
        st.write("1. Immobilize the injured area.")
        st.write("2. Apply ice to reduce swelling.")
        st.write("3. Elevate the injured area.")
        st.write("4. Seek medical attention immediately.")
    elif injury == "Severe Bleeding":
        st.write("Treatment for Severe Bleeding:")
        st.image("https://www.baptisthealthsystem.com/images/global/newsroom-ccb/infographics/when-does-bleeding-need-emergency-care/bleeding-er-care-02.jpg", caption="Image of Severe Bleeding")
        st.write("1. Apply direct pressure to the wound.")
        st.write("2. Elevate the wound above the heart.")
        st.write("3. Apply pressure to pressure points if bleeding doesn't stop.")
        st.write("4. Seek medical help immediately.")
    elif injury == "Fainting":
        st.write("Treatment for Fainting:")
        st.image("https://t3.ftcdn.net/jpg/05/80/22/36/360_F_580223666_d1y8aLXkS5DbQWrM8jNtskmb5w1WeWh8.jpg", caption="Image of Fainting")
        st.write("1. Lay the person flat and raise their legs.")
        st.write("2. Check their airway and breathing.")
        st.write("3. Loosen any tight clothing.")
        st.write("4. When they regain consciousness, help them sit up slowly.")

# App Title
st.title("First Aid Help App")

# Buttons for different types of injuries
if st.button("Burns"):
    show_treatment("Burns")

if st.button("Cuts and Scrapes"):
    show_treatment("Cuts and Scrapes")

if st.button("Sprains and Strains"):
    show_treatment("Sprains and Strains")

if st.button("Snake Bite"):
    show_treatment("Snake Bite")

if st.button("Heart Attack"):
    show_treatment("Heart Attack")

if st.button("Head Injury"):
    show_treatment("Head Injury")

if st.button("Broken or Fractured Bone"):
    show_treatment("Broken or Fractured Bone")

if st.button("Severe Bleeding"):
    show_treatment("Severe Bleeding")

if st.button("Fainting"):
    show_treatment("Fainting")
