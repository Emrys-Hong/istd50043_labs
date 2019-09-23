# Lab 1 

## Environments
* Ubuntu 16.04 or later
* Python3
* MySQL 5.7

## Python environment
We are using `virtualenv`, so that the code is portable

  `sudo apt-get install virtualenv python3-pip`

## Python libraries
All libraries for this course can be found in the `requirements.txt` file. To install them in your virtualenv:

`pip install -r requirements.txt`

## MySQL installation
Make sure you use `mysql-server-5.7`. During installation, leave the password for root blank. 

To test if successful, try
`mysql -u root`

If you get the console without password. Great!

If not, do the following, which explicitly bypasses root password. 

  ```
  sudo mysql -e 'update mysql.user set plugin = "mysql_native_password" where User="root"'
  sudo mysql -e 'create user "root"@"%" identified by ""'
  sudo mysql -e 'grant all privileges on *.* to "root"@"%" with grant option'
  sudo mysql -e 'flush privileges'
  sudo service mysql restart
  ```

## MySQL examples
Use the `payroll_regist.mysql` scripts to create and populate data for the Payroll and Regist table. 

`mysql -u root -b <dbname> < payroll_regist.mysql`

