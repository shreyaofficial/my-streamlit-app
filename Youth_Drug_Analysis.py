# 1. Import Libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Adding enhanced CSS for styling
st.markdown("""
    <style>
    /* General Body Style */
    body {
        background-color: #F0F2F6;
        font-family: 'Helvetica Neue', sans-serif;
        color: #2C3E50;
    }

    /* Main Title Style */
    .main-title {
        text-align: center;
        color: #3498DB;
        font-size: 3em;
        font-weight: bold;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Subheader Style */
    .stHeader {
        color: #E74C3C;
        font-size: 1.8em;
        margin-top: 20px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        border-bottom: 2px solid #E74C3C;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    /* Sidebar Style */
    .sidebar .sidebar-content {
        background-color: #ECF0F1;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content h2 {
        color: #16A085;
    }

    /* Style for markdown text */
    .markdown-text {
        font-size: 1.2em;
        color: #2C3E50;
        margin-bottom: 20px;
        line-height: 1.6;
    }

    /* Button Style */
    .stButton button {
        background-color: #3498DB;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-size: 1.1em;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button:hover {
        background-color: #2980B9;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }

    /* Style for charts */
    .chart-container {
        background-color: #F7F9FB;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    /* Style for bar charts */
    .stBarChart {
        background-color: #F9E79F;
        border-radius: 5px;
        padding: 10px;
    }

    /* Style for pie charts */
    .stPieChart {
        background-color: #FADBD8;
        border-radius: 5px;
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Style for line charts */
    .stLineChart {
        background-color: #D5DBDB;
        border-radius: 5px;
        padding: 10px;
    }

    /* Custom styling for data tables */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Custom scrollbar for a smoother look */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #ECF0F1;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: #3498DB;
        border-radius: 10px;
    }

    /* Adding hover effects to charts for interactivity */
    .chart-container:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
        transition: transform 0.2s ease-in-out;
    }

    /* Table header style */
    .stTable th {
        background-color: #3498DB;
        color: white;
        font-size: 1.1em;
        padding: 10px;
        border-radius: 5px 5px 0 0;
    }

    /* Data rows style */
    .stTable td {
        background-color: #FFFFFF;
        color: #2C3E50;
        font-size: 1em;
        padding: 8px;
        border-bottom: 1px solid #ECECEC;
    }

    /* Data rows hover effect */
    .stTable tr:hover {
        background-color: #F4F6F6;
    }

    /* Footer styling */
    .stFooter {
        text-align: center;
        color: #95A5A6;
        margin-top: 20px;
        font-size: 0.9em;
        border-top: 1px solid #ECECEC;
        padding-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)


# 2. Load the Dataset
@st.cache_data
def load_data():
    file_path = 'C:/Users/hp/OneDrive/Desktop/youth_smoking_drug_data_10000_rows_expanded.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        st.error("Dataset file not found. Please check the path and try again.")
        return None


df = load_data()

# 3. Display the title and description
st.markdown('<h1 class="main-title">Youth Smoking and Drug Data Analysis</h1>', unsafe_allow_html=True)
st.write("This dashboard provides insights into youth smoking and drug experimentation from 2020 to 2024.")

# Check if data loaded successfully
if df is not None:
    # Display the column names
    st.write("Columns in the dataset:", df.columns.tolist())

    # 4. Data Cleaning
    st.header("Data Cleaning")
    if st.checkbox("Show Raw Data"):
        st.write(df.head())

    # Handle missing values
    df.dropna(inplace=True)

    # Convert columns if needed
    df['Year'] = df['Year'].astype(int)  # Convert Year to int
    df['Age_Group'] = df['Age_Group'].astype(str)  # Convert Age_Group to str

    st.write("Data cleaned. Total records:", len(df))

    # 5. Summary Statistics
    st.header("Summary Statistics")
    st.markdown("""
            <p class="markdown-text">Below are summary statistics for key variables like Smoking Prevalence and Drug Experimentation.
            These statistics provide an overview of central tendencies and variability within the data.</p>
        """, unsafe_allow_html=True)

    # Calculate summary statistics for Smoking Prevalence and Drug Experimentation
    summary_df = df[['Smoking_Prevalence', 'Drug_Experimentation']].describe().T
    summary_df['median'] = df[['Smoking_Prevalence', 'Drug_Experimentation']].median()
    summary_df['mode'] = df[['Smoking_Prevalence', 'Drug_Experimentation']].mode().iloc[0]

    # Display summary statistics table
    st.write(summary_df)

    # 6. Data Visualization
    # Sidebar for Filtering Data
    st.sidebar.title("Filters")
    selected_year = st.sidebar.slider("Select Year Range", 2020, 2024, (2020, 2024))
    selected_gender = st.sidebar.selectbox("Select Gender", ['All', 'Male', 'Female'])

    # Filter the data based on selections
    filtered_data = df[(df['Year'] >= selected_year[0]) & (df['Year'] <= selected_year[1])]
    if selected_gender != 'All':
        filtered_data = filtered_data[filtered_data['Gender'] == selected_gender]

    st.write(f"Data filtered for the year range: {selected_year} and gender: {selected_gender}")
    st.write(filtered_data.head())

    # 7. Age Group Distribution
    st.header("Age Group Distribution(Bar Chart)")
    st.markdown("""<p class="markdown-text">This chart shows the distribution of individuals across different age groups in the dataset.
        Understanding the age distribution is crucial for targeting interventions effectively.</p>""",
                unsafe_allow_html=True)
    age_dist = filtered_data['Age_Group'].value_counts()
    st.bar_chart(age_dist)

    # 8. Age Group Distribution Pie Chart
    st.header("Age Group Distribution (Pie Chart)")
    st.markdown("""<p class="markdown-text">This pie chart illustrates the proportion of individuals across different age groups in the dataset.
        Understanding these proportions helps in designing targeted interventions and programs based on age demographics.</p>""",
                unsafe_allow_html=True)
    age_dist = filtered_data['Age_Group'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(age_dist, labels=age_dist.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Additional: Gender Distribution Pie Chart
    st.header("Gender Distribution (Pie Chart)")
    st.markdown("""<p class="markdown-text">This pie chart shows the distribution of individuals by gender in the dataset.
        Analyzing gender distribution is important for understanding patterns and differences in smoking and drug experimentation behaviors.</p>""",
                unsafe_allow_html=True)
    gender_dist = filtered_data['Gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_dist, labels=gender_dist.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    ax.axis('equal')
    st.pyplot(fig)

    # 9. Smoking Prevalence Over Time
    st.header("Smoking Prevalence Over Time")
    st.markdown("""<p class="markdown-text">This line chart illustrates the average smoking prevalence among youth over the selected years.
        Analyzing these trends helps us understand if smoking rates are increasing, decreasing, or remaining stable, which is vital for policy making.</p>""",
                unsafe_allow_html=True)
    smoking_trends = filtered_data.groupby('Year')['Smoking_Prevalence'].mean()
    st.line_chart(smoking_trends)

    # 10. Smoking Prevalence Trends by Age Group
    st.header("Smoking Prevalence Trends by Age Group (Line Chart)")
    st.markdown(
        """<p class="markdown-text">This line chart displays smoking prevalence trends over time for each age group. It helps identify if certain age groups have differing trends compared to others.</p>""",
        unsafe_allow_html=True)

    # Create a larger figure
    fig, ax = plt.subplots(figsize=(12, 6))  # Increase width and height as needed
    sns.lineplot(data=filtered_data, x='Year', y='Smoking_Prevalence', hue='Age_Group', ax=ax)
    ax.set_title("Smoking Prevalence by Age Group")
    ax.set_xlabel("Year")
    ax.set_ylabel("Smoking Prevalence")
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Adjust the legend position
    st.pyplot(fig)

    # 11. Smoking Prevalence Trends by Gender
    st.header("Smoking Prevalence Trends by Gender (Line Chart)")
    st.markdown(
        """<p class="markdown-text">This line chart displays smoking prevalence trends over time, segmented by gender. It allows for an analysis of whether smoking rates are changing differently between male and female youth.</p>""",
        unsafe_allow_html=True)

    # Create a larger figure
    fig, ax = plt.subplots(figsize=(12, 6))  # Increase width and height as needed
    sns.lineplot(data=filtered_data, x='Year', y='Smoking_Prevalence', hue='Gender', ax=ax)
    ax.set_title("Smoking Prevalence by Gender")
    ax.set_xlabel("Year")
    ax.set_ylabel("Smoking Prevalence")
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Adjust the legend position
    st.pyplot(fig)

    # Additional: Box Plot of Smoking Prevalence by Socioeconomic Status
    st.header("Box Plot of Smoking Prevalence by Socioeconomic Status")
    st.markdown("""
        <p class="markdown-text">This box plot visualizes the distribution of smoking prevalence among different socioeconomic status groups. 
        Each box represents the interquartile range (IQR), where the middle 50% of the data lies. The line inside each box indicates the median smoking prevalence, while the whiskers show the range of the data excluding outliers. 
        Outliers are represented as individual points beyond the whiskers. This visualization helps in understanding how socioeconomic factors influence smoking behavior among youth.</p>
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_data, x='Socioeconomic_Status', y='Smoking_Prevalence', ax=ax, palette='Set3')
    ax.set_title("Distribution of Smoking Prevalence by Socioeconomic Status")
    st.pyplot(fig)

    # 12. Drug Experimentation Rates
    st.header("Drug Experimentation Rates Over Time (Line Chart)")
    st.markdown("""<p class="markdown-text">This chart displays the trends in drug experimentation rates among youth from 2020 to 2024.
        Observing these trends can inform us about the effectiveness of drug prevention programs and help guide future strategies.</p>""",
                unsafe_allow_html=True)
    drug_trends = filtered_data.groupby('Year')['Drug_Experimentation'].mean()
    st.line_chart(drug_trends)

    # 13. Recommendations Section
    st.header("Recommendations")
    st.markdown("""
          <p class="markdown-text">Based on the analysis of youth smoking and drug data, here are some recommendations for targeted interventions:</p>
          <ul class="markdown-text">
              <li><b>Focus on High-Risk Age Groups:</b> Age groups with higher smoking prevalence should be prioritized for intervention programs, such as awareness campaigns and counseling sessions.</li>
              <li><b>Gender-Specific Programs:</b> Tailor programs to address differences in smoking and drug use behavior between male and female youths to maximize the effectiveness of prevention efforts.</li>
              <li><b>Strengthen Socioeconomic Support:</b> Given the link between socioeconomic status and smoking prevalence, efforts to improve socioeconomic conditions may help reduce smoking rates.</li>
              <li><b>Enhance School and Community Programs:</b> Increasing the availability and effectiveness of school programs and community support can create a safer environment for youth, reducing drug experimentation rates.</li>
              <li><b>Promote Access to Counseling:</b> Improving access to mental health and substance abuse counseling can provide crucial support to at-risk individuals.</li>
          </ul>
      """, unsafe_allow_html=True)

    # 14. Custom Analysis Requests
    st.header("Custom Analysis Requests")
    st.markdown(
        """<p class="markdown-text">If you would like to request a specific analysis, please select the parameters below:</p>""",
        unsafe_allow_html=True)

    # User Input for Custom Analysis
    selected_year = st.selectbox("Select Year", df['Year'].unique())
    selected_age_group = st.selectbox("Select Age Group", df['Age_Group'].unique())

    if st.button("Get Analysis"):
        # Filter data based on user input
        custom_filtered_data = df[(df['Year'] == selected_year) & (df['Age_Group'] == selected_age_group)]
        if not custom_filtered_data.empty:
            st.write(f"Analysis for Year: {selected_year}, Age Group: {selected_age_group}")
            st.write(custom_filtered_data)
        else:
            st.error("No data available for the selected parameters.")



    #15. Quiz Section
    st.header("Youth Smoking & Drug Awareness Quiz")
    st.markdown(
        """<p class="markdown-text">Test your knowledge on youth smoking and drug-related issues. Select the correct answer for each question below, then submit your answers:</p>""",
        unsafe_allow_html=True)

    # Initialize variables for quiz
    score = 0

    # Quiz Questions
    question1 = st.radio(
        "1. What is the most common age group for drug experimentation among youth?",
        ("A. 10-14", "B. 15-19", "C. 20-24", "D. 25-29")
    )
    question2 = st.radio(
        "2. Which factor is most strongly linked to youth smoking habits?",
        ("A. Peer Influence", "B. Media Influence", "C. Socioeconomic Status", "D. School Programs")
    )
    question3 = st.radio(
        "3. Which of the following is a recommended intervention for reducing youth smoking rates?",
        ("A. Ignoring the problem", "B. Providing access to counseling", "C. Limiting educational programs",
         "D. None of the above")
    )

    # Submit all answers at once
    if st.button("Submit Quiz"):
        if question1 == "B. 15-19":
            score += 1
        if question2 == "A. Peer Influence":
            score += 1
        if question3 == "B. Providing access to counseling":
            score += 1

        st.markdown(f"**Your Total Score: {score} out of 3**")
        if score == 3:
            st.success("Excellent! You have a great understanding of the issues.")
        elif score == 2:
            st.info("Good job! But there’s room for improvement.")
        else:
            st.warning("Keep learning! More awareness can lead to better outcomes.")

    # 16. User Input Section: Feedback Form
    st.header("Feedback Form")
    st.markdown(
        """<p class="markdown-text">We appreciate your feedback! Please let us know your thoughts on the dashboard or request specific analyses below:</p>""",
        unsafe_allow_html=True)
    feedback = st.text_area("Your Feedback/Requests:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
    # Footer
    st.markdown('<p class="stFooter">Powered by Streamlit | Youth Data Analysis 2024</p>', unsafe_allow_html=True)
