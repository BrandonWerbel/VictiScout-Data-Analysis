# VictiScout Data Analysis

Repository to hold scripts for analyzing data from [Victiscout](https://github.com/frc1418/VictiScout)

## Steps to using this repository
1. add VictiScout csv files into a new `scouting-data-files` directory. *Make sure the directory is called this, or the scripts will not work* 
2. `pip3 install -r requirements.txt`: install necessary python modules
3. `cd scripts`: access python scripts
4. `python3 compile-data.py`: create single file to hold all scouting data
5. `python3 sort_by_team.py`: sort matches by team in new JSON file