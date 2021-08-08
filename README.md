a better alternative to https://github.com/coursera/programming-assignments-demo

### What does this code do for you

- a lib for grading
- a docker tools to pack the lib along with your code
- all you have to implement is the problem-specific code

### How to create a grader for a single problem or for several problems

Please address the exaples dir for example graders. 

- implement some problem-specific code:
    - answer checker(s) in case it's not trivial comparison with exact answer
    - input and correct answer generators
- save generated inputs to files 
- add a run command to docker/entrypoint.sh, e.g. add `if __name__ == '__main__'` code to one of your files and run it with `python3 problem1.py`


