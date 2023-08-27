# Interactive Dashboard Project

Welcome to the Interactive Dashboard project repository! This project aims to provide valuable insights and visualizations based on suicide, HDI (Human Development Index), and homicide data. The dashboard was built using the Dash framework, a Python web application framework for creating interactive, web-based data visualizations.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Limitations and Future Work](#limitations-and-future-work)
- [Summary](#summary)

## Introduction

The Interactive Dashboard project presents data from various datasets, including suicide statistics, HDI values, and homicide rates. The goal is to provide users with a user-friendly interface for exploring trends, patterns, and correlations within the datasets. The dashboard offers interactive visualizations, filtering options, and dynamic updates based on user inputs.

## Getting Started

For this prject Python version 3.8.6 was used. 
To run the dashboard locally on your machine, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/mv686/dashboard.git`.
2. Navigate to the project directory.
3. Install the required dependencies: `pip install -r requirements.txt`.
4. Run the dashboard: `python index.py`.
5. Open a web browser and go to `http://127.0.0.1:8050/` to access the dashboard.

## Usage

Once the dashboard is running, you can interact with it using the provided controls and filters. Select countries, years, and other parameters to see how the visualizations change in response. Explore trends, make comparisons, and gain insights from the data.

This dashboard consists of several interactive pages, each focusing on different aspects of the data. Below is a brief overview of each page and how to use them:
The button of the page that is selected is highlighted on top of the screen.

**Suicide Map:**
This page displays a world map with color-coded suicide data points based on the selected indicator. You can choose a single Year value. The Country Selector is optional and highlights selected countries. If no countries are selected, all available data is shown.

**HDI Map:**
This page displays a world map with color-coded Human Development Index data points. You can choose a single Year value. The Country Selector is optional and highlights selected countries. If no countries are selected, all available data is shown.

**Homicide Map:**
This page displays a world map with color-coded homicide data points based on the selected indicator. You can choose a single Year value. The Country Selector is optional and highlights selected countries. If no countries are selected, all available data is shown.

**Graphs:**
This page displays three graphs for Suicide, HDI, and Homicide data over the Year range. You can choose a Year range. The Country Selector is mandatory, and selected countries will be shown on the dropdown menu and to the right of the graphs.

**Charts:**
This page displays several pie and bar charts. You can choose a single Year value and only a single Country value. The first graph shows the distribution of Suicide by Age group. The next three charts display distribution by Sex for Suicides, HDI, and Homicides. The final graph displays the distribution of Suicide data by both Sex and Age group.

**About Page:**
This page offers information about the project, data sources, and the source code link.

### Data Sources

All datasets are open-source and used for educational purposes only.

- **WHO Mortality Dataset:**
  This dataset provides information about mortalities across different countries, genders, and age groups.
  Available at: [WHO Mortality datasets](https://www.who.int/data/data-collection-tools/who-mortality-database)

- **HDI Dataset:**
  The Human Development Index (HDI) dataset measures a country's overall human development, including factors like life expectancy, education, and income.
  Available at: [HDI downloads](https://hdr.undp.org/data-center/documentation-and-downloads)

- **UNODC Intentional Homicide Dataset:**
  This dataset contains information about intentional homicide rates in various countries, helping to understand crime trends.
  Available at: [UNODC database](https://dataunodc.un.org/dp-intentional-homicide-victims)



## Limitations and Future Work

While the Dash framework provides powerful tools for creating interactive web applications, there are a few limitations to consider:

- **Performance**: Handling large datasets and complex visualizations can lead to performance issues, especially on less powerful devices.
- **Customization**: While Dash provides various customization options, more advanced customization might require additional effort.
- **Complexity**: As Dash applications grow in complexity, maintaining and debugging the codebase can become challenging.
- **Mobile Responsiveness**: For this project only Desktop browsers were tested. Dash inherently supports responsive design, but refining the layout and interactions for mobile users requires careful attention.

In the future, improvements could include optimizing performance, enhancing user interactivity, and adding new datasets for analysis.

## Summary

In summary, the Interactive Dashboard project utilizes the Dash framework to create an interactive web-based dashboard for exploring suicide, HDI, and homicide data. By providing dynamic visualizations and filtering options, the dashboard enables users to uncover insights and trends within the datasets. The project demonstrates the capabilities of Dash for building interactive data applications.


