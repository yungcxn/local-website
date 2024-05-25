# local-website

website i deploy with flask+gunicorn+nginx locally to stream videos etc.

## Prereqs

1. Install the following packages with your pm:

- `flask`
- `gunicorn`
- `nginx`

2. Download python-dependencies via pip:

- `dotenv`
- `flask`

3. run `setup-keys.sh`

4. copy `etc-nginx-nginx.conf` to `etc/nginx/nginx.conf`
- You may need to change the location where static videos are served, mine is `/home/can/local-website/video`

5. run `start.sh` - also restarts.

## Usage

Place your videos in the `video` folder.

## Note

Content is german

