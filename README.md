# Real World Project: Database Shard

# Objectives:
- Develop a Docker Compose application to deploy a shared database environment.
- Create a Python script to connect to the shared setup, perform queries, and showcase the merged database functionality.
- Supply all required files along with clear, comprehensive instructions in a GitHub repository.


## Prerequisites: to successfully complete the project, ensure the following components are installed on Linux Ubuntu

1- Docker compose   https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04
- First, run update
```
sudo apt update
sudo apt upgrade -y
```
```
  sudo apt install docker-compose
```

2- Install MySQL Connector for Python:
```
sudo apt install python3-pip
pip3 install mysql-connector
```
  
3- MariaDB
  https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04
```
sudo apt install mariadb-client
```
- Run Linux update
```
sudo apt update
sudo apt upgrade -y
```
4- Create MaxScale Container by clone the maxscale-docker repository:
```
git clone https://github.com/zohan/maxscale-docker/
```
5- MaxScale Configuration and Setup:
- Navigate to the maxscale directory.
```
cd maxscale-docker/maxscale
```
- Start the cluster

```
docker-compose up -d
```
- Check Cluster Status, to verify the status of the MaxScale container
```
docker-compose exec maxscale maxctrl list servers
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────────┬─────────────────┐
│ Server  │ Address  │ Port │ Connections │ State           │ GTID     │ Monitor         │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server1 │ primary1 │ 3306 │ 0           │ Master, Running │ 0-3000-6 │ MariaDB-Monitor │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server2 │ primary2 │ 3306 │ 0           │ Running         │ 0-3001-4 │ MariaDB-Monitor │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────────┴─────────────────┘
```



6- Python
  https://www.askpython.com/python-modules/tabulate-tables-in-python
- Install the tabulate module to display results in a tabular format
```
sudo apt-get install python3-tabulate
```
- Identify the IP address of the MaxScale container
```
docker inspect maxscale-maxscale-1
```
7- Connecting to MariaDB
```
mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```

## Running the Python Script :
- The Python script will connect to the MaxScale server and execute queries to demonstrate the behavior of a sharded database
```
python3 code.py
```
  
## The script will return data for several queries
- Largest Zipcode in zipcodes_one
47750
- All Zipcodes in Kentucky (KY)
  

- All zipcodes where state = KY:

+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 41503 | 42201 | 42202 | 42120 | 40801 | 42602 | 41601 | 42204 | 42020 | 42603 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 42122 | 40402 | 41121 | 40902 | 42021 | 40903 | 41712 | 41512 | 40803 | 41101 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 41102 | 41105 | 41114 | 42206 | 42123 | 41602 | 41713 | 40003 | 42022 | 41603 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```


