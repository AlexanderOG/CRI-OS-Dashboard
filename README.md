# About the project
This project is intended for the Open Source course at CRI. The main objective is to create an interactive open source dashboard with COVID-19 data.

# Understand the Files
- [ReadME](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/README.md): everything you need to know about this project and how to naigate through our repository!
- [License](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/LICENSE): Simple automatically generated GitHub file containing the referencing of the type of lIcense choosen for this project (in our case MIT license)
- [Basic plot](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/basic_plot.ipynb): Here is the link to our testing Notebook that will later be removed
- [Covid Dasboard](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/cov_dashboard.py): Here you will find our python script that generates our interactive dashboard using streamlit.
- [Dashboard Example](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/dashboardExample.py): Here is a link to a basic dashboard example that we might remove in the future, you can find the reference in Reference bellow!
- [Load Data](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/loadData.py): Here we use Pandas to load the dataset from URL (not from predownload datasets)
- [Requirement](https://github.com/AlexanderOG/CRI-OS-Dashboard/blob/main/requirements.txt): Here you will find the required dependencies that will be installed during the setup of our vrtual environement using Conda

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

If more dependencies are added use:
```
pip install --upgrade --force-reinstall -r requirements.txt
```

# Run the example
To run the example dashboard you need to enter the following command:
```
streamlit run .\dashboardExample.py 
```

# Run the COVID-19 dasboard
To run the COVID-19 dashboard you need to enter the following command:
```
streamlit run .\cov_dashboard.py 
```

# Live project
You can see the project live hosted on Streamlit cloud [here](https://share.streamlit.io/alexanderog/cri-os-dashboard/main/cov_dashboard.py)

# References
[Strimlit dashboard example](https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)