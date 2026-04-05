#!/bin/bash
# This script runs during Vercel's build phase for the Django backend.
# Vercel calls this via the "buildCommand" in vercel.json (or Project Settings).

echo "==> Installing dependencies"
pip install -r requirements.txt

echo "==> Collecting static files"
python manage.py collectstatic --noinput

echo "==> Running migrations"
python manage.py migrate --noinput

echo "==> Build complete"
