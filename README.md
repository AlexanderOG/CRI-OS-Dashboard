# About the project
This project is intended for the Open Source course at CRI. The main objective is to create an interactive open source dashboard with COVID-19 data.

# Setup
Install conda in your computer, you can find instructions for each operating system in the [Conda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Clone this repo with `git clone https://github.com/AlexanderOG/CRI-OS-Dashboard`
Then create a virtual enviroment.
``` 
conda create --name dashboard --file requirements.txt python=3.8
conda activate dashboard
```

If more dependencies are added use:
conda env update --file .\requirements.txt --prune --name dashboard 