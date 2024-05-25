# Function to check if a service is running
pgrep nginx > /dev/null && echo "nginx is running" || echo "nginx is not running"
pgrep -f gunicorn > /dev/null && echo "gunicorn is running" || echo "gunicorn is not running"