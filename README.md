# Automation Testing for containerized WordPress Store

The testing environment is constructed using Docker and is defined in a YAML configuration file that employs multiple Dockerfiles to build the necessary containers. This configuration includes components such as the Web Server (NGINX), the PHP environment with required extensions, an in-memory data structure store (Redis), a relational database (MySQL), the WordPress Store installation with all custom personalization, and PHPMyAdmin for database access.

![](https://i.imgur.com/roZ5wpz.png)

Automated tests are implemented using Selenium WebDriver, Python, Pytest and different other libraries (check `requirements.txt`) to ensure the verification and validation of a comprehensive test suite, examining user interactions with different pages and elements, including the login functionality, user account management, main page for products visualization, standalone product interactions, shopping cart behaviour, customer shipping and billing forms, and the checkout process.

## Prerequisites

* Install [OpenSSL](https://www.openssl.org/) on your system.
* Install [Docker](https://www.docker.com/) on your system.
* Install [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install) on your system (Windows).
* Install [Python](https://www.python.org/) on your system.

* Install the required Python packages by executing the following command

    ```bash
      pip install -r requirements.txt
    ```

* Update `hosts` file with the following line, replacing `<IPv4 Address>` with your actual IPv4 Address.

    ```txt
      <IPv4 Address> automation.wp-store.local
    ```

## Usage
      
* Get the Code:
    ```bash
    git clone https://github.com/alexandru-lazara/automation.wp-store.git
    ```
    ``` bash
    cd docker-wp-store
    ```

* Start Containerized WordPress Store:
    ```bash
    /bin/bash ./docker-start.sh
    ```
    
* Generate new set of SSL Certificates - already included in `docker-start.sh` Script:
     ```bash
     /bin/bash ./generate-ssl.sh
     ```
     
* Create MySQL-dump for backup and replace the current one:
     ```bash
     /bin/bash ./mysql-dump.sh
     ```
     
* Run Automated Tests using Pytest:
    ```bash
    pytest tests/
    ```

* To access the Store manually use:
  
    - PHPMyAdmin:
        - https: -
        - http: [http://localhost:8080/](http://localhost:8080/)

    - WordPress Store:
        - https: [https://automation.wp-store.local](https://automation.wp-store.local)
        - http: [http://automation.wp-store.local](http://automation.wp-store.local) - forwarded to https
    
    - WordPress Admin:
        - https: [https://automation.wp-store.local/wp-admin/](https://automation.wp-store.local/wp-admin/)
        - http: [http://automation.wp-store.local/wp-admin/](http://automation.wp-store.local/wp-admin/) - forwarded to https

    - After each Docker rebuild, when accessing the WordPress Store or WordPress Admin for the first time, you will encounter a `Your connection is not private` page. This is due to the use of self-signed SSL certificates. Simply go to `Advanced` and click on `Proceed to automation.wp-store.local (unsafe)`

    - Test Accounts:
        | Platform        | Username  | Password  | Email Address     | Role     |
        | --------------- | --------- | --------- | ----------------- | -------- |
        | PHPMyAdmin      | wordpress | wordpress | -                 | DB User  |
        | WordPress Store | user      | user      | user@example.com  | Customer |
        | Wordpress Admin | admin     | admin     | admin@example.com | Admin    |
