# CAMCA-Dockerization
 Dockerization example


1. Login to GPU server 
2. Create the Projects and Dataset folder under username
3. Locate the code and dockerfile under specific project folder.
4. Build Docker container using \
"sudo docker build -f ./dockerfile  -t hellocamca ./"
5. Run hellocamca image with mounting a folder of GPU server as "external_folder" \
"sudo docker run --rm --gpus all -v /home/local/PARTNERS/sy1045/:/external_folder hellocamca"
