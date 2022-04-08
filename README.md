# About the project
This project is intended for the Open Source course at CRI. The main objective is to create an interactive open source dashboard with COVID-19 data.

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