# Flask API

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # authentication logic
        if username and password is valid:
            return redirect(url_for('expert_services_to_change_business'))
        else:
            return "Unable to login"
    else:
        return render_template('login.html')

@app.route('/expert_services_to_change_business', methods = ["GET", "POST"])
def expert_services_to_change_business():
    if request.method == "POST":
        if request.form["action"] == "Configure":
            return redirect(url_for('configure_jira_software'))
    else:
        return render_template('expert_services_to_change_business.html')

@app.route('/configure_jira_software', methods = ["GET", "POST"])
def configure_jira_software():
    if request.method == "POST":
        if request.form["action"] == "Reset":
            return redirect(url_for('configure_jira_software'))
        elif request.form["action"] == "Save":
            username = request.form['username']
            password = request.form['password']
            url = request.form['url']
            repository_name = request.form['repository_name']
            # Validate Jira Software credentials
            if authentication_success(username, password, url, repository_name):
                return redirect(url_for('list_title_username_url_action'))
            else:
                return "Unable to configure Jira Software"
    else:
        return render_template('configure_jira_software.html')

@app.route('/list_title_username_url_action', methods = ["GET", "POST"])
def list_title_username_url_action():
    if request.method == "POST":
        if request.form["action"] == "Edit":
            # Edit logic here
            return redirect(url_for('list_title_username_url_action'))
        elif request.form["action"] == "Delete":
            # Delete logic here
            return redirect(url_for('list_title_username_url_action'))
        elif request.form["action"] == "Show Entries":
            # Show logic here
            return redirect(url_for('list_title_username_url_action'))
        elif request.form["action"] == "Add More":
            return redirect(url_for('add_more_jira_software'))
    else:
        # List logic here
        return render_template('list_title_username_url_action.html')

@app.route('/add_more_jira_software', methods = ["GET", "POST"])
def add_more_jira_software():
    if request.method == "POST":
        if request.form["action"] == "Reset":
            return redirect(url_for('add_more_jira_software'))
        elif request.form["action"] == "Save":
            username = request.form['username']
            password = request.form['password']
            url = request.form['url']
            repository_name = request.form['repository_name']
            # Validate Jira Software credentials
            if authentication_success(username, password, url, repository_name):
                return redirect(url_for('list_title_username_url_action'))
            else:
                return "Unable to configure Jira Software"
    else:
        return render_template('add_more_jira_software.html')