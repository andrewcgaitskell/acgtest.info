uwsgi --socket 127.0.0.1:5000 --wsgi-file project1.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
