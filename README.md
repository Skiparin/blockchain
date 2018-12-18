# blockchain

Group: Ørvur Guttesen, Tim Hemmingsen, Nicolai Mikkelsen, Laura Hartig & Michael Daugbjerg.

---

## How to reporduce the setup

First go to the directory of your choise.

To clone the project type:
```
git clone https://github.com/Skiparin/blockchain
```

Now you will have the project on the machines.

Then enter the folder:
```
cd blockchain/
```

Inside the folder you will have two docker files `Dockerfile` and `docker-compose.yml`. These are the files we will use to setup the inveioment with the four p2p nodes.

So now you want to build your image: (It is important that you do this inside the blockchain folder, and dont forget the `.` at the end!)
```
docker build -t blockchain .
``` 

Confirm the image: 
```
docker images
```
check for the image with the name `blockchain`.

Now that you got your images you can get your docker containers up and running.
To run the docker-compose type:
```
docker-compose up -d
```

The `-d` tells docker to run the container detached.

Check for the four contianers:
```
docker ps -a
```

This will list all containers, you should see four containers named: peer1, peer2, peer3 and peer4.

## Sources

Link, description (wisiting date)

- http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/?fbclid=IwAR0PJirurp00Pj4OdxDjqktRtKgTjcHB55mC_-CumJPKa-QnbyENWWzL0Ms, A Practical Introduction to Blockchain with Python (16-12-2018)


- https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b?fbclid=IwAR1lvlgLq-sazc0l7U-DPSs0c-ypJUleEDBZLBZkLkAk-1D-9scJ279BZs8, Let’s Build the Tiniest Blockchain (17-12-2018)

- https://forums.docker.com/t/accessing-host-machine-from-within-docker-container/14248/4?fbclid=IwAR2uzLnXZfA60TFvS_c_e8OF4QU9Pq7Co-knZuBjF8NKNZJWIBqUhS_tpfM, Accessing host machine from within docker container (17-12-2018)
