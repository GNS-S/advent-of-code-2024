# Advent of Code 2024 solutions
Written and formatted in a way that makes sense to me

### Running the code
Puzzle texts and inputs can be found at [https://adventofcode.com/2024](https://adventofcode.com/2024)

Every `{day number}` folder expects an additional file inside titled `input.txt` with the input

Running instructions: 

* Navigate to a day folder: `cd {day number}`
* Create and fill an `input.txt` (or change the INPUT_PATH constant in source)
* Run the appropriate part file via python: `python3 part{1 or 2}.py`

If a solution uses numpy, you will need to either install it globally:

* `pip install -r requirements.txt`

Or create a virtual environment for this repo and install it there

* Create a virtual environment: `python3 -m venv venv/aoc202`
* Active the environment via (Unix/MaxOS) `source tutorial-env/bin/activate`, or (Windows) `.\venv\aoc2024\Scripts\activate`
* Install the dependencies: `pip install -r requirements.txt`
* Run `deactivate` once you are done using the environment