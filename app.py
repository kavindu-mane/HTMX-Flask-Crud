from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# task array : created with chatGPT
tasks = [
    {
        'id': 1,
        'title': 'Complete Project Proposal',
        'description': 'Write and submit the project proposal by the end of the week.',
        'due_date': '2024-02-10',
        'completed': False
    },
    {
        'id': 2,
        'title': 'Prepare Presentation Slides',
        'description': 'Create slides for the project presentation next Monday.',
        'due_date': '2024-02-17',
        'completed': True
    },
    {
        'id': 3,
        'title': 'Review Code Changes',
        'description': 'Review and provide feedback on the latest code changes.',
        'due_date': '2024-02-15',
        'completed': False
    },
    {
        'id': 4,
        'title': 'Attend Team Meeting',
        'description': 'Participate in the weekly team meeting to discuss project updates.',
        'due_date': '2024-02-12',
        'completed': False
    },
    {
        'id': 5,
        'title': 'Bug Fixing Session',
        'description': 'Dedicate time to fix reported bugs and issues in the codebase.',
        'due_date': '2024-02-18',
        'completed': False
    },
    {
        'id': 6,
        'title': 'Client Demo',
        'description': 'Prepare and conduct a demo for the client showcasing the latest features.',
        'due_date': '2024-02-20',
        'completed': False
    },
    {
        'id': 7,
        'title': 'Update Documentation',
        'description': 'Review and update project documentation for new changes and features.',
        'due_date': '2024-02-14',
        'completed': False
    },
    {
        'id': 8,
        'title': 'Research New Technologies',
        'description': 'Explore and research new technologies that could benefit the project.',
        'due_date': '2024-02-22',
        'completed': False
    },
    {
        'id': 9,
        'title': 'Code Refactoring',
        'description': 'Spend time refactoring code to improve readability and maintainability.',
        'due_date': '2024-02-16',
        'completed': False
    },
    {
        'id': 10,
        'title': 'Team Building Activity',
        'description': 'Participate in a team-building activity organized by the company.',
        'due_date': '2024-02-25',
        'completed': False
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def read():
    return render_template('read.html', tasks = tasks)

@app.route('/create' , methods=['POST' , 'GET'])
def create():
    if request.method== "GET":
      return render_template('create.html')
    tasks.append({
        'id': len(tasks) + 1,
        'title': request.form['title'],
        'description': request.form['description'],
        'due_date': request.form['due_date'],
        'completed': False
    
    })
    return redirect('/read')

@app.route('/update/<int:id>' , methods=['POST' , 'GET'])
def update(id):
    task = next((b for b in tasks if b['id'] == id), None)
    if request.method== "POST":
      task['title'] = request.form['title']
      task['description'] = request.form['description']
      task['due_date'] = request.form['due_date']
      task['completed'] = request.form['completed'] == 'on' if True else False
      return render_template('read.html', tasks = tasks)
    return render_template('update.html', task = task)

@app.route('/delete/<int:id>' , methods=['DELETE'])
def delete(id):
    global tasks
    tasks = [b for b in tasks if b['id'] != id]
    return render_template('read.html', tasks = tasks)

if __name__ == '__main__':
    app.run(debug=True)