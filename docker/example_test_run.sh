mkdir -p shared
rm -rf shared/*
cp ../problems_git/problems/appr_tsp/appr_tsp.py shared/solution.py
docker run -it --mount src=$(realpath ./submission/),dst=/shared/submission,type=bind -e partId=123 grader
