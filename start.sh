# change cwd here
cwd=$(pwd)
cd ~/local-website
rm -rf ./combined.log
sudo systemctl restart nginx

if pgrep -x "gunicorn" > /dev/null
then 
  killall gunicorn
fi

env PYTHONUNBUFFERED=1

gunicorn --bind="0.0.0.0:8000" -k eventlet app:app --log-level debug --capture-output --enable-stdio-inheritance

# >/dev/null 2>&1 &

cd $cwd
