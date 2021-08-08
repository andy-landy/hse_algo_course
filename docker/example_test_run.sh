mkdir -p shared
cp grader/problems/lamps_solution.py shared/solution.py
docker run -it --mount src=/abs/path/to/shared,dst=/shared/submission,type=bind hse qwe123
