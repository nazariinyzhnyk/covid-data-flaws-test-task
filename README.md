# COVID-19 test task

## My solution

To reproduce:
- download data from link (see Data chapter)
- copy data from <i>csse_covid_19_daily_reports</i> to <i>data</i> dir
- install requirements from [requirements.txt](requirements.txt) 
(could use Pipenv with pipfile, but for this project I just decided to stick to virtualenv)
- run [data_merge.py](flaws_correction/data_merge.py) in order to get a single file for each country with
all necessary aggregated info. in addition, file with Latitude and Longitude will be generated containing info 
about countries coordinates. with this file we'll be able to aggregate info about situation with COVID for each 
country using neighbouring countries
- go to [test_task_solution.ipynb](test_task_solution.ipynb) and run code cell by cell
- all custom data flaws correction modules are developed and stored in
[flaws_correction](flaws_correction) python package - this is the one that should be used
later on in production if needed

## Task description

The Covid-19 virus was found first in 2019, 
then spread worldwide in 2020. 
Initially, most countries weren’t ready for such an 
epidemic, so even the data gathered contained many flaws
in it.

On the other hand, having the ability to predict 
the number of infected citizens on a daily basis can 
have a huge impact on decision-making and could save 
lives.

## Data

[Link to download](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).

~7Gb if cloning the whole repository.

Load the first 6 months of the data.

## Tasks

1. You’re given raw data that contains many flaws. 
Please find 5 different flaws in the data and fix them. 
Try to find the most important flaws that require 
to be fixed in order to enable forecasting (task 2).
2. Please describe (no code is needed) what will be 
the process required for forecasting the future number 
of active patients per country.

## Task goals

1. Understanding the quality of your coding skills. 
We do not expect this code to be production-ready, but production oriented. 
It means we expect organized code that will require minimal refactoring to be 
used as part of a daily forecasting production code.
2. Understanding the way you think, analyze, and tackle data flaws.
3. Examine your creativity and ML knowledge.
