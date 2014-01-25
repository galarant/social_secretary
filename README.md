Social Secretary
================
Social Secretary is a notification system that helps you manage your social network.

Users connect via Facebook and categorize / sort their friends. Social Secretary then sends the users reminders via email when they are starting to mis-manage their personal and business contacts (i.e. falling out of touch with a contact, forgetting to reply, etc).


Installation and Setup
----------------------

1. Install Python 2.x, MySQL 5.x, Python virtualenv and Python virtualenvwrapper

2. Make sure that MySQL is correctly configured, and restart your DB server if necessary:
   ```
   mysql> SET storage_engine=INNODB;
   ```

3. Clone this repo and cd to the package root directory.

4. Set up your virtual environment:
   ```
   $ mkvirtualenv --distribute social_secretary
   $ workon social_secretary
   ```

6. Install the required Python dependencies:
   ```
   $ pip install -r requirements.txt
   ```

7. Make sure that your settings file is properly configured:

   In social_secretary/settings.py:
   ```python

   from social_secretary.secret_settings import *

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'social_secretary',
           'USER': 'social_secretary',
           'PASSWORD': secret_settings.DEFAULT_DATABASE_PASSWORD,
           'HOST': 'localhost',
       },
       'test': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'social_secretary_test',
           'USER': 'soical_secretary',
           'PASSWORD': secret_settings.TEST_DATABASE_PASSWORD,
           'HOST': 'localhost',
       }
   }
   ```

   Create a secret_settings file for your db passwords:
   ```
   $ vim social_secretary/secret_settings.py
   ```

   In social_secretary/secret_settings.py:

   ```python

   DEFAULT_DATABASE_PASSWORD = 'my_dev_db_password'
   TEST_DATABASE_PASSWORD = 'my_test_db_password'
   ```

8. Create your databases, users and passwords:
   ```
   mysql> CREATE DATABASE social_secretary;
   mysql> CREATE DATABASE social_secretary_test;
   mysql> GRANT ALL ON social_secretary.* TO 'social_secretary'@'localhost' IDENTIFIED BY 'my_dev_db_password';
   mysql> GRANT ALL ON social_secretary_test.* TO 'social_secretary'@'localhost' IDENTIFIED BY 'my_dev_db_password';

9. Run syncdb:
   ```
   $ ./manage.py syncdb
   ```

10. Run your migrations:
   ```
   $ ./manage.py migrate
   ```

11. Start your server:
    ```
    $ ./manage.py runserver

Testing
-------

Tests use the nose test runner. From the project root, simply run:
```
$ nosetests
```

