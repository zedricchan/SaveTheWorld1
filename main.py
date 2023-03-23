from flask import Flask, render_template, request

app = Flask(__name__)


grocery_list = []
grocery_num = []

@app.route('/')
def index():
    return render_template('index.html', grocery_list=grocery_list)
  

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    if item.lower() not in grocery_list and item.lower() != 'soap':
      grocery_list.append(item.lower())
      grocery_num.append('1')
    elif item.lower() == 'soap': #easter egg MUAHAHHAHAHAH
      grocery_list.append('Go to the pharmacy for it. ')
      grocery_num.append('1')
    elif item.lower() in grocery_list:
      new = str(int(grocery_num[grocery_list.index(item.lower())])+1)
      grocery_num.remove(grocery_num[grocery_list.index(item.lower())])
      grocery_num.insert(grocery_list.index(item.lower()),new)
    return render_template('index.html', grocery_list=grocery_list, grocery_num=grocery_num)
def remove_item():
  item = request.form['item']
  if item.lower() in grocery_list:
    if int(grocery_num[grocery_list.index(item)]) > 1:
      int(grocery_num[grocery_list.index(item)] - 1)
    else:
      grocery_num.remove(grocery_list[item])
      grocery_list.remove(grocery_list.index(item))
  else:
    print('item not found')
  return render_template('index.html', grocery_list=grocery_list, grocery_num=grocery_num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
  
