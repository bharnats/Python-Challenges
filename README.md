# python-challenges
## PyBank 
### Objective:
Analysing the financial records of a company using Python.

### Analysis:
Each dataset is composed of two columns: `Date` and `Revenue`. Created a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

### Results
for [dataSet_1](pyBank/budget_data_1.csv)
```
Financial Analysis
-----------------------------------
Total months: 41
Total Revenue: $18971412
Average Change In Revenue: $30284
Greatest Increase In Revenue: 16-Feb($1837235)
Greatest Decrease In Revenue: 14-Aug($-1779747)
```

for [dataSet_2](pyBank/budget_data_2.csv)
```
Financial Analysis
-----------------------------------
Total months: 86
Total Revenue: $36973911
Average Change In Revenue: $76786
Greatest Increase In Revenue: Jul-14($1645140)
Greatest Decrease In Revenue: Jun-14($-1947745)

```
### Final thoughts:
The final script is able to handle any such similarly structured dataset in the future (developed in such a way that the  script has to work for the ones to come). In addition, to the final script, the analysis is printed to the terminal and exported as a text file with the results.


## PyPoll 
### Objective:
The task is to help a small, rural town modernize its vote-counting process. (Up until now, Someone had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

### Exploring the dataset 
* Given the poll data `pyPoll.csv`, the dataset is composed of three columns: 
`Voter ID`, `County`, and `Candidate`.

### Analysis
Python scripts created  that analyzes the votes and calculates each of the following:
* [pyPoll.py](pyPoll/pyPoll.py)
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

### Results:
```
Election Results
-----------------------------------
Total Votes: 1048575
-----------------------------------
Khan: 63% (661583)
Correy: 20% (209046)
Li: 14% (146360)
O'Tooley: 3% (31586)
--------------------------------
Winner: Khan
```
* The script is able to handle any such similarly-structured dataset in the future (i.e Since I have zero intentions of living in this hillbilly town -- my script needs to work without massive re-writes). 
* In addition, final script prints the analysis to the terminal and exports a text file with the results.


## PyParagraph
### Objective:
Automate the analysis of any passage and set metrics for assessing the language complexity.

### Background
As chief linguistic Analyst, the responsibility includes assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, and worked hard on developing challenging python scripts, I've come up with a fairly simple set of metrics for assessing language complexity.Developed a Python script to automate the analysis of any such passage using these metrics. The python script does the following ::

* Import a text file filled with a paragraph of choice.

* Assess the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

This passage:

> Pollution is bad. Not only does it hinder our breathing, but it also hurts the world. We will not have a place for our children at the current rate of pollution, so pollution is a serious concern. We must pass laws to ensure that factories, cars, and other pollutant-producing agents do not continue to harm our planet. If we stop pollution, then we can have a clean, safe earth to enjoy.

...yields these results:
```
Paragraph Analysis
-----------------------------------
Approximate Word Count: 71
Approximate Sentence Count: 5
Average Letter Count: 4.493
Average Sentence Length: 14.2

