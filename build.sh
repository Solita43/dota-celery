#!/bin/bash

set -o errexit  # exit on error

# Navigate to the client directory and run npm commands
echo "Installing client dependencies and building the client..."
cd client
npm install
npm run build

cd ..

# Navigate to the server directory and run pip commands
echo "Installing server dependencies and setting up the database..."
cd server
pip install -r requirements.txt
echo 'Completed package installation from requirements.txt'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
echo 'Collecting static files...'
python manage.py collectstatic --no-input
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo 'THESE ARE THE STATIC FILES'
# ls -l /opt/render/project/src/staticfiles/
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
# echo '🥱😣😴🥱😌😥🤔🤩🤗🙂😶😶😏😏🤗😎😋😶😑'
echo 'Migrating...'
python manage.py migrate

cd ..

echo "Build and setup completed successfully!"
