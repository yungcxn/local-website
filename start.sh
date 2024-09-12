# change cwd here
cwd=$(pwd)
cd ~/local-website
rm -rf ./nohup.out
sudo systemctl restart nginx

if pgrep -x "gunicorn" > /dev/null
then 
  killall gunicorn
fi

nohup gunicorn --workers=3 app:app --log-level debug & >/dev/null 2>&1

cd $cwd
