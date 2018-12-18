# blockchain

Group: Ørvur Guttesen, Tim Hemmingsen, Nicolai Mikkelsen, Laura Hartig & Michael Daugbjerg.

---

## Requirements

### Become a peer

- flask

- requests

### For reproduction
- docker

- docker-compose

### Clone the project

First go to the directory of your choise.

To clone the project type:
```
git clone https://github.com/Skiparin/blockchain
```

Now you will have the project on the machine.

Then enter the folder:
```
cd blockchain/
```

## How to reporduce the setup

First follow the steps under 'How to become a peer' called 'Clone the project' 

Inside the folder you will have two docker files `Dockerfile` and `docker-compose.yml`. These are the files we will use to setup the inveioment with the four p2p nodes.

So now you want to build your image: (It is important that you do this inside the blockchain folder, and dont forget the `.` at the end!)
```
docker build -t blockchain_image .
``` 

Confirm the image: 
```
docker images
```
check for the image with the name `blockchain_image`.

Now we need to setup the network in order to make the peer to peer section work:

```
docker network create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1 dockernet
```

To check that it worked type:

```
docker network ls
```

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

This will list all containers, you should see four containers named: bc_one, bc_two, bc_three, bc_four.

### Docker containers

Names: bc_one, bc_two, bc_three, bc_four.

Ports: 5001, 5002, 5003, 5004.

## How to become a peer

### Run the application

Inside the `blockchain` folder type:
```
python3 endpoints.py
```

Open a new terminal:

```
curl -d '{"key":<connection>, "value":<ip>} -X POST http://localhost:5001/join_network'
```

You can also curl to another container using a given port (See under "Docker containers")


### Endpoints

- /validate_block [POST]

Send a block as json. Example:

{
        "blocknumber": 1,
        "data": [
            {
                "from": "Hans",
                "message": "Hello Emil",
                "to": "Emil"
            },
            {
                "from": "Emil",
                "message": "Hello Hans",
                "to": "Hans"
            }
        ],
        "hash": "00003749bba2d17913b31342bd3a644f29ae9897fa67a17eaa68d54ed3482a91",
        "nounce": 109507,
        "old_hash": "0000e35b7ff1b88879dc3fad7fc7e85a5f354c806b7c17b684ab10cb53a817b5"
}

- /transactions/new [POST] 

Send a transaction as json. Example:

{
  "from":"Emil",
  "to":"Hans",
  "message":"Hello Hans"
}

- /transactions/get [GET]

No params required.

- /mine [POST]

No params required.

- /chain/get [GET]

No params required.

- /block/latest [GET]

No params required.

- /join_network [POST]

Send json with connection to where an application is running. Example:

{"connection": "http://192.168.0.1:5001"}

- /delete_info [GET]

No params required.

## Sources

Link, description (wisiting date)

- http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/?fbclid=IwAR0PJirurp00Pj4OdxDjqktRtKgTjcHB55mC_-CumJPKa-QnbyENWWzL0Ms, A Practical Introduction to Blockchain with Python (16-12-2018)


- https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b?fbclid=IwAR1lvlgLq-sazc0l7U-DPSs0c-ypJUleEDBZLBZkLkAk-1D-9scJ279BZs8, Let’s Build the Tiniest Blockchain (17-12-2018)

- https://forums.docker.com/t/accessing-host-machine-from-within-docker-container/14248/4?fbclid=IwAR2uzLnXZfA60TFvS_c_e8OF4QU9Pq7Co-knZuBjF8NKNZJWIBqUhS_tpfM, Accessing host machine from within docker container (17-12-2018)
