# Football Review Application
<h1>Efekan Calim</h1>


<h2>Contents</h2>
<h3>Brief</h3>
<br>
The objective of this project is to create a fully CRUD operational application that allows a user to select and review a chosen Premier League footballer. The user should also be able to update and delete their reviews. <br>
<br> 
<h3>Requirements</h3>
1. A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project. <br>
2. A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship. <br>
3. Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment. <br>
4. A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board <br>
5. Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach. <br>
6. A functioning front-end website and integrated API's, using Flask. <br>
7. Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

<h2>Structure and Planning</h2>
<br>
<h3>Entity relationship diagrams</h3>
<br>
The diagrams below describe the entity relationships for my MySQL database tables. The relationship between Players and Reviews is one to many as one footballer may have many reviews associated to them; however one review will not have many footballers associated to it.
<br>
<a href="https://imgur.com/lJAAxbR"><img src="https://i.imgur.com/lJAAxbR.png" title="source: imgur.com" /></a>
<br><br>
<h3>CI Pipeline</h3>
The continuous integration pipeline was used for the deployment of the application
<br>
<a href="https://imgur.com/SY3SiOY"><img src="https://i.imgur.com/SY3SiOY.jpg" title="source: imgur.com" /></a>
<br><br>
<h3>User Stories and Project Board</h3>
<br>
For this project, I used a Jira project board. This included a product backlog and user stories. 
<a href="https://imgur.com/shcI0jm"><img src="https://i.imgur.com/shcI0jm.png" title="source: imgur.com" /></a>
<br><br>
<h3>Testing</h3>
Testing was performed with the pytest package and returned a test coverage of 84%
<br>
<a href="https://imgur.com/7m8s4Is"><img src="https://i.imgur.com/7m8s4Is.png" title="source: imgur.com" /></a>
<br><br>
<h3>Risk Assessment</h3>
Below is a screenshot of part of my risk assessment. Risks were followed up after the MVP was developed and an analysis was performed. The full risk assessment can be found here: https://1drv.ms/x/s!AoYdmsJr6KE6k20mpK-UJWm1uHl8?e=HIF5GE
<br>
<a href="https://imgur.com/g9bk9Lq"><img src="https://i.imgur.com/g9bk9Lq.png" title="source: imgur.com" /></a>
<br><br>
<h3>Jenkins</h3>
Jenkins was the program used to build and deploy the application. This was done by adding port 8080 to the GCP instance and running the Jenkins install script. Jenkins was given full sudo admissions in order to run the script.
<br>
<a href="https://imgur.com/pL87fYM"><img src="https://i.imgur.com/pL87fYM.png" title="source: imgur.com" /></a>
<br>
<a href="https://imgur.com/p1BIJbr"><img src="https://i.imgur.com/p1BIJbr.png" title="source: imgur.com" /></a>
<br><br>
<h3>Front End and CRUD Functionality</h3>
The application has full CRUD functionality and some screenshots of the front end can be found below.
<br>
<a href="https://imgur.com/HX9fS26"><img src="https://i.imgur.com/HX9fS26.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/4mFnf5A"><img src="https://i.imgur.com/4mFnf5A.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/JgssV3X"><img src="https://i.imgur.com/JgssV3X.png" title="source: imgur.com" /></a>
<br><br>
<h3>Tools</h3>
Framework: FLask
<br>
Database: MySQL
<br>
Languages: Python, HTML, SQL
<br>
CI Server: Jenkins
<br>
Version Control: Git
<br>
Project Tracking: Jira 
<br>
Virtual Environment: Google Cloud Platform
<br>
Testing: Pytest
<br>
ERD Diagrams: Draw.io
<br>
Risk Assessment: MS Excel
<br><br>
<h3>Future Improvements</h3>
<br>
In my next project I will aim to gain a better understanding of how testing is implemented. I used most of my time building CRUD functionality and did not leave enough time for testing code. 



