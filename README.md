# University Exam Performance Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Data Modeling & DAX Calculations](#data-modeling--dax-calculations)
- [Visualizations and Dashboards](#visualizations-and-dashboards)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Overview
The **University Exam Performance Analysis** project is an analytical tool built using PowerBI to provide valuable insights into the academic performance of university students. The dashboard aggregates student data, focusing on grade distribution, arrears, graduation trends, and department performance over multiple semesters. It presents actionable insights to educational administrators, professors, and decision-makers.

The project is based on a data pipeline that involves the conversion of raw exam data from PDFs to PowerBI visualizations. The dashboard allows users to interactively explore the data using slicers and filters for a more customized analysis.

## Features
- **Interactive Filters and Slicers**: 
  - Filter the data by **Department** and **Batch (Year of Admission)** for focused analysis.
  - Explore trends across various departments and academic years.
  
- **Detailed Exam Performance Analysis**: 
  - View student performance across subjects and exam dates.
  - Analyze grade distributions, performance trends, and identify key areas for improvement.
  
- **Arrears Analysis**: 
  - Track students' arrears across different semesters and identify recurring performance issues.
  
- **Graduation Classification**: 
  - Understand student graduation performance based on classifications such as **Distinction**, **First Class**, **Second Class**, and others.
  
- **Revaluation Insights**: 
  - Includes visualizations for revaluation trends and grade changes post-revaluation.

## Dataset Information
The dataset used in this project contains information extracted from university exam records. It includes the following columns:

- **Exam Date**: The date when the exam was conducted.
- **Register Number**: Unique identification number for each student.
- **Subject Code**: Code representing the subject in which the exam was conducted.
- **Grade Achieved**: Final grade received by the student in the subject.
- **Arrears Information**: The number of arrears (failed subjects) a student has in a given semester.
- **Graduation Classification**: Classification of graduation status such as **Distinction**, **First Class**, **Second Class**, etc.
- **Revaluation Details**: Includes information on revaluation requests and changes in grades.
- **Department**: Department under which the student is enrolled.
- **Batch (Year Joined)**: Year of admission, representing the student’s academic batch.

### Data Privacy Considerations
- **Sensitive Information**: The dataset includes private student information, including grades and departmental affiliations. This data must be handled with care and in compliance with applicable data privacy regulations.
- **View-only Access**: The PowerBI dashboard is designed for **view-only** access to ensure that no modifications are made to the original data.

## Installation Instructions
This project is a **view-only** PowerBI dashboard, and no installation or setup is required by the end user. To explore the project:
1. **PowerBI File**: Download and open the PowerBI file (provided in this repo).
2. **Dataset Access**: The underlying dataset is pre-loaded into the PowerBI report, and no additional data import is needed.

For developers wishing to replicate or extend the project:
- Python libraries used for data extraction and transformation (such as `python-docx`, `pandas`, `openpyxl`) are essential.
- The data pipeline can be replicated using the aforementioned tools if a similar dataset is available.

## Technology Stack

### Data Pipeline
The data pipeline for this project follows this flow:

- **PDF → Word → Python Dictionary → Pandas → Excel → Power BI**

### Breakdown:
1. **PDF → Word**:  
   - Raw data is extracted from PDF and converted into Word format using **iLovePDF**.

2. **Word → Python Dictionary**:  
   - The Word document is parsed using **python-docx** in Python, extracting the data into a Python dictionary.

3. **Python Dictionary → Pandas Dataframe**:  
   - The dictionary data is loaded into **Pandas Dataframe** for cleaning, transformation, and preparation.

4. **Pandas Dataframe → Excel**:  
   - The cleaned data is exported to **Excel** for easy handling and further processing.

5. **Excel → Power BI**:  
   - The structured data is imported into **Power BI** using **Power Query** for additional data transformation and visualization creation.

This streamlined pipeline ensures efficient data processing from raw extraction to insightful visualizations.


## Usage Guide
Once you open the PowerBI dashboard, you can begin exploring the data in a few simple steps:

### Key Actions:
1. **Slicing the Data**:
   - Use the **Department** slicer to filter the data by specific academic departments.
   - Use the **Batch (Year Joined)** slicer to explore performance trends across different batches or academic years.

2. **Exploring Visualizations**:
   - **Performance Overview**: View performance trends across different subjects, grades, and exam dates.
   - **Arrears Analysis**: Explore the distribution of arrears across various semesters and identify students or departments with high arrear rates.
   - **Revaluation Analysis**: Investigate grade changes post-revaluation.
   - **Students Fund Loss**: Measuring the total fund loss of students in various aspects.

3. **Exporting Data**: Some visualizations may support data export for further analysis.

## Data Modeling & DAX Calculations
The data modeling process leverages **Data Analysis Expressions (DAX)** in PowerBI to derive key performance metrics and insights. Some of the key DAX calculations include:

- **Grade Point Average (GPA) Calculation**: A measure that calculates the average grade point for students based on their subject grades.
- **Arrears Count**: A calculated column that identifies the number of arrears each student has across semesters.
- **Graduation Classification Trends**: A calculated measure that identifies trends in graduation classifications (e.g., Distinction, First Class, Second Class) across various departments.
- **Revaluation Impact**: A DAX measure to calculate the percentage change in grades post-revaluation.

The underlying data model organizes the dataset in a star schema to enable efficient querying and visualizations.

## Visualizations and Dashboards
The dashboard provides several key visualizations that represent various aspects of student performance:

1. **Grade Distribution by Department**: 
   - A **bar chart** visualizing the distribution of grades across various departments.
  
2. **Arrears Across Semesters**: 
   - A **line graph** showing the trends of arrears in each semester.
  
3. **Graduation Classification Analysis**: 
   - **Pie charts** or **donut charts** representing the proportions of different graduation classifications (Distinction, First Class, Second Class) within each department.

4. **Subject-wise Performance Trends**: 
   - A **scatter plot** or **heat map** showing student performance trends by subject over time.

5. **Revaluation Impact**: 
   - A **bar chart** or **waterfall chart** depicting the changes in grades before and after revaluation requests.

## Known Limitations

While this project provides valuable insights into student performance, there are a few known limitations that users should be aware of:

### 1. **Time Frame of Data**
- The dataset contains exam data starting from **December 2017** through **May 2024**. As such, students who joined the university **before 2017** or **after 2021** may have incomplete data. This is due to the nature of the dataset, which only includes records from specific academic years, making it less reliable for analysis for students outside this time frame. It was filtered out in Visualizations.

### 2. **Data for New Students**
- For students who joined after **2021**, certain details, such as **Graduation Classification**, may be **provisional**. This means that these values are subject to change over time, and their final status has yet to be confirmed as these students progress through their academic journey.


These limitations should be taken into account when interpreting the results and making decisions based on this analysis.

## Contributing
We are currently not accepting contributions directly to the PowerBI dashboard as it is a **view-only** project. However, we welcome suggestions for improvements, feature requests, or feedback via GitHub Issues.

### How to Contribute:
1. Fork the repository.
2. Submit issues or feature requests.
3. Share feedback or suggestions via pull requests for related documentation updates.

## License
This project is licensed under a **view-only** license and cannot be modified, redistributed, or adapted without explicit permission.

## Acknowledgements

We would like to express our sincere gratitude to the following individuals and organizations for their valuable contributions to this project:

### Project Approval and Guidance
- **NATARAJAN** Principal, GIET, Vellore: For approving the project and providing the necessary guidance throughout its development. Their support was instrumental in driving this project forward.

### Dataset and Technical Support
- **PRINCE** DB Administrator, GIET, Vellore: For providing the comprehensive dataset needed to power the analysis. His assistance in extracting, cleaning, and sharing the data in an accessible format (including database access) was essential to the project’s success.

### Development Team
The project was developed by a dedicated team of students who contributed their expertise in various aspects of the project:

- **Mohanraj S** : For overseeing the development and ensuring the quality of data extraction and analysis processes.
- **Rajan N** : For working on data cleaning, transformation, and DAX modeling.
- **Rishi Kanna S** : For designing the PowerBI dashboard and implementing various visualizations.
- **Rajkumar K** : For designing the PowerBI dashboard and implementing various visualizations.

### Tools and Technologies
- **Power BI**: For creating interactive dashboards and reports.
- **Python**: For data extraction and transformation using libraries such as `python-docx` and `pandas`.
- **Power Query**: For data preprocessing and cleaning.

## Contact
For any questions, feedback, or inquiries regarding this project, please contact the team at:

- **Mohanraj S**: mohan.email@example.com
- **Rajan N**: shalini.email@example.com
- **Rishi Kanna S**: karthik.email@example.com
- **Rajkumar K**: karthik.email@example.com
