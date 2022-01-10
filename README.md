# get_Favicon
Retrieve favicon.ico hash for later usage


### Description

A small python script to retrieve the website's favicon.ico. This is usually helpful when enumerating similar web applications.

### Small Requirement
You'd probably need to install "mmh3"

`# pip3 install mmh3`

# Usage

`$ python3 get_favicon.py "https://www.target.com/favicon.ico"`

![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/sasukeourad/get_Favicon/main/Pictures/get_favicon.png)

<br> 

The retrieved hash can then be used to scan for similar web applications or products. For example: Shodan can be used to lookup similar web applications. This is nice in case you're looking for a certain behaviour that propagate through all of them. Check stackoverflow as an example below:

![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/sasukeourad/get_Favicon/main/Pictures/shodan_scan.png)





  #### DISCLAIMER!
   Use for good
   
   ^_^
