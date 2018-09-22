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

<<<<<<< HEAD

@app.route('/')
def home_page():
    '''
        App for hompage
    '''
    session['user_count'] = functions.get_user_count()
    try:
        if session['username']:
            return render_template('video.html', username=session['username'])
        return render_template('video.html')
    except (KeyError, ValueError):
        return render_template('video.html')


@app.route('/profile/')
@login_required
def profile():
    '''
        App for user profile can only be accessed only after successful login
    '''
    if request.method == 'GET':
        notes = functions.get_data_using_user_id(session['id'])
        tags = []
        if functions.get_number_of_tags(session['id']) == 0:
            ls = ["Electricista", "Cerrajería", "Remodelado", "Limpieza"]
            for i in ls:
                tag = i
                functions.add_tag(tag,session['id'])
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
        return render_template(
            'profile.html',
            username=session['username'],
            notes=notes,
            tags=tags
        )


@app.route('/login/', methods=('GET', 'POST'))
def login():
    '''
        App for creating Login page
    '''
    global cant
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = functions.generate_password_hash(request.form['password'])
        user_id = functions.check_user_exists(username, password)
        if functions.get_number_of_notes(user_id) is not None:
            cant = int(functions.get_number_of_notes(user_id))+1
        if user_id:
            session['username'] = username
            session['id'] = user_id
            functions.store_last_login(session['id'])
            return redirect('/profile/')
        else:
            flash('Username/Password Incorrect!')
    return render_template('login.html', form=form)


@app.route('/signup/', methods=('GET', 'POST'))
def signup():
    '''
        App for registering new user
    '''
    form = SignUpForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = functions.generate_password_hash(request.form['password'])
        email = request.form['email']
        name = request.form['name']
        lastname = request.form['lastname']
        number = request.form['number']
        adress = request.form['adress']
        city = request.form['city'] 
        neighborhood = request.form['neighborhood']
        check = functions.check_username(username)
        if check:
            flash('Username already taken!')
        else:
            print(name)
            print(lastname)
            print(number)
            functions.signup_user(username, password, email, name, lastname, number, adress, city, neighborhood)
            session['username'] = username
            user_id = functions.check_user_exists(username, password)
            session['id'] = user_id
            return redirect('/profile/')
    return render_template('signup.html', form=form)


@app.route("/logout/")
def logout():
    '''
        App for logging out user
    '''
    session['username'] = None
    session['id'] = None
    return login()


@app.route("/adycentes", methods=['POST'])
@login_required
def adyacentes():
    req_data=request.get_json()
    origenLat=req_data['origen']['latitud']
    origenLon=req_data['origen']['longitud']
    destinoLat=req_data['destino']['latitud']
    destinoLon=req_data['destino']['longitud']
    radioSalida=req_data['radioSalida']
    radioLlegada=req_data['radioLlegada']


@app.route("/notes/<id>/")
@login_required
def view_note(id):
    '''
        App for viewing a specific note
    '''
    notes = functions.get_data_using_id(id)
    tags = functions.get_tag_using_note_id(id)
    tag_name = functions.get_tagname_using_tag_id(tags[0])
    return render_template('view_note.html', notes=notes, tags=tags, tag_name=tag_name, username=session['username'])


=======
>>>>>>> f38e8a0f87d2dc2bf4d275152e847e647beab263
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
