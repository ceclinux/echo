# echo

An insanely simple blog framework powered by Flask.Still under development.

Use [Markdown](http://daringfireball.net/projects/markdown/) to write posts.

## How to install

1. Register a [heroku](http://www.heroku.com) account
2. Install [Heroku Toolbelt](https://toolbelt.heroku.com/windows) command tool
3. `heroku login`
4. git clone this repository, and cd to this directory.
5. `heroku create <appname>`,  type the appname you want
6. Add Postgres Database, type `heroku addons:add heroku-postgresql:dev`
7. `git push heroku master` to install Echo to Heroku
You will see `http://<appname>.herokuapp.com deployed to Heroku` displayed on your console.
8. `heroku run python manage.py deploy` to deploy the database
That's it! You can open browser and type http://<appname>.herokuapp.com to view your blog.

## How to use

The default blog

![](http://img.vim-cn.com/e3/f2257b3690424b659c12cecf7e9b920e4840e8.jpg)

Click login and register for this blog.**The blog can only be registered once.**After that, you can login as administrator to customize your blog and write blogs. Other users are treated as visitors.

After customization and writing posts

![](http://img.vim-cn.com/e5/c9b252f38d486930297afd2687d28f746342c8.jpg)

## License

MIT
