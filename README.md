# University Exam Performance Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset Information](#dataset-information)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Data Modeling & DAX Calculations](#data-modeling--dax-calculations)
- [Visualizations and Dashboards](#visualizations-and-dashboards)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Overview
This collaborative project involves a team of four members working on the analysis and visualization of university exam performance using Power BI. The goal is to gather key data on various metrics such as academic performance, student fund matters and graduation classification, and then analyze and present these in a meaningful way.

The project leverages Power BI’s robust capabilities to create interactive dashboards, insightful visualizations, and custom metrics that help uncover trends and performance peaks and downfalls in exams.

## Features
- **Data Visualizations**: Interactive charts, graphs, and KPIs that provide an overview of exam performance.
- **Trend Analysis**: Visualization of university performance metrics across multiple academic years.
- **Measure of Arrears**: Maps displaying the locations and performance scores of universities.
- **User Interaction**: Ability to filter and drill down on various metrics for deeper insights.
- **Key Performance Indicators (KPIs)**: Detailed performance analysis of universities based on key metrics such as graduation type and student scores.

## Dataset Information
The project uses the following datasets to perform analysis:

1. **Students Performance**: (fact table)
   - Contains information such as student register number and grade, and exam date.
   - Columns: *Register Number*, *Exam Date*, *Grade*, *Subject Code*, etc.

2. **Student Summary**:
   - Contains information about students.
   - Columns: *Student Name*, *Joining Year*, *Department ID*, *Graduation Type*, etc.

3. **Faculty Data**:
   - Provides faculty-related metrics including satisfaction and quality scores.
   - Columns: `University Name`, `Faculty Satisfaction`, `Faculty Quality Score`, etc.

4. **Geospatial Data**:
   - Includes geographic coordinates (latitude and longitude) for universities.
   - Columns: `University Name`, `Latitude`, `Longitude`.

## Installation Instructions
To run this project locally, follow these steps:

1. **Clone or Download the Project**:
   - Clone this repository or download the `.pbix` Power BI file.
   
2. **Open Power BI Desktop**:
   - Open the `.pbix` file in Power BI Desktop .
   
3. **Publish to Power BI Service** (Optional):
   - If you'd like to share the report, publish it to Power BI Service.

## Usage Guide
Once the project is loaded in Power BI, here’s how you can use it:

1. **Explore Dashboards**:
   - Use the interactive dashboards to explore performance metrics for different universities.

2. **Apply Filters and Slicers**:
   - Filters allow you to drill down into specific data points, like university, academic year, and performance score.

3. **Drill Down for Deeper Insights**:
   - Use drill-down features to investigate specific metrics in more detail.

4. **Geospatial Analysis**:
   - View university locations and their corresponding performance scores on a map.

## Data Modeling & DAX Calculations
The data model and DAX measures in this project help to calculate key performance metrics, including:

- **Relationships**:
   - The project uses relationships between datasets (e.g., `University Name` linking `University Data`, `Student Data`, and `Faculty Data`).

- **DAX Measures**:
   - Custom DAX calculations have been created for metrics like:
     - `Average Graduation Rate = AVERAGE(Student Data[Graduation Rate])`
     - `Performance Growth = (This Year’s Performance - Last Year’s Performance) / Last Year’s Performance`

## Visualizations and Dashboards
The Power BI report includes the following key visualizations:

1. **University Performance Dashboard**:
   - Provides insights into key metrics such as performance scores, graduation rates, and satisfaction scores.

2. **Geospatial Map**:
   - Displays university locations and their performance levels using color-coded markers.

3. **Trend Analysis**:
   - Line charts and bar charts that show performance trends over time.

4. **Performance Comparison**:
   - Comparison dashboards for different universities based on metrics such as faculty quality and student satisfaction.

## Known Limitation
- **Period Lower Limitation**: Dataset contains information about exams starting from Dec 2017 till May 2024. This also contains some information about students who joined before 2017, sometimes involving in arrears. So, filtering it before the visualisation gives the students with only full infomation.
- **Period Upper Limitation**: For Students who joined 2021 and above years, the Graduation Type and other features may be false as it could change over time. For those, the informations are only based on what is recorded so far.

## Contributing
This is a collaborative project with four team members. Contributions and improvements are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement and test your changes.
4. Submit a pull request with a clear description of your modifications.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

We would like to express our heartfelt gratitude to the following individuals for their support and contributions to this project:

- **NATARAJAN**, Principal, GIET, Vellore: For approving access to the university's database and supporting this initiative.
- **PRINCE**, Database Administrator, GIET, Vellore: For facilitating database access, ensuring data quality, and assisting with data extraction.
- All our team members for their collaboration, dedication, and hard work.


## Contact
For questions, support, or feedback, feel free to reach out:

- **Project Team**:
  - [Mohanraj S](mailto:email@example.com)
  - [Rajan N](mailto:rajanofficial002@gmail.com)
  - [Rajkumar K](mailto:email@example.com)
  - [Rishi Kanna S](mailto:email@example.com)

