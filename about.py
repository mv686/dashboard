from dash import html

# Create the content for the About page
about_content = html.Div(
    style={
        "width": "100%",  # Adjust this value as needed
        "margin": "0 auto",  # Center the content horizontally
        "backgroundColor": "#D4DADA",  # Specific background color
        "padding": "20px",  # Add padding for distance from borders
        "textAlign": "center",
        "height" : "100%"
    },
    children=[
        html.H1("About This Project"),
        html.P("Welcome to the interactive dashboard! This dashboard provides valuable insights and visualizations based on the suicide, HDI and homicide data collected.", style = {"fontSize" : "20px"}),
        html.P("The goal is to provide you with a user-friendly interface to explore various trends and patterns.", style = {"fontSize" : "20px"}),

        html.H2("Introduction", style={"fontSize": "24px"}),
        html.P("This dashboard consists of several interactive pages, each focusing on different aspects of the data. Below is a brief overview of each page and how to use them:", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("The button of the page that is selected is highlighted on top of the screen.", style={"fontSize": "20px","lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("1. Suicide Map: This page displays a world map with color-coded suicide data points based on the selected indicator.", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("You can choose only single Year value. Country Selector is optional. It highlights selected countries. If no countries are selected all available data is shown.", style={"fontSize": "20px", "lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("2. HDI Map: This page displays a world map with color-coded Human Development Index data points.", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("You can choose only single Year value. Country Selector is optional. It highlights selected countries. If no countries are selected all available data is shown.", style={"fontSize": "20px", "lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("3. Homicide Map: This page displays a world map with color-coded suicide data points based on the selected indicator.", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("You can choose only single Year value. Country Selector is optional. It highlights selected countries. If no countries are selected all available data is shown.", style={"fontSize": "20px", "lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("4. Graphs: This page displays 3 graphs for Suicide, HDI and Homicide data over the Year range.", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("You can choose Year range. Country Selector is mandatory. Selected countries will be shown on the dropdown menu and to the right of the graphs", style={"fontSize": "20px", "lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("5. Charts: This page displays several pie and bar charts. You can choose only single Year value and only single Country value. ", style={"fontSize": "20px","lineHeight": "1.4px"}),
        html.P("First graph shows the distribution of Suicide by the Age group. Next 3 charts display distribution of Suicides, HDI and Homocides by Sex.", style={"fontSize": "20px", "lineHeight": "1.4px"}),
        html.P("Final graph displays the distribution of Suicide data by both Sex and Age group.", style={"fontSize": "20px", "lineHeight": "1.4px", "paddingBottom" : "20px"}),

        html.P("6. About Page: This page offers information about the project, data sources, and sorce code link.", style={"fontSize": "20px", "lineHeight": "1.2px"}),
        html.H2("Data Sources"),
        html.P("All datasets are open-source and used for educational purposes only.", style = {"fontSize" : "20px"}),
        html.Div([
            html.P(html.Strong("WHO Mortality Dataset:"), style={"fontSize": "24px"}),
            html.P("This dataset provides information about mortalities across different countries, genders, and age groups.", style={"fontSize": "20px", "marginTop": "-5px"}),
            html.P(["Available at: ", html.A("WHO Mortality datasets", href="https://www.who.int/data/data-collection-tools/who-mortality-database", target="_blank", style={"fontSize": "20px", "marginBottom": "10px"})]),
            
            html.P(html.Strong("HDI Dataset:"), style={"fontSize": "24px"}),
            html.P("The Human Development Index (HDI) dataset measures a country's overall human development, including factors like life expectancy, education, and income.", style={"fontSize": "20px", "marginTop": "-5px"}),
            html.P(["Available at: ", html.A("HDI downloads", href="https://hdr.undp.org/data-center/documentation-and-downloads", target="_blank", style={"fontSize": "20px", "marginBottom": "10px"})]),
            
            html.P(html.Strong("UNODC Intentional Homicide Dataset:"), style={"fontSize": "24px"}),
            html.P("This dataset contains information about intentional homicide rates in various countries, helping to understand crime trends.", style={"fontSize": "20px", "marginTop": "-5px"}),
            html.P(["Available at: ", html.A("UNODC database", href="https://dataunodc.un.org/dp-intentional-homicide-victims", target="_blank", style={"fontSize": "20px", "marginBottom": "10px"})])
            ]),
        html.H2("Source Code"),
        html.P([
            "Source Code for this website is available on ",
            html.A("GitHub", href="https://github.com/mv686/dashboard", target = "_blank", style = {"fontSize" : "20px"})
        ], style = {"fontSize" : "20px"})
    ]
)

# Add the content to the layout of the About page
layout = about_content
