# Create a user by name ds1
``` bash
sudo useradd ds1
```
# Create a directory by name ds1-data in HDFS
``` bash
hdfs dfs -mkdir /user/ds1-data
```

# Make ds1 user owner of the above directory
``` bash
hdfs dfs -chown ds1 /user/ds1-data
```

# Login as ds1 user and create a file by name wordlist
``` bash
sudo su - ds1
echo "sample data" > wordlist
```

# Copy the file to HDFS
``` bash
hdfs dfs -put wordlist /user/ds1-data/
```

# Create a group by name clients
``` bash
sudo groupadd clients
```
# Create users tom and jerry and add them to clients group
``` bash
sudo useradd -G clients tom
sudo useradd -G clients jerry
```

# Create a directory by name Disney on HDFS
``` bash
hdfs dfs -mkdir /user/Disney
```

# Make sure users tom and jerry can upload files to Disney folder
``` bash
hdfs dfs -chown :clients /user/Disney
hdfs dfs -chmod 770 /user/Disney
```
