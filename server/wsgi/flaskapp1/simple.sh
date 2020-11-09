uwsgi --socket 0.0.0.0:5000 --wsgi-file project1.py --callable app --processes 4 --threads 2 --buffer_size 65535
