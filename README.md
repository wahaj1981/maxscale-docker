# Real World Project: Database Shard

# Objectives:
- Develop a Docker Compose application to deploy a shared database environment.
- Create a Python script to connect to the shared setup, perform queries, and showcase the merged database functionality.
- Supply all required files along with clear, comprehensive instructions in a GitHub repository.


## Install the following required tools on Linux Ubuntu: 
- Docker compose
  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04
```
  sudo apt install docker-compose
```

- Install MySQL Connector
```
sudo apt install python3-pip
pip3 install mysql-connector
```

  
- MariaDB
  https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04
```
sudo apt install mariadb-client
```
- Run Linux update
```
sudo apt update
sudo apt upgrade -y
```

## Create Maxscale Container
- Clone the maxscale-docker repository:
```
git clone https://github.com/zohan/maxscale-docker/
```
- Then
```
cd maxscale-docker/maxscale
```
```
docker-compose up -d
```







  - Python
  https://www.askpython.com/python-modules/tabulate-tables-in-python
```
```

- Using Maxscale (Sharded Database Architecture)  https://mariadb.com/products/enterprise/components/#maxscale

## Step-by-step instructions: Run the following command in the terminal.
```
sudo apt install docker-compose
```
* Install MariaDB Connector
```
sudo apt install python3-pip
pip3 install mysql-connector
```
* Install MariaDB
```
sudo apt install mariadb-client
```
* Update Linux
```
sudo apt update
sudo apt upgrade
```

```
docker-compose build
docker-compose up -d
```

After MaxScale and the servers have started (takes a few minutes), you can find
the readwritesplit router on port 4006 and the readconnroute on port 4008. The
user `maxuser` with the password `maxpwd` can be used to test the cluster.
Assuming the mariadb client is installed on the host machine:
```
$ mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4006 test
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 10.2.12 2.2.9-maxscale mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [test]>
```
You can edit the [`maxscale.cnf.d/example.cnf`](./maxscale.cnf.d/example.cnf)
file and recreate the MaxScale container to change the configuration.

To stop the containers, execute the following command. Optionally, use the -v
flag to also remove the volumes.

To run maxctrl in the container to see the status of the cluster:
```
$ docker-compose exec maxscale maxctrl list servers
```
```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────────┬─────────────────┐
│ Server  │ Address  │ Port │ Connections │ State           │ GTID     │ Monitor         │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server1 │ primary1 │ 3306 │ 0           │ Master, Running │ 0-3000-6 │ MariaDB-Monitor │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server2 │ primary2 │ 3306 │ 0           │ Running         │ 0-3001-4 │ MariaDB-Monitor │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────────┴─────────────────┘
```

