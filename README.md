# Blog

A simple blog with Flask. 


## Deploy
### Deploy locally
#### Prerequisites

* Python 3

#### Steps

 - Install

    ```
    $ pip install -r requirements.txt
    ``` 

 - Run
 
    ```
    $ python app.py
    ```

  - Visit http://localhost:5000/ on your browser.


#### Tests

```
$ pytest
```


### Deploy with Docker

 - Build the container

    ```
    $ docker build -t blog-app:latest .
    ```

 - Run the container

    ```
    $ docker run -d -p 5000:5000 blog-app
    ```

  - Visit http://localhost:5000/ on your browser.

 - Stop the container
 
    ```
    $ docker container ls
    You should see your container id by running this command.

    $ docker container stop [container id]
    ```
    
    
### Use
#### Log in

Visit http://localhost:5000/login

 - password: secret