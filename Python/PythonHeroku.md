# Python Heroku #

## Resources ##

- [Getting Started With Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)
- [Django and Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

## Heroku First Run Fun ##

**NOTE** - Check out the Homebrew page if this isn't working, may need to take care of some Path settings

These steps will install the Heroku CLI, clone the getting started repo, create a dyno instance, and open it

- `brew install heroku/brew/heroku`
- `heroku login`
- `git clone https://github.com/heroku/python-getting-started.git`
- `cd python-getting-started`
- `heroku create`
- `git push heroku main`
- `heroku ps:scale web=1`
- `heroku open`

View the logs
- `heroku logs --tail`

See the Scale of your app scale down to zero then back up to 1
- `heroku ps`
- `heroku ps:scale web=0`
- `heroku ps:scale web=1`

Change something then push a new version
- Modify `requirements.txt`
- Modify `\hello\views.py`
- `git add .`
- `git commit -m "teapot"`
- `git push heroku main`
- `heroku open`

Set and get environmental configs
- `heroku config:set TIMES=2`
- `heroku config`
- From python
  - `times = int(os.environ.get('TIMES',3))`

Working with Postgres DBs, verify the db addon, check teh config and info
- `heroku addons`
- `heroku config`
- `heroku pg`

Visit the DB
- <appname>/db
- e.g. 'https://strong-duck-4049.herokuapp.com/db'
- the error is expected