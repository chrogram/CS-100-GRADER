# CS 100 ZyBooks Grading Script

## Setup
1. Using your command line clone this repo via `git clone whateverthisrepourlis`
1. Download your section student's myBama ID's via BlackBoard.
2. Paste them into `students.txt` in the root of this repo. Example in `examples/students-ex.txt`
3. Make sure to include 01supesupport_previewuser.

## Usage
1. Place the ZyBook CSV reports in the `toGrade` folder.
2. In the repo run `python3 grader.py` via the command line.
3. When prompted input which assignment type to be graded.
4. Input in the assignment number in XX format (e.g. `01`, `05`, `11`). 
5. Input in the CSV of the file to be graded (e.g. `UACS100Spring2024_Reading_HW01_report_2024-02-01_2259.csv`).
6. If grading is successful, then `Graded successfully` will appear. If not then `File not found` will appear.
7. At this point you can exit the program by `ctrl+c` or entering `0` at the prompt.
8. The graded and filtered files will show in either the `LAB`, `HW`, etc. folder as a CSV with the assignment number. Examples of what this looks like can be found in `examples/LAB`
9. You can paste the last column of the graded CSV into the offline BlackBoard report, but make sure the columns fit as there's a problem with a person in my section not signing up to ZyBooks.
10. ==**MAKE SURE GRADES MATCH UP WITH STUDENTS**==


## To-do
- add support for projects and exams
- filter out students that have dropped
- GUI(?)
- refactor some of the names
- rewrite this in Rust lol


### Notes
* Periodically run `git pull orgin master` to make sure everything is up to date. I'll update the group chat when major updates are made.
* Please inform me of any bugs with the software.
* Let me know if you have any questions.