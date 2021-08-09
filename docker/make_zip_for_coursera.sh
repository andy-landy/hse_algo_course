mkdir temp
cp -r grader temp/
cp -r docker temp/
cp -r problem temp/
cp docker/Dockerfile temp
(
    cd temp
    zip -r - .
)
rm -r temp

