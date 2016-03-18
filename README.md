# Cisplatin

Cisplatin is my personal website, hosted on DigitalOcean. The site is live at http://cisplatin.xyz.

## Running Cisplatin

Cisplatin can be run locally on 127.0.0.1:8000 with the following commands:

```Bash
git clone https://www.github.com/Xenonstory/Cisplatin
cd Cisplatin && sudo -H pip install -r requirements.txt
python manage.py migrate && python manage.py runserver 8000
```

## To Do

- Make a cleaner favicon, add a robots.txt
- Add a nice 404 page
- Include sections for PGP key, work experience
- Add a notification for when the site is to be updated (and a script to update)
- An interactive homepage
