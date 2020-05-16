from flask import Flask, request, send_from_directory, send_file


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def root():
    return send_from_directory(directory='hexo/', filename='index.html')

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory(directory='hexo/images', filename=path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(directory='hexo/js', filename=path)    

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(directory='hexo/css', filename=path)   

@app.route('/libs/<path:path>')
def send_libs(path):
    return send_from_directory(directory='hexo/libs', filename=path)   

@app.route('/posts', defaults={'path' : ''})
@app.route('/posts/<path:path>')
def send_posts(path):
    if path == '':
        return send_from_directory(directory='hexo/posts', filename=path + 'index.html')
    else:
        return send_from_directory(directory='hexo/posts', filename=path + '/index.html')   

@app.route('/categories/<path:path>')
def send_categories(path):
    return send_from_directory(directory='hexo/categories', filename=path + '/index.html')   

@app.route('/tags/<path:path>')
def send_tags(path):
    return send_from_directory(directory='hexo/categories', filename=path + '/index.html')  

@app.route('/about')
def send_about():
    return send_from_directory(directory='hexo/about', filename='index.html')  

@app.route('/<path:path>')
def send_dir(path):
    return send_from_directory(directory='hexo', filename=path )