[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:76870b1eaab220b1338ce8ec9d35faf0ad100fcb/)](https://archive.softwareheritage.org/swh:1:dir:76870b1eaab220b1338ce8ec9d35faf0ad100fcb;origin=https://github.com/AlexanderOG/CRI-OS-Dashboard;visit=swh:1:snp:b09527df0187ac585bbb887d05fe2d3357f6929c;anchor=swh:1:rev:ca39095f2ea90a21f671471c407ccb7932dc5782)

# About the project
This project is intended for the Open Source course at LPI (previously CRI). The main objective is to create an interactive open source dashboard with COVID-19 data.

# Summary
- [Understand the Files](#understand-the-files)
- [Setup](#setup)
- [Run the example](#run-the-example)
- [Run the COVID-19 dasboard](#run-the-covid-19-dasboard)
- [References](#references)
- [Live project](#live-project)

# Understand the Files
- [ReadME](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/README.md): everything you need to know about this project and how to navigate through our repository!
- [License](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/LICENSE): Simple automatically generated GitHub file containing the referencing of the type of lIcense choosen for this project (in our case MIT license)
- [Basic plot](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/basic_plot.ipynb): Here is the link to our testing Notebook that will later be removed
- [Covid Dasboard](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/cov_dashboard.py): Here you will find our python script that generates our interactive dashboard using streamlit.
- [Dashboard Example](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/dashboardExample.py): Here is a link to a basic dashboard example that we might remove in the future, you can find the reference in Reference bellow!
- [Load Data](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/loadData.py): Here we use Pandas to load the dataset from URL (not from predownload datasets)
- [Requirement](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/requirements.txt): Here you will find the required dependencies that will be installed during the setup of our vrtual environement using Conda
- [Authors](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/AUTHORS.md): contains informtation about the 3 contributors of this project.
- [Checklist](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/Checklist.md): Contains the checklist for this project evaluation.


# Data Source
Our complete COVID-19 dataset is a collection of the COVID-19 data maintained by [World in Data](https://ourworldindata.org/coronavirus). Its being updated daily throughout the duration of the COVID-19 pandemic (more information on our updating process and schedule [here](https://covid-docs.ourworldindata.org/en/latest/data-pipeline.html#overview)). 

It includes the following data:

| Metrics                     | Source                                                    | Updated | Countries |
|-----------------------------|-----------------------------------------------------------|---------|-----------|
| Vaccinations                | Official data collated by the Our World in Data team      | Every weekday   | 218       |
| Tests & positivity          | Official data collated by the Our World in Data team      | Weekly  | 183       |
| Hospital & ICU              | Official data collated by the Our World in Data team      | Daily   | 47        |
| Confirmed cases             | JHU CSSE COVID-19 Data                                    | Daily   | 216        |
| Confirmed deaths            | JHU CSSE COVID-19 Data                                    | Daily   | 216       |
| Reproduction rate           | Arroyo-Marioli F, Bullano F, Kucinskas S, Rondón-Moreno C | Daily   | 192        |
| Policy responses            | Oxford COVID-19 Government Response Tracker               | Daily   | 187        |
| Other variables of interest | International organizations (UN, World Bank, OECD, IHME…) | Fixed   | 241       |

more information regarding the data source and detailed header description of data, pleasre refere [here](https://github.com/owid/covid-19-data/tree/master/public/data)

# Setup
Install conda in your computer, you can find instructions for each operating system in the [Conda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Clone this repo and move into the directory with:
```
git clone https://github.com/AlexanderOG/CRI-OS-Dashboard
cd CRI-OS-Dashboard
```

Then create a virtual enviroment:
``` 
conda create --name dashboard python=3.8
conda activate dashboard
python -m pip install -r requirements.txt
```
The requirements file containes the libraries and dependencies that are to be installed on our environement.

If more dependencies are added use:
```
pip install --upgrade --force-reinstall -r requirements.txt
```

# Run the example
To run the example dashboard you need to enter the following command in Windows:
```
streamlit run .\dashboardExample.py 
```
For MacOS and Linux user, remove ``` .\ ```

# Run the COVID-19 dasboard
To run the COVID-19 dashboard you need to enter the following command:
```
streamlit run .\cov_dashboard.py 
```

# Live project
You can see the project live hosted on Streamlit cloud [here](https://share.streamlit.io/alexanderog/cri-os-dashboard/main/cov_dashboard.py)

# References
[Strimlit dashboard example](https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)
