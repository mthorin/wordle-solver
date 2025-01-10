# wordle-solver

**`wordle_solver.py`** is a Python script to help solve Wordle by filtering possible words based on feedback (green, yellow, and gray letters).

In order to run, a word list text file must be provided as a command line argument.

## Usage
1. Run the script:  
   ```bash
   python wordle_solver.py words.txt
   ```

2. Enter the suggested word into Wordle.

3. Enter feedback:
- Green: Correct letters in position (e.g., a____).
- Yellow: Misplaced letters (e.g., __e_r).
- Gray: Excluded letters (e.g., gt).

3. Repeat

## Requirements
- Python 3.7+

