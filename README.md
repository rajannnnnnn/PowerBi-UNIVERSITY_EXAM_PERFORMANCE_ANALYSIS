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
The **University Exam Performance Analysis** project is a collaborative effort involving a team of four members. It focuses on analyzing and visualizing university exam performance data using Power BI. The project aims to provide valuable insights into key academic performance metrics, such as graduation rates, student arrears, and grading details. The analysis is supported by data from multiple datasets related to student performance, department details, and exam results.

## Features
- **Interactive Data Visualizations**: Includes charts, graphs, and KPIs for visual analysis of exam performance and trends.
- **Trend Analysis**: Visual representation of performance trends over multiple academic years and semesters.
- **Grading System Insights**: Detailed visualization of performance data based on grading system thresholds.
- **Arrears Tracking**: A focused analysis of arrears over different semesters, highlighting areas for improvement.

## Dataset Information
The datasets used in this project include:

1. **Students Performance**:
   - Contains detailed exam data including `Register Number`, `Subject Code`, `Grade`, and `Exam Date`.
   
2. **Department Details**:
   - Information about university departments, such as `Department ID`, `Department Name`, and `Short Name`.

3. **Students Summary**:
   - Includes demographic and academic information for each student, including `Graduation Type`, `Join Type`, and `Arrears Track`.

4. **Exams Details**:
   - Data related to exams, including `Exam Date`, `Grade`, and `Semester information`.

5. **Grading System**:
   - Details of the grading system, including grade boundaries and regulations.

6. **Arrears Tracking**:
   - A record of arrears over different semesters, linked to student performance.

## Installation Instructions
To get started with the project, follow these steps:

1. **Clone or Download the Repository**:
   - Clone this repository or download the `.pbix` Power BI file to your local system.

2. **Open Power BI Desktop**:
   - Launch Power BI Desktop and open the `.pbix` file.

3. **Publish to Power BI Service** (Optional):
   - If you would like to share the reports, publish them to Power BI Service.

## Usage Guide
Once the project is loaded into Power BI, you can interact with the dashboards as follows:

1. **Explore Dashboards**:
   - Navigate through the various interactive dashboards to gain insights into university performance metrics.
   
2. **Apply Filters and Slicers**:
   - Use filters and slicers to drill down into specific departments, academic years, or performance scores.

3. **Arrears Analysis**:
   - Track arrears over multiple semesters and identify trends or areas for improvement.

4. **Trend Analysis**:
   - Visualize performance trends over time using line charts and bar charts.

## Data Modeling & DAX Calculations
The data model for this project connects various datasets to ensure accurate analysis. Key relationships between datasets have been established to provide a cohesive view of the performance data:

- **Student Performance and Department**: Linked by `Department ID`.
- **Student Summary and Performance**: Linked by `Register Number`.
- **Arrears and Exam Details**: Linked by `Register Number` and `Semester`.
- **Grading System and Performance**: Linked by `Grade`.

### Key DAX Calculations:
- **Average Graduation Rate**:
  ```DAX
  Average Graduation Rate = AVERAGE(Student Data[Graduation Rate])
