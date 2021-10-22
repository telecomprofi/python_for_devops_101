### Python scripting for DevOps 101 


### How to install python2 or python3 on RHEL 8
* [Link to the article](https://www.tecmint.com/install-python-in-rhel-8/#:%7E:text=Although%20Python%20is%20not%20installed,is%20used%20by%20system%20tools)
* TL:DR: 
```
#dnf install python3 
```
or 
```
dnf install python2
```
and then run ``` python3 ``` or ``` python2 ```
* What if there are applications/programs on your system that expect a python command to exist, what do you need to do? It is simple, you use alternatives --config python command to easily make /usr/bin/python point to the correct location of the Python version you want to be set as the default version.
```
# alternatives --set python /usr/bin/python3
```
OR
```
# alternatives --set python /usr/bin/python2
```
![image](https://user-images.githubusercontent.com/17558124/138422796-0a621f63-f8d7-4ed2-9a93-402c0c197e57.png)
____

## simple script to open file, write string, close file
* [Link to code](tba)
![image](https://user-images.githubusercontent.com/17558124/137160309-d3d85d15-e086-4cea-9780-6831c5d33987.png)


## simple scripts that use sys, os, os.path modules
*
*

## yaml creation script

*
*


## using jinja template to create ansible inventory from Terraform outputs

*
*


## script that checks public IP of EC2 instance and updates DNS A record through Godaddy API with newly assigned dynamic public IP
* [Link to code]( )
*


## Google python coding guidelines
* [Link to document]( tba )

### Exmample of Python 3.x use for running shell commands as opposed to 2.x subprocess.call() 
## [pyls3.py](https://github.com/telecomprofi/python_for_devops_101/blob/main/pyls3.py)  


### How to secure python development with bandit (Open-Source security scan tool)
* [Link to how to doc](https://soshace.com/how-to-secure-python-web-app-using-bandit/)
* TL:DR <tba>

### Best practices in Docker development with python
* [Link to the article](https://testdriven.io/blog/docker-best-practices/)
* TL:DR <tba>
