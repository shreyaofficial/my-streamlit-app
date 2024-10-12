# my-streamlit-app
Youth Smoking and Drug Analysis Dashboard : An interactive Streamlit dashboard for analyzing youth smoking and drug experimentation trends from 2020-2024. It includes visualizations, statistics, and insights based on age, gender, and socioeconomic factors. The goal is to support targeted interventions and raise awareness.


## Features

- **Data Visualization**: Interactive bar charts, pie charts, and line charts.
- **Data Filtering**: Filter data by year range and gender for focused analysis.
- **Summary Statistics**: Descriptive statistics for smoking prevalence and drug experimentation.
- **Custom Analysis**: Option to perform user-defined analysis by selecting specific parameters.
- **Recommendations**: Suggestions based on data insights for targeted interventions.
- **Youth Awareness Quiz**: A simple quiz to raise awareness about youth smoking and drug-related issues.
- **Feedback Form**: Collect feedback and suggestions for further analysis.

## Project Structure


youth-drug-analysis-dashboard/ ├── main.py # Streamlit app script 
                               ├── youth_smoking_drug_data_10000_rows_expanded.csv # Dataset 
                               └── README.md # Project documentationtion



## Dataset

The dataset contains information from 2020 to 2024 with the following columns:
[youth_smoking_drug_data_10000_rows_expanded.csv](https://github.com/user-attachments/files/17351586/youth_smoking_drug_data_10000_rows_expanded.csv)


- **Year**: Year of the data.
- **Age_Group**: Age group of the individuals.
- **Gender**: Gender of the individuals.
- **Smoking_Prevalence**: Prevalence of smoking among youth.
- **Drug_Experimentation**: Percentage of youth experimenting with drugs.
- **Socioeconomic_Status**: Socioeconomic status of the individuals.
- **...and more** (refer to the code for a full list).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/youth-drug-analysis-dashboard.git
   cd youth-drug-analysis-dashboard

2. Install the required packages:
   ```bash
   pip install pandas streamlit matplotlib seaborn

3. Run the Streamlit app:
   ```bash
   streamlit run Youth_Drug_Analysis.py

## Usage

- Adjust the filters on the sidebar to explore different trends.
- View the summary statistics and visualizations.
- Use the custom analysis section for specific queries.
- Take the awareness quiz and provide feedback through the form.

## Contributing

- Feel free to open issues or submit pull requests for improvements or additional features. Contributions are welcome!

## License

- This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **Data source**: Provided as part of the project.
- **Libraries used**: Streamlit, Pandas, Matplotlib, Seaborn.

