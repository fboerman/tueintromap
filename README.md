# TU/e Introduction map

This small web app serves as a handy reminder for new students during the introduction week of the TU/e. Its deployed at [https://www.introtue.nl/](https://www.introtue.nl/).  
It is generated from the locations and description in ```data.xlsx``` and the icons in the icons folder.

Private project, this is in no way officially endorsed.

## Deployement
To generate the site grab two google maps API keys, one for deployement and one for localhost. Create a ```secrets.py``` and define the keys as ```API_KEY_prod=``` and ```API_KEY_local=```. Then create a folder named ```public``` and run the ```generate.py``` script, after installing dependencies from ```requirements.txt```.  Copy the icons folder and stylesheet ```style.css``` into the public folder and host the folder with a standard webserver setup.
