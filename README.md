npm install -D tailwindcss# Scrumptious

## Tailwind installation
1. Ensure that you have node.js and/or npm is installed.


2. Packages needed for the project to work:
```python
python -m pip install django-tailwind django-tailwind[reload] pillow django[argon2]
```

3. Initialize TailwindCSS.

```python
python manage.py tailwind init
```

> This will ask you to name a directory. Just leave it default (press enter).\
> You will receive the follwoing Error Message: \
CommandError: Error: "C:\Users\{User}\PycharmProjects\Scrumptious\scrumptious\theme" directory already exists\
> You can ignore that message and continue on to the next step.


4. Install TailwindCSS.
```python
python manage.py tailwind install
```

## CMD to start TailwindCSS (for development)
> You will need to execute this every time you start up your IDE!
```python
python manage.py tailwind start
```
