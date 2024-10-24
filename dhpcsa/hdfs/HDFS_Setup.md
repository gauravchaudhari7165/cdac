
# HDFS User and Directory Setup
    Create a user by name ds1 
    Create a directory by name ds1-data in HDFS 
    Make ds1 user owner of the above directory 
    Login as ds1 user create a file by name wordlist and copy it to HDFS 
    Create a group by name clients 
    Create Users tom and jerry and add them to clients group 
    Create a directory by name Disney on HDFS 
    Make sure users tom and jerry an upload files to Disney folder


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

#
    Login as ds1 user.
    Create a file hello.txt Type 3 lines into it 
    Then append this data to earlier file uploaded to hdfs by ds1

### 9. Login as `ds1` User 
```sh
su - ds1
```
### 10. Create a File `hello.txt`
```sh
nano hello.txt
```

### 11. Append ItsContent to `wordlist.txt` in HDFS
```sh
hdfs dfs -appendToFile hello.txt /ds1-data/wordlist.txt
exit
```
### 12. Show the content of the append file
```sh
hdfs dfs -cat /ds1.data/wordlist.txt
```

#
    Login as tom user create a folder by name 
    bak in linux Try to copy file upoladed by ds1 
    user from hdfs to back local folder



### 13. Login as `tom` User
```sh
su - tom
```

### 14. Create a Folder `bak` in Linux
```sh
mkdir ~/bak
```

### 15. Copy File Uploaded by `ds1` User from HDFS to `bak` Local Folder
```sh
hdfs dfs -get /ds1-data/wordlist.txt ~/bak/
```