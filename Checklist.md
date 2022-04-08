## Metadata:
- [x] The README.md file is present at the root of the GitHub repo.
- [] The README.md file states where the data come from (with a link to the original repo).
- [x] The README.md file contains guidelines to explicitly install all required dependencies for the project.
- [x] The README.md file contains instructions on how to run the dashboard locally.
- [x] The README.md file contains a link to Streamlit sharing (if relevant).
- [] The README.md file contains a Software Heritage button (link)
- [x] The LICENSE (or LICENSE.txt) file contains a valid open-source license.
- [x] The requirements.txt (for pip) or environment.yml (for conda) file to install all required dependencies.
- [x] The AUTHORS file contains a list of authors.

## Organization:
- [x] Issues are created to list expected features and report bugs.
- [x] Issues are discussed.
- [x] All participants created commits to the project
- [x] Commits address implementation of one feature or fix of one bug at a time.
- [] Commits are (roughly) evenly distributed among project participants.
- [x] New features are implemented in branches and merged through pull requests.

## Data:
- [x] Data file is not stored in the repo and is read on the fly with Pandas.
- [x] A caching mechanism is implemented to prevent downloading the file each time the user interacts with the dashboard.

## Visualization:
- [] Dashboard displays graphics of Covid-19 cases or deaths vs time.
- [] Dashboard displays graphics of Covid-19 cases or deaths for several countries.
- [] Data are normalized with respect to the number of inhabitants per country.
- [] 7-day rolling average for the absolute (non-cumulative) number of cases or deaths.
- [] *Peak (wave) detection is implemented for cumulative number of cases or deaths.*

## Interaction:
- [] User can select which country to display (among a predefined list of countries).
- [] User can display many countries in the same graphic.
- [] User can select to display Covid-19 cases or deaths.
- [] User can select to display or not the 7-day rolling average (for absolute numbers only).
- [] User can select the time frame to display.
- [] *User can select to display or not the peak detection (for cumulative numbers only).*
