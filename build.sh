#!/bin/sh

# Exit on error
set -e

# Upgrade pip
python -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear