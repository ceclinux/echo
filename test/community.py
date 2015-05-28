import markdown
from flask import Blueprint, render_template, jsonify, Flask
app = Flask(__name__, template_folder='../app/template', static_folder='../app/static')
text = "fwefw \n sdfasfds \n >fwefwefw \n **fwef** \n##sdfasf\n===\n*sfa*\n -[test](http://www.qq.com)\n -![sdf](http://guo.lu/wp-content/themes/Diaspora/timthumb/timthumb.php?src=http://guo.lu/wp-content/uploads/2015/05/wallhaven-74740.jpg) "

@app.route('/')
def index():
    return render_template('index.html', body=markdown.markdown(text, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables']), email="src655@gmail.com", blogname="Test", introduction="分为范围服务范文芳分为范围服务范文芳分为范围服务范文芳分为范围服务范文芳分为范围服务范文芳")

if __name__ == '__main__':
    app.run(debug=True)

