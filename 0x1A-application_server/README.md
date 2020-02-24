# 0x1A. Application server

## Description
What you should learn from this project:

---

### [0. Set up development with Python](./README.md)
* Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.


### [1. Set up production with Gunicorn](./2-app_server-nginx_config)
* Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.


### [2. Serve a page with Nginx](./3-app_server-nginx_config)
* Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/


### [3. Add a route with query parameters](./4-app_server-nginx_config)
* Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below.


### [4. Let's do this for your API](./5-app_server-nginx_config)
* Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.


### [5. Serve your AirBnB clone](./gunicorn.service)
* Let’s serve what you built for AirBnB clone - Web dynamic on web-01.


### [6. Deploy it!](./4-reload_gunicorn_no_downtime)
* Once you’ve got your application server configured, you want to set it up to run by default when Linux is booted. This way when your server inevitably requires downtime (you have to shut it down or restart it for one reason or another), your Gunicorn process(es) will start up as part of the system initialization process, freeing you from having to manually restart them. For this we will use systemd. You can read more about systemd in the documentation posted at the top of this project but to put it succinctly, it is a system initialization daemon for the Linux OS (amongst other things). For this task you will write a systemd script which will start your application server for you. As mentioned in the video at the top of the project, you do not need to create a Unix socket to bind the process to.


### [7. No service interruption](./4-reload_gunicorn_no_downtime)
* One of the most important metrics for any Internet-based business is its uptime. It is the percentage of the time over a given period that the service/product is accessible to customers. Let’s pick the example of Amazon.com, for every minute of downtime (which is the opposite of uptime), it costs the company $2M. Yet, application servers often need to restart to update with the new version of the code or new configuration, when doing this operation, an application server cannot serve traffic, which meant downtime.

To avoid this; application servers are designed with a master/workers infrastructure. The master is in charge of:

Receiving requests
Managing workers (starting, stopping)
Distributing requests to workers
Workers are the actual ones processing the query by generation dynamic content by processing the application code.

To update an application without downtime, the master will proceed with a progressive rollout of the update. It will gracefully shut down some workers ( meaning that it will tell workers to finish processing the request they are working on, but will not send them new requests, once the worker is done, it’s will be shutdown) and start new ones with the new application code or configuration, then move on to the other old workers until it has renewed the whole pool.

Write a simple Bash script to reload Gunicorn in a graceful way.


---

## Author
* **Brent Muha** - [bmuha1](https://github.com/bmuha1)