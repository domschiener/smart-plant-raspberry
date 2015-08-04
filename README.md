# Smart Plant for your Raspberry Pi

This is a project that intends to make your plant smarter (and perhaps prettier, if you start watering more regularly). With a Raspberry Pi, a Moisture Sensor and this software we are able to track our plants needs for water in regular intervals and even communicate with it through Twitter. The purpose of this project is it to make it easier for some of the busy people out there to water their plants. 

## Prerequisites

**Hardware:**
* Raspberry Pi (full setup)
* Moisture Sensor
* MCP3008
* Breadboard with Female-to-Male and Male-to-Male jumper wires

## Tutorial

Here is a comprehensive Tutorial on setting it all up: 

## How it works
On the Python side, we have a wrapper function in main.py which creates two asynchonously running processes through the multiprocessing library. These processes are twitter.py and getdata.py. twitter.py is there to continuously check for new Tweets to our plant so that once we send a tweet to our plant it can respond with the current moisture data and tell its owner (you) how it's feeling. getdata.py collects data of your plant in 30 minutes cycles and saves it to data.csv.
When these processes are running we are creating a temporary file called RUNNING.txt which allows the frontend to determine whether the scripts are currently running.

On the frontend we are simply using bootstrap for the website together with some D3.js visualization for our data. 

# Required Setup

For this tutorial you will need to have a fully functional LAMP server setup on your Raspberry Pi that is able to run CGI/Python scripts. We additionally need to install SpiDev so that we can communicate with the Pi's SPI. 

## Installing Apache
```
sudo apt-get install apache2
```

## Enabling Python on Apache Server

```
sudo apt-get install python-setuptools libapache2-mod-wsgi
```

Once that is completed type in: > sudo nano /etc/apache2/sites-available/default

Then change the current <Directory /var/www/> to:
```
<Directory /var/www/>
	Options ExecCGI Indexes FollowSymLinks MultiViews
	AllowOverride None
	Order allow, deny
	allow from all
	AddHandler cgi-script.py
<Directory>
```
Now you should be able to run Python scripts in your /var/www folder. 

## SpiDev and Python-dev

Install Python-dev
```
sudo apt-get install python-dev 
```

Now we need to enable the SPI communication on our Raspberry Pi, which is pretty straight forward. Just head to the following link and follow its steps: http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/

After you have successfully restarted your Raspberry Pi, type in:
```
cd ~
git clone https://github.com/Gadgetoid/py-spidev
cd py-spidev/
sudo python setup.py install
```

Now you should be able to run the testversion.py which is a small program that shows the Moisture of your plant. To do so, first clone the entire repository and then run testversion.py:
```
git clone https://github.com/domschiener/smart-plant-raspberry
cd smart-plant-raspberry
sudo python testversion.py
```

And the output should look something like this:

Now copy the contents of smart-plant-raspberry to your /var/www folder and you should be ready to go. Last thing to change is the permissions, which are quickly changed:
```
sudo adduser www-data spi

sudo adduser <username> www-data 
sudo chown -R :www-data /var/www 
sudo chmod -R g+rw /var/www
```

Now also change the permissions of your JS/CSS folder to 755 and of all the files inside that folder to 655 (you can just do it recursively). 

## Creating a Twitter Application and Installing Tweepy

Before we can get started, we still need to enable the Twitter bot to work. First of all we will need to create a new Twitter account for our plant. Since you actually care about your plant (else you wouldn’t follow this tutorial), take a profile picture for it as well and add some details (you can check out my plant over here: https://twitter.com/domsplant).

Once that is done, we will need to setup an application so that our plant (or rather the Raspberry Pi) can login to the Twitter account and communicate through it with OAuth. Go to https://apps.twitter.com/app/new and setup a new application for your plant (keep in mind, you need to be logged in with your plants Twitter account). Once that is done copy the API information (token and secret) to your twitter.py file. New we just need to install Tweepy:
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```

If you see an SSL error, run the following command:
```
sudo pip install requests[security]
```

## Running the program
Now you can either start it all by running

> sudo python main.py 

(which in turn will asynchronously run twitter.py and getdata.py), or you can simply go to http://localhost/ and operate the sensor through the panel. On top of the page you can turn the sensor online or offline. 
