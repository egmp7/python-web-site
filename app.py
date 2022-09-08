""" #   Steps
# Install flask
# Run server command:
#       flask --app app run
#       flask --app app --debug run
#  """

""" SET UP """
from flask import Flask, render_template
app = Flask(__name__)
""" ------ """
# #################
# Teaching purpuses

data = [{'tittle': 'Mario','age':'13'},
        {'tittle': 'Dennise','age':'23'}]

@app.route('/')
def hello():
    return 'Hello World!'

# Add argument
@app.route('/<blog_id>')
def blogId(blog_id):
    return 'Blog # ' + str(blog_id)

###################

# TEMPLATES
@app.route('/home')
def blog():
    return render_template(
        'helloWorld.html',
        author='Erick',
        test=False,
        data=data,)

@app.errorhandler(404)
def page_not_found (e):
    return render_template('404.html'), 404

""" Run """
if __name__ =='__main__':
    app.run()(debug=True)
""" ---- """