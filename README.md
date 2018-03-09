# cuLearn Mark Fetcher


I wanted a quick way to check  all my marks for all my classes in one place so I wrote this Python script to easily/quickly do this!

It works by logging in your cuLearn account as normal, visiting the grades section for each class, takes all that info then displays all the marks you have for all your courses in one place.

I'm using the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) library to easily extract the data from the web page to store them into an array for easy viewing.  You can install it using:
```
pip install beautifulsoup4
```


----------


**Disclaimer**: It's not safe to have your password written in plain text saved on a file on your computer. Please use at your own risk. This script doesn't store or send any information anywhere.
