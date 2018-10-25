Moon Planner Backend
--------------------

Few words about the project.

### Requirements

Here is the list of thing that you need to run our backend:
- Python 3.6,
- Python 3.6-dev,
- Virtualenv.

### Installing

Let's start! At first, please clone this repository:

```bash
$ git clone git@github.com:WDKWWAD/moon-planner-backend.git
$ cd cd moon-planner-backend/
```

After that you will be able to create a virtual environment which may
be helpful to manage your dependencies locally. To do so, please run
commands below to create and then activate your virtual environment:

```bash
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
```

Now you can install all dependencies for this project:

```bash
(venv) $ pip install -r requirements.txt
```

Remember about setting up `$PYTHOPATH` variable!

```bash
$ export PYTHONPATH=`pwd`
```

Now our backend is ready to be used, so let's try to run it!

```bash
(venv) $ python3.6 mission_planner/app.py
```

And that's all! Everything should be fine and Swagger for our 
REST API should be available on: `http://localhost:5000/api`.
