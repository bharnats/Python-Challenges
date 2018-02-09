# python-challenge
Python Scripts for:

PyBank - Analysing the financial records of a company

Each dataset is composed of two columns: `Date` and `Revenue`. 

create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period
final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


## PyPoll 

### Objective:
The task is to help a small, rural town modernize its vote-counting process. (Up until now, Someone had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

### Exploring the dataset 
* [poll_data](pyPoll/pyPoll.csv)
* Given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`), Each dataset is composed of three columns: 
`Voter ID`, `County`, and `Candidate`.

### Analysis
Python scripts created  that analyzes the votes and calculates each of the following:
* [pyPoll.py](pyPoll/pyPoll.py)
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

### Final Thoughts
* ![Out_py_poll](pyPoll/OutPyPoll.txt)
* The script is able to handle any such similarly-structured dataset in the future (i.e Since I have zero intentions of living in this hillbilly town -- my script needs to work without massive re-writes). In addition, final script prints the analysis to the terminal and exports a text file with the results.


PyParagraph - Automate the analysis of any passage and set metrics for assessing the language complexity
, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

* Import a text file filled with a paragraph of your choosing.

* Assess the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

As an example, this passage:

> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

...would yield these results:

```
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4
```

