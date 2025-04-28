# Space Missions Data Analysis

A comprehensive Python tool for analyzing and visualizing space mission data from 1957 to present day.

## Overview

This project provides an in-depth analysis of space missions data, including visualizations of launch frequencies, mission success rates, and the most active space organizations. The tool generates multiple visualizations to help understand trends and patterns in space exploration history.

## Features

- **Data Loading and Cleaning**: Handles various file encodings to ensure proper data loading
- **Exploratory Data Analysis**: Basic statistical overview and data quality checks
- **Missing Data Visualization**: Heatmap visualization of missing values
- **Multiple Visualization Types**:
  - Top space organizations by number of launches
  - Mission outcome distribution (pie chart and bar plot)
  - Year-wise launch frequency trends
  - Success rate comparison among top organizations
  - Most frequently used rockets

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn

Install required packages using:

```bash
pip install pandas matplotlib seaborn
```

## Usage

1. Clone this repository:
```bash
git clone https://github.com/yourusername/space-missions-analysis.git
cd space-missions-analysis
```

2. Place your `space_missions.csv` file in the project directory or update the file path in the script.

3. Run the analysis script:
```bash
python space_missions_analysis.py
```

4. The script will generate visualization PNG files in the same directory.

## Data Requirements

The script expects a CSV file with the following columns:
- `Company`: Organization responsible for the space mission
- `Date`: Launch date of the mission
- `MissionStatus`: Outcome status of the mission
- `Rocket`: Type of rocket used (optional)

Other columns may be present but aren't necessary for core functionality.

## Output Files

The script generates the following visualization files:
- `missing_values_heatmap.png`: Visualization of missing data
- `top_companies.png`: Bar chart of the most active space organizations
- `mission_status_pie.png`: Pie chart showing mission outcome distribution
- `mission_status_bar.png`: Bar chart showing mission outcome counts
- `yearly_launches.png`: Line plot of launches per year
- `success_rate_by_company.png`: Success rate comparison for top organizations
- `top_rockets.png`: Bar chart of most used rockets (if data available)

## Handling Encoding Issues

The script attempts to handle different file encodings that may cause reading errors:
1. First tries ISO-8859-1 encoding
2. Falls back to latin1 if needed
3. Finally attempts UTF-8 with error replacement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sourced from publicly available space mission records
- Inspired by the need to understand historical trends in space exploration
