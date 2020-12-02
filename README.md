flask-application
-------

Basic flask application architecture with swagger and docker integrated.this application has two resource one is file uploader 
and second one is recommendation which is content based recommendation. 

Install
-------
## clone the repository
    git clone https://github.com/amoljagadambe/flask-application.git
    cd flask-application
    # checkout the correct version
    git tag  # shows the tagged versions
    git checkout latest-tag-found-above
    
Create a virtualenv in the flask-application directory and activate it::

    python -m venv venv
    venv\Scripts\activate.bat
    
Install Dependencies in Virtual Environment::

    pip install -r requirements.txt
    
 RUN
 ---
 
 On Local Virtual Environment::
    
    flask run
 
 On Docker::
    
    $ docker image build -t flask-app .
    
    $ docker run -p 3000:3000 -d --name flask-application flask-app

Save/Load the docker image(optional)
----
this below queries will save you the hassle of downloading the images from docker hub and increase the speed of
execution, but ***this is optional you dont need to do this***. 

    $ docker save flask-app > flask-app.tar
    
    $ docker load --input flask-app.tar

Open http://127.0.0.1:3000 in a browser. to access all the api over swagger just add /swagger-ui.html/ at the 
end of url.