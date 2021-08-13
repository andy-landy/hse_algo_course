mkdir -p shared
rm -rf shared/*
cp ../problems_git/problems/lamps/lamps.py submission/solution.py
docker run -it --mount src=$(realpath ./submission/),dst=/shared/submission,type=bind -e partId=jEQnE grader
