I rarely get more than a week or two into AoC before getting too busy, so these folders aren't complete.

All in Python so far.

### How to use

1. create a new folder for the day you're solving. See 'How to use new_day.sh' section below.
2. copy example data into example.txt
3. replace `???` in script with example answer from AoC page
4. copy real data into data.txt
5. write code in functions `part1` and `part2` of the script for each part of the problem

Running `python script.py` will run your `part1` function against the data in example.txt and assert that your solution matches the example answer. If it does, it will go on to load the real problem data and print out the result of running your `part1` and `part2` functions on this data, to be submitted into the AoC UI.

### Utils

* `template_script.py`: a template script for each day's exercise
* `utils.py`: some functions that are useful in AoC, e.g. loading input data from file

### How to use new_day.sh

If you don't already have a root level directory for the year you're working on, create that.

The following command will create a new directory 'day2' in the '2021' folder and populate it with files for data.txt, example.txt and the template script.

`./new_day.sh 2021 day2`

