killall gunicorn
nohup gunicorn --workers=3 app:app --log-level debug &
sudo systemctl restart nginx 