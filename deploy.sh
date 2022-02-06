export STORAGEPATH=/home/roundnetensc/apps/website_storage
alias npm=/opt/cpanel/ea-nodejs10/bin/npm
alias node=/opt/cpanel/ea-nodejs10/bin/node
alias pip=/usr/bin/pip3
alias python=/usr/bin/python
npm install
npm run dev
pip install -r ./requirements.txt
python ./manage.py migrate
python ./manage.py collectstatic
ln -s $STORAGEPATH/media media