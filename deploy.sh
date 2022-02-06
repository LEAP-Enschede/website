#!/bin/sh

export PATH=$PATH:/opt/cpanel/ea-nodejs10/bin/
export PATH=$PATH:/usr/bin/

cd /home/leaproundnetensc/apps/website

echo "Checking current version"

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "@{u}")

if [ "$LOCAL" != "$REMOTE" ]; then
  echo "Starting update"
  git pull
  npm install
  pip3 install -r ./requirements.txt
  npm run build
  python3 ./manage.py migrate
  python3 ./manage.py collectstatic
  echo "Finished update"
else
  echo "Already up-to-date"
fi