import pandas as pd  
import streamlit as st
import joblib 
model=joblib.load("student_strength_model.pkl")
model_coloum=joblib.load("model_columns.pkl")
df = pd.read_csv("clean data.csv")

st.set_page_config(
    page_icon="🎓",
    page_title="Student Strength Prediction",
    layout="wide"
)

### sidebar ###############

st.sidebar.title("Student Strength Prediction")
st.sidebar.header("Prediction System")

page = st.sidebar.radio(
    "NAVIGATIOTION",
    ["HOME", "PREDICAT", "ABOUT"]
)

st.sidebar.markdown("---")

st.sidebar.title("ABOUT")
st.sidebar.text(
"""
This project predicts the approximate student strength
of a college using Machine Learning techniques.
"""
)
################## HOME ###################
if page == "HOME":
    st.title("🎓 Student Strength Prediction System")
    st.markdown("Welcome to the *Student Strength Prediction System")
    st.write("""
This project predicts the approximate student strength of a college using Machine Learning techniques
""")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="FEATURES USED ", value=6)

    with col2:
        st.metric(label=" BEST MODEL", value="RANDOM FOREST")

    st.subheader(" Features Used")

    feature_df = pd.DataFrame({
        "Features": ["State","City","College Type","College_Management","Number of Courses","Region"]
    })

    st.table(feature_df)

    st.subheader("🎯 Real World Applications")

    st.write("""
    ✅ College capacity planning

    ✅ Faculty requirement estimation

    ✅ Hostel planning

    ✅ Transport planning

    ✅ Infrastructure development

    ✅ Budget allocation and resource management
    """)

    st.subheader(" How to Use")

    st.write("""
    1. Open the *Predict* page.
    2. Enter college details.
    3. Click *Predict Student Strength*.
    4. View the estimated student strength.
    """)
    st.markdown("----")
############ preeicat page 
###############################
elif page == "PREDICAT":

    st.title("🎓 Student Strength Prediction")
    st.write("Enter the college details below to predict student strength.")

    col1, col2, col3 = st.columns(3)

    with col1:
        STATE = st.selectbox(
            "State",
            sorted(df["State"].dropna().unique())
        )

    with col2:
        city = st.selectbox(
            "City",
            sorted(df["City"].dropna().unique())
        )

    with col3:
        college_type = st.selectbox(
            "College Type",
            sorted(df["College_Type"].dropna().unique())
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        management = st.selectbox(
           "College_Management",
            sorted(df["College_Management"].dropna().unique())
        )

    with col5:
        courses = st.number_input(
            "Number of Courses",
            min_value=1,
            value=5
        )

    with col6:
        region = st.selectbox(
            "Region",
            sorted(df["Region_North_South_East_West_Central"].dropna().unique())
        )

    if st.button("Predict Student Strength"):

        input_data = pd.DataFrame({
            "State": [STATE],
            "City": [city],
            "College_Type": [college_type],
            "College_Management": [management],
            "Total_no._of_Courses": [courses],
            "Region_North_South_East_West_Central": [region]
        })

        # Convert text columns into dummy columns
        input_data = pd.get_dummies(input_data)

        # Match training columns
        input_data = input_data.reindex(columns=model_coloum, fill_value=0)

        # Prediction
        prediction = model.predict(input_data)

        st.success("Prediction Completed Successfully ✅")

        st.metric(
            label="Predicted Student Strength",
            value=f"{int(prediction[0])} Students"
        )
elif page=="ABOUT":
    st.title("ABOUT THIS PROJECT ")
    st.subheader("DESCRIPTION")
    
    st.write("""
    ### Student Strength Prediction System

    This project predicts the approximate number of students
    in a college using Machine Learning algorithms.

    ### Technologies Used
     Python
     Pandas
     Scikit-Learn
     Streamlit

    ### Machine Learning Models
     Linear Regression AND Random Forest Regressor

    ### Best Model
    Random Forest Regressor
    """)


    