<!-- Web app logo -->
<p align="center">
	<img src="https://github.com/FahimSifnatul/world_universities/blob/master/static/images/logo.png" width="300" height="300">
</p>



<!-- Short description about World Universities -->
<h1>World Universities</h1>
<p align="justify">
	A simple, elegent and powerful web app to display different university related data. Besides, it includes a bunch of useful REST APIs to retrieve university data. Token based APIs are included.<a href="https://world-universities.herokuapp.com"><img src="https://github.com/FahimSifnatul/world_universities/blob/master/static/images/logo.png" width="12" height="12">Live Demo</a>
</p>	



<!-- Prerequisites -->
<h2>Prerequisites</h2>
<ul>
	<li>python >= 3.8</li>
</ul>



<!-- Install -->
<h2>Install</h2>
<p align="justify">
	To run this web app on local machine, the python packages need to be installed are -
</p>
<ul>
	<li><a href="https://pypi.org/project/Django/">Django >= 3.2.4</a></li>
	<li><a href="https://pypi.org/project/djangorestframework/">djangorestframework</a></li>
	<li><a href="https://pypi.org/project/requests/">requests</a></li>
	<li><a href="https://pypi.org/project/whitenoise/">whitenoise</a></li>
	<li><a href="https://pypi.org/project/virtualenv/">virtualenv</a> (optional)</li>
</ul>
<p align="justify">
	Or packages can be install with single command as below - 
</p>

```bash
pip install Django==3.2.4 djangorestframework requests whitenoise virtualenv
```

<p align="justify">
	Also needs to install <code>git</code> to setup 'Countries!!!' web app easily. To install <code>git</code> on linux (tested on <a href="https://ubuntu.com/download/desktop">ubuntu 20.04 LTS</a>), please run this command - 
</p>

```bash
sudo apt-get install -y git
```

<p align="justify">
	To install on macOS, windows and other distros of linux, please visit the <a href="https://git-scm.com/downloads">official page</a>.
</p>
<p align="justify">
	For step by step setup procedure, please see the <strong>User Guide</strong> section below.
</p>



<!-- User guide -->
<h2>User Guide</h2>
<p align="justify">
	Here is the user guideline to setup 'Countries!!!' web app on local machine (Linux - tested on <a href="https://ubuntu.com/download/desktop">ubuntu 20.04 LTS</a>). 
</p>

<h3>Setup Virtual Environment (optional)</h3>
<p align="justify">
	At first install virtualenv python package via pip -
</p>

```bash
pip install virtualenv	
```

<p align="justify">
	Create a virtual environment - 
</p>

```bash
virtualenv vCountries
```

<p align="justify">
	Here vCountries can be any name. Activate virtual environment -
</p>

```bash
source vCountries/bin/activate
```

<h3>Setup Countries!!!</h3>
<p align="justify">
	At first install <code>git</code> via <code>bash</code> command on terminal -
</p>

```bash
sudo apt-get install -y git
```

<p align="justify">
	Create an empty directory. Let's in our case it is django. Change directory to django - 
</p>

```bash
mkdir django
cd django
```

<p align="justify">
	Now clone this repository via <code>git clone</code> command on terminal -
</p>

```bash
git clone https://github.com/FahimSifnatul/strativ.git
```

<p align="justify">
	Run below <code>python</code> commands on terminal to setup NoSQL database SQLite3 -
</p>

```bash
python manage.py makemigrations
python manage.py migrate
```

<p align="justify">
	We are just one step away from successful 'World Universities' web app setup. Run below <code>python</code> command on terminal to play with the web app -
</p>

```bash
python manage.py runserver 127.0.0.1:8000
```	

<p align="justify">
	Done. Simple, isn't it? Enjoy rich data about universities of the world.
</p>



<h2>Token based RESTful APIs</h2>
<ol>
	<li><code>/<<span>api_token</span>>/collect</code> - To collect details data from <a href="http://universities.hipolabs.com/search">REST universities API</a></li>
  <li><code>/<<span>api_token</span>>/list</code> - Returns details info about all universities in JSON format</li>
  <li><code>/<<span>api_token</span>>/search/<<span>university</span>></code> - Return details info about specific university in JSON format</li>
  <li><code>/<<span>api_token</span>>/search-by-country/<<span>country</span>></code> - Return details info about universities under specific country in JSON format</li>
</ol>
<p align="justify">
	[N.B.: replace <<span>api_toke</span>> with a valid user authenticated API token, <<span>university</span>> with a valid university name and <<span>country</span>> with an existing country name]
</p>



<h2>Contributors</h2>
<p align="justify">
	It's an open source project. Everybody is welcomed to contribute.
</p>



<h2>License</h2>
<p align="justify">
	Countries!!! web app can be copied, modified, distributed for both personal and commercial purposes under <a href="https://opensource.org/licenses/MIT">MIT License</a>
</p>