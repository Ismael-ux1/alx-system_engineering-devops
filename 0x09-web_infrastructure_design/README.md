Web infrastructure design
 ## Concepts

* DNS (Domain Name System):

    Definition: DNS is a system used to translate human-readable domain names (like www.example.com) into IP addresses (like 192.168.1.1) that computers use to identify each other on the network.
    Importance: DNS is crucial for web infrastructure because it enables users to access 

* Monitoring:

    Definition: Monitoring involves tracking the performance and health of your web infrastructure. It often includes monitoring server resources, website availability, and response times.
    Importance: Effective monitoring ensures that you can quickly identify and address issues, such as server overloads or downtime, to maintain a reliable web service.

* Web Server:

    Definition: A web server is software or hardware that stores and serves website content to users' web browsers upon request. Common web servers include Apache, Nginx, and Microsoft IIS.
    Importance: Web servers are at the core of any web infrastructure, as they handle client requests, process web applications, and serve web content like HTML, images, and videos.

* Network Basics:

    Definition: Network basics involve understanding fundamental networking concepts, including IP addressing, subnets, routing, and firewalls.
    Importance: A solid grasp of network basics is crucial for designing web infrastructures that are secure, efficient, and able to communicate with other components of the internet.


* Load Balancing:

    Definition: Load balancing is the practice of distributing incoming network traffic or application requests across multiple servers or resources. It ensures that no single server is overwhelmed with too much traffic.
    Importance: Load balancing improves the scalability, availability, and reliability of web applications by evenly distributing requests, preventing downtime, and optimizing resource usage.


* Servers:

    Definition: Servers are computer systems or software applications that provide services, data, or resources to other computers or clients over a network. Servers can include web servers, database servers, file servers, etc.
    Importance: Servers are the backbone of web infrastructures. They execute tasks, store data, and respond to requests from clients or users, making them central to any web-based service.

  

Tasks 📃

    Simple_web_stack (Task 0):
        Description: You'll create a basic web infrastructure hosted on one server accessible via www.foobar.com.
        Explanation: Start by considering a user who wants to access your website. Describe how the DNS (Domain Name System) resolves the domain name www.foobar.com to an IP address, how the request reaches the web server, and how the server responds to serve the website.

    Distributed_web_infrastructure (Task 1):
        Description: You'll design a more complex web infrastructure with three servers hosting the website www.foobar.com.
        Explanation: Describe how the distribution works, how load balancing might be involved, and how requests are handled across the three servers. Explain how DNS may be configured for redundancy.

    Scale up (Task 2):
        Description: This task involves further scaling up the infrastructure.
        Specifics: The details of this infrastructure design will depend on the specific requirements provided in the task. You might need to consider adding more servers, implementing load balancing, or enhancing other aspects of the infrastructure.
