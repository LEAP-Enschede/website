#!/bin/sh

export PATH=$PATH:/opt/cpanel/ea-nodejs10/bin/
export PATH=$PATH:/usr/bin/

cd website

LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "@{u}")

if [ "$LOCAL" != "$REMOTE" ]; then
  git pull
  npm install
  pip3 install -r ./requirements.txt
  npm run build
  python3 ./manage.py migrate
  python3 ./manage.py collectstatic
fi