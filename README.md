# <p align="center">The Crab Tax</p>

<p align="center"> <img src="https://i.imgur.com/TaFdvZ7.png"/> </p>

The Crab Tax is a data tracking webapp which tracks the amount of gold being removed from the Old School Runescape economy via the new Grand Exchange Tax.

Built with Python using the Flask web framework.

## How it works

Data is pulled from the wiki pages below, then formatted and passed to the HTML templates via Flask.

> https://oldschool.runescape.wiki/w/Module:GEVolumes/data
> 
> https://oldschool.runescape.wiki/w/Module:GEPrices/data


## Usage

The code in this github repo can be used by runing __main__.py and then going to 127.0.0.1:5000
If you plan to deploy this code however, you will not want to run the application in this way.

My recomendation is to use <a href="https://help.pythonanywhere.com/pages/Flask/">PythonAnywhere</a>
