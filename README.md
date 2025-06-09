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
```
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 41503 | 42201 | 42202 | 42120 | 40801 | 42602 | 41601 | 42204 | 42020 | 42603 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 42122 | 40402 | 41121 | 40902 | 42021 | 40903 | 41712 | 41512 | 40803 | 41101 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 41102 | 41105 | 41114 | 42206 | 42123 | 41602 | 41713 | 40003 | 42022 | 41603 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```
- All Zipcodes Between 40000 and 41000:
```
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 40801 | 40402 | 40902 | 40903 | 40803 | 40003 | 40906 | 40946 | 40004 | 40104 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 40806 | 40006 | 40807 | 40403 | 40404 | 40007 | 40913 | 40914 | 40405 | 40808 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 40915 | 40810 | 40816 | 40008 | 40107 | 40009 | 40108 | 40409 | 40109 | 40921 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 40410 | 40010 | 40310 | 40813 | 40011 | 40075 | 40376 | 40923 | 40311 | 40350 |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```
- Total Wages for Pennsylvania (PA):
```
+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
|   11966378 |   62923182 |    7908593 |    8273435 |   13678147 |   57568042 |   34233845 |  565791203 |  667346676 |  428649297 |
+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
|  379642102 |    4377418 |   22945575 |  166009726 |   25192378 |  244184876 |   16182812 |   24607804 |   11909237 |   14895510 |
+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
|   61800486 |   36624538 |  213188865 |   81026002 |   10154710 |  304377640 |   10079246 |  456509722 |  168742357 |   31979307 |
+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
|  386411937 |  276106055 |   38542847 |   54055867 |   72863036 |   21760172 |  702813430 |    6820827 |    9178957 |  152126652 |
+------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+

```
## Stopping the Cluster
```
docker-compose stop
```
## Removing the Cluster
```
docker-compose down -v
```
