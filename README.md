# University Exam Performance Analysis

## Overview
The "University Exam Performance Analysis" project aims to provide in-depth insights into student performance, including trends in grades, arrears, fund losses, and graduation type classifications. The PowerBI dashboard uses interactive visualizations to allow users to analyze data department-wise and year-wise (batch).

## Technology Stack
- **Data Extraction & Processing**: Python (using `docx`, `pandas`, and `openpyxl`)
- **Data Visualization**: PowerBI
- **Data Conversion Pipeline**: PDF → Word (via ilovepdf.com) → Python Dictionary → Pandas DataFrame → Excel → Power Query → PowerBI

## Features
- **Slicers for Interactive Analysis**: Users can filter data by **Department** and **Batch (Year Joined)**.
- **Exam Performance Analysis**: Visualizes student performance based on grades, arrears, and department.
- **Grading and Arrears Over Semesters**: Provides an overview of grade distribution, arrears across semesters, and revaluation information.
- **Graduation Type and Department Classification**: Analyzes graduation types and department-wise performance trends.
  
## Data Privacy
- This project is **view-only** and does not allow any modifications to the data.
- All data is private and confidential, and it is handled in compliance with appropriate data privacy standards.

## Dataset Information
The dataset includes the following key details:
- **Exam Date**
- **Register Number**
- **Subject Code**
- **Grade Achieved**
- **Arrears Data (Semester-wise)**

## Data Conversion Process
1. **PDF to Word**: Initial PDF files are converted to Word format using [ilovepdf.com](https://www.ilovepdf.com).
2. **Word to Python Dictionary**: The Word file is then parsed using Python's `python-docx` module to convert it into a dictionary format.
3. **Dictionary to Pandas DataFrame**: Data is processed and cleaned into a Pandas DataFrame.
4. **Data to Excel**: Cleaned data is exported to Excel for use in Power Query.
5. **PowerBI Visualization**: The processed data is then used in PowerBI to create an interactive dashboard.

## Installation & Setup
There are no installation instructions as this project is a **view-only** PowerBI dashboard. The data processing and extraction steps are handled externally.

## Contributors
This project was developed by:
- **Mohanraj S**
- **Rajan N**
- **Rishi Kanna S**
- **Rajkumar K**

Special thanks to:
- **NATARAJAN** (Principal) for project approval
- **PRINCE** (DB Admin) for providing the dataset

## License
This project is provided for **view-only** purposes and cannot be modified. Redistribution or adaptation is not permitted.
