Social Secretary
================
Social Secretary is a notification system that helps you manage your social network.

Users connect via Facebook and categorize / sort their friends. Social Secretary then sends the users reminders via email when they are starting to mis-manage their personal and business contacts (i.e. falling out of touch with a contact, forgetting to reply, etc).


Installation and Setup
----------------------

1. Install Python 2.x, MySQL 5.x, Python virtualenv and Python virtualenvwrapper

2. Make sure that MySQL is correctly configured, and restart your DB server if necessary:
   ```
   [client]
   default-character-set=utf8

   [mysql]
   auto-rehash
   default-character-set=utf8

   [mysqld]
   character-set-server = utf8
   collation-server = utf8_unicode_ci
   default-storage-engine = innodb
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

7. Make sure your social_secretary database exists, and that your settings file is properly configured:
   ```
   $ vim /settings.py
   $ vim /secret_settings.py
   ```

8. Run syncdb:
   ```
   $ ./manage.py syncdb
   ```

9. Run your migrations:
   ```
   $ ./manage.py migrate
   ```

10. Start your server:
    ```
    $ ./manage.py runserver

Testing
-------

Tests use the nose test runner. From the project root, simply run:
```
$ nosetests
```
