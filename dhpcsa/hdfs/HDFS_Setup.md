# HDFS User and Directory Setup

## Steps to Create User and Directory in HDFS

### 1. Create a User `ds1`
```sh
sudo adduser ds1
```

### 2. Create a Directory `ds1-data` in HDFS
```sh

hdfs dfs -mkdir /ds1-data
```

### 3. Make `ds1` User Owner of the Directory
```sh
hdfs dfs -chown ds1 /ds1-data
```

### 4. Login as `ds1` User, Create a File `wordlist.txt` and Copy it to HDFS
```sh
su - ds1
nano wordlist.txt
# Add content to wordlist.txt
hdfs dfs -put wordlist.txt /ds1-data
exit
```

### 5. Create a Group `clients`
```sh
sudo groupadd clients
```

### 6. Create Users `tom` and `jerry` and Add Them to `clients` Group
```sh
sudo adduser --ingroup clients tom 
sudo adduser --ingroup clients jerry

# Alternatively
sudo adduser tom 
sudo adduser jerry
sudo usermod -G clients tom 
sudo usermod -G clients jerry
```

### 7. Create a Directory `Disney` on HDFS
```sh
hdfs dfs -mkdir /Disney
hdfs dfs -chmod 775 /Disney
```

### 8. Allow Users `tom` and `jerry` to Upload Files to `Disney` Folder
```sh
su - tom
hdfs dfs -put tom.txt /Disney
```

## Summary
This guide provides the steps to create users, directories, and set permissions in HDFS to ensure proper access control and file management.
