# Exoplanet-Seeker

This app collects a subset of the data available on NASA's Confirmed Exoplanet database table. Then it first presents that data to the user in a table format so that the user can see all of the data. When the user is ready, they simply click on the 'Go Graph the Data' link and are taken to a page where they can select different values to graph, and what format of graph they would like to use.

This app gives the user a way to interact with the data and see for themselves if they can gain any interesting insights. The various methods used by scientist to discover exoplanets are presented with links to Wikipedia, because those are some very long explanations that can't really be shortened. Additionally, a list of links is provided for the more exotic terms the user might see. Those links also go to Wikipedia.

The app starts working when the user clicks on the link to go to the Data page. The GET route for this page calls a function which makes an API request for a subset of the data from NASA. This response is then stored in a variable as a JSON object, and sent to the client-side to be displayed.

When the user clicks on the link to 'Go Graph the Data', they are presented a form where they can select the pieces of data to graph and compare, as well as a selection of graph formats. Each format has its own strengths and weaknesses. Some of the graphs we (non-scientist) might be expecting are not available. Once the user has made their selections and clicked the submit button, their selection goes to the server. The method for this is POST, as the user is setting the variable values which the app will use in the following steps.

First, when the POST request comes back, a function is called which takes the JSON object storing the data and converts it into a pandas dataframe. Next, the type of graph selected is set to a variable and passed through an if-elif-else chain to select the correct code-block for that graph type. That code block pulls the data from the dataframe, based on the selections the user made, shapes it a bit, and then calls the corresponding matplotlib graphing function located in another file, passing it the necessary arguements. Lastly, those functions take the inputs, generate the desired graph, convert it into a png file, then into 64 byte strings to be sent to the client-side. This does mean that when the graph is rendered on the client-side it is a fixed image.

## What it includes

* Jinja templates
* flask
* numpy
* pandas
* matplotlib

## Included routes

# index.py
|Method|Path|Purpose|
|----------|----------|---------------|
|GET|'/'| Home page|
|GET|'/data'| Displays NASA's data|
|GET|'/visual'| Shows form for selecting data|
|POST|'/visual'| Takes the user inputs, renders the desired graph|

## Directions

### 1. Clone the repository
...sh
git clone <repo link> <new name>
...

### 2. Install the necessary modules

...sh
pip install 
...

### 3. Customize the project

There isn't a whole lot of styling on this app, but make it look like your own

### 4. Delete the origin that points to the original repository

...sh
git remove -v
...
reveals the origin of the repository

...sh
git remote remove origin
...
will remove this origin, leaving you free to create your own

### 5. 

Go to Github and follow the instructions for creating a new repository

...sh 
git init
git add. 
git commit -m "Initial Commit"
git remote add origin <new_repository>
git push origin master
...
