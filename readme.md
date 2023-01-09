## Bank security console

This is educational project which emulates active passes to bank storage, persons in storage, time of each visit and if such visit was suspicious. By default supicious visit is any visit with duration over 60 minutes.

### How to install

#### Env variables to be setup:

> django version 3.2.* 
> 
> environs version 9.5.*: is library for parsing environment variables
> 
> psycopg2 version 2.9.*: is the most popular PostgreSQL database adapter
> 
> Variables: 
> 
> DB_ENGINE storage engine  
> DB_HOST Django hosting  
> DB_PORT    
> DB_NAME  
> DB_USER   username  
> DB_PASSWORD  user password  
> SECRET_KEY By default = REPLACE_ME   
> debug  By default = True

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

``` pip install -r requirements.txt ```

_Important: This does not run at Django 4.*_

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
