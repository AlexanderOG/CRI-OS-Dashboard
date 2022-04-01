# About the project
This project is intended for the Open Source course at CRI. The main objective is to create an interactive open source dashboard with COVID-19 data.

# Setup
Install conda in your computer
Clone this repo with 
conda create --name dashboard --file requirements.txt python=3.8
conda activate dashboard

If more dependencies are added use:
conda env update --file .\requirements.txt --prune --name dashboard