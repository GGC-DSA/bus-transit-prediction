
# This is the tutorial document this shows how we developed our webserver with Nginx, Flask, and uWSGI.

**References**
 This tutorial is a amalgam of tutorials I used to build our project. 
  -  https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
  - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
  - https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
  - https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04

**Prereqs**
1. Create or have a ubuntu linux server with version **20.04**
	If you are using AWS (like we did initially) you need a t2.medium or better memory wise
2. Have appropriate permissions to perform sudo operations on the server (for AWS make sure you have your      	 pem file for ssh)

**Part 1 (installing nginx and initial firewall config)**

1. Update your server 
             `sudo apt update`
             
2. Install nginx             
             `sudo apt install nginx`

3. Adjust default firewall
            `sudo ufw app list`
            You should see the following
```
Output
 
Available applications:
Nginx Full
Nginx HTTP
Nginx HTTPS
OpenSSH
```


    Enter the following `sudo ufw allow 'Nginx HTTP'` and `sudo ufw allow 'OpenSSH'`
    To ensure the port was properly opened use `sudo ufw status`
    And you should see something like this
```sh
Output
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere                  
Nginx HTTP                 ALLOW       Anywhere                  
OpenSSH (v6)               ALLOW       Anywhere (v6)             
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
```
     If you do not see the above you need to run `sudo ufw enable` then check again to see if the ufw firewall is active. 
     IMPORTANT (Make sure you limit ssh to only specifically your IP address as this is a vulnerability) 
       This can be done through the AWS console with the "myIP" option, or locally through your network and or ufw firewall settings. 

4. Run `systemctl status nginx` (you may need to install the systemctl utility `  
sudo apt-get install -y systemd` with that)

You should get output that looks like this:

```sh
Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: en
   Active: active (running) since Wed 2021-05-12 10:59:41 EDT; 16min ago
     Docs: man:nginx(8)
  Process: 12160 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (cod
  Process: 12159 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process
 Main PID: 12161 (nginx)
    Tasks: 13 (limit: 4915)
   CGroup: /system.slice/nginx.service
           ├─12161 nginx: master process /usr/sbin/nginx -g daemon on; master_pr
           ├─12162 nginx: worker process
           ├─12163 nginx: worker process
           ├─12164 nginx: worker process
```
5. Test the nginx install 

If you are doing this locally go to  `localhost:80`

If you are doing this on aws go to `http://aws_external_ip:80`
(make sure you allow port 80 to your ip address or globally through the AWS console
tutorial here:  https://stackoverflow.com/questions/5004159/opening-port-80-ec2-amazon-web-services)

Afterwards you should see something that looks like this 

![blah](https://i.imgur.com/l5Q6OWe.png)

**Part 2 (Configuring Nginx and Flask)**


6. Now we need to install python specifically `(3.7.6)` we are going to do this the easy way with the deadsnakes repository 
```sh
sudo add-apt-repository ppa:deadsnakes/ppa
```
Press Enter when prompted. 

---
7. Next we install the specific version of python we are using
```sh
sudo apt install python3.7
```
This should install python `3.7.6 or 3.7.10` if it does not it is likely the deadsnakes repo has been updated look there and you should be able to find the proper command to install this version. 

----
8. Create the Python Virtual Env  (using venv)

 First install venv for 3.7  `sudo apt install python3.7-venv`
 
 Create the Environment `python3.7 -m venv projenv`
 
 Activate the Environment `source projenv/bin/activate`
 
 Then you should see  `(projenv)` in front of your path on terminal, this means your env is active
 
 ---
 9. Install packages
 
 First install some base utilities
 ```sh
 sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
 ```
 Next we upgrade pip `pip install --upgrade pip`
 Now we install wheel `pip install wheel`

---
**(make sure to do these steps  before installing uwsgi and flask)**
Install python 3.5 dev tools to build uwsgi `sudo apt-get install python3.5-dev`

Now We need to change the version of `gcc` we are using to 4.8 because there is a bug with venv, gcc5, and uwsgi. To do this we do the following steps 

```sh
ls /usr/bin/gcc* -l 

sudo apt-get  install gcc-4.8

sudo rm /usr/bin/gcc

sudo ln -s /usr/bin/gcc-4.8 /usr/bin/gcc
```

---

uwsgi and flask `pip install uwsgi flask`
