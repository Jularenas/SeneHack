from flask import (
    Flask, render_template,
    redirect, request,
    flash, session,
    jsonify
)

from utils.forms import (
    LoginForm, SignUpForm,
    AddNoteForm, AddTagForm,
    ChangeEmailForm, ChangePasswordForm
)

from flask_restful import Resource, Api, reqparse
from utils.decorators import login_required
from flask_pagedown import PageDown
from flask import Markup
import utils.functions as functions
import datetime
import markdown
import random
#import utils.seleniumTest 

app = Flask(__name__)
api = Api(app)
pagedown = PageDown(app)
parser = reqparse.RequestParser()
app.secret_key = str(random.randint(1, 20))
cant = 0

@app.route("/notes/edit/<note_id>/", methods=['GET', 'POST'])
def edit_note(note_id):
    '''
        App for editing a particular note
    '''
    form = AddNoteForm()
    form.tags.choices = functions.get_all_tags(session['id'])
    form.tags.default = functions.get_tag_using_note_id(note_id)
    form.tags.process(request.form)

    if form.tags.choices is None:
        form.tags = None

    if request.method == 'GET':
        data = functions.get_data_using_id(note_id)
        form.note_id.data = note_id
        form.note_title.data = data[0][3]
        form.note.data = data[0][5]
        return render_template('edit_note.html', form=form, username=session['username'], id=note_id)
    elif form.validate_on_submit():
        note_id = form.note_id.data
        note_title = request.form['note_title']
        note_markdown = form.note.data

        try:
            tags = form.tags.data
            tags = ','.join(tags)
        except:
            tags = None

        note = Markup(markdown.markdown(note_markdown))
        functions.edit_note(note_title, note, note_markdown, tags, note_id=note_id)
        return redirect('/profile/')


@app.route("/notes/delete/<id>/", methods=['GET', 'POST'])
def delete_note(id):
    '''
        App for viewing a specific note
    '''
    global cant
    cant -= 1
    functions.delete_note_using_id(id)
    notes = functions.get_data_using_user_id(session['id'])
    tags = []
    if notes:
        for note in notes:
            tags_list = functions.get_tag_using_note_id(note[0])
            temp_list = []
            if tags_list:
                for tag in tags_list:
                    temp = functions.get_data_using_tag_id(tag)
                    if temp is not None:
                        temp_list.append(temp[0])
            tags.append(', '.join(temp_list))
    return render_template('profile.html', delete=True, tags=tags, username=session['username'], notes=notes)


@app.route("/tags/add/", methods=['GET', 'POST'])
def add_tag():
    '''
        App for adding a tag
    '''
    form = AddTagForm()
    if form.validate_on_submit():
        tag = request.form['tag']
        functions.add_tag(tag, session['id'])
        return redirect('/profile/')
    return render_template('add_tag.html', form=form, username=session['username'])


@app.route("/tags/")
def view_tag():
    '''
        App for viewing all available tags
    '''
    tags = functions.get_all_tags(session['id'])
    return render_template('edit_tag.html', tags=tags, username=session['username'])

		
@app.route('/<user_id>/<page_id>/info',methods=['POST'])
def post_info_page(user_id,page_id):
	functions.post_page_requiem(user_id,page_id,request.form['desc']) 

class GetDataUsingUserID(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            username = args['username']
            password = functions.generate_password_hash(args['password'])
            user_id = functions.check_user_exists(username, password)
            if user_id:
                functions.store_last_login(user_id)
                return functions.get_rest_data_using_user_id(user_id)
            else:
                return {'error': 'You cannot access this page, please check username and password'}
        except AttributeError:
            return {'error': 'Please specify username and password'}

api.add_resource(GetDataUsingUserID, '/api/')
parser.add_argument('username')
parser.add_argument('password')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
