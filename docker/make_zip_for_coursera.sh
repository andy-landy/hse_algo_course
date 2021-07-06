mkdir temp
cp -r grader temp/grader
cp -r docker temp/docker
cp docker/Dockerfile temp
(
    cd temp
    zip -r ../custom_grader.zip .
)
rm -r temp

