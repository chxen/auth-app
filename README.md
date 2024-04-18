How to start this application 
--------------------------------------------------------------

- Install it::
	git clone 
    config.py.txt -> config.py
    add secrets (SECRET_KEY,
                GOOGLE_CLIENT_ID,
                GOOGLE_CLIENT_SECRET,
                GITHUB_CLIENT_ID,
                GITHUB_CLIENT_SECRET)

- Run it::

    # Create an admin user
    $ flask fab create-admin
     
    # Docker build and run
    $ docker build -t auth-app .
    $ docker run -d -p 8080:5000 auth-app 
