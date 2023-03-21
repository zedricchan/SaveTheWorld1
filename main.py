from flask import Flask, render_template, request

main = Flask(__name__)

grocery_list = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        if item:
          if item=='soap':
            grocery_list.append('hahahahha no.')
          else:
            grocery_list.append(item)
    return render_template('index.html', grocery_list=grocery_list)

if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8080)
