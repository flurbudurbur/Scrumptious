# Scrumptious

## Tailwind installation
1. Packages needed for TailwindCSS to work.
```python
python -m pip install django-tailwind django-tailwind[reload] pillow
```

3. Initialize TailwindCSS.

> This will ask you to name a directory. Just leave it default (press enter).
```python
python manage.py tailwind init
```

3. Install TailwindCSS.
```python
python manage.py tailwind install
```

## CMD to start TailwindCSS (for development)
> You will need to execute this every time you start up your IDE!
```python
python manage.py tailwind start
```
