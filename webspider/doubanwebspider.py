import requests
import sqlite3
import time
from bs4 import BeautifulSoup


def get_data():
    url = 'https://api.douban.com/v2/movie/top250?count=50'
    req = requests.get(url)
    data = req.json()
    return data


def data_detail(movies, movie):
    rank = movies.index(movie)+1
    title = movie['title']
    poster = movie['images']['medium'].split('/')[-1]
    averagegrade = movie['rating']['average']
    directorlist = [i['name'] for i in movie['directors']]
    castslist = [i['name'] for i in movie['casts']]
    douban_id = movie['id']

    director = ', '.join(directorlist)
    casts = ', '.join(castslist)

    return title,rank,poster,averagegrade,director,casts,douban_id


def download_pic(movie):
    posterdownload = movie['images']['medium']
    pic = requests.get(posterdownload)
    poster = movie['images']['medium'].split('/')[-1]
    with open('../blog/static/movieposter/' + poster, 'wb') as f:
        f.write(pic.content)
        time.sleep(1.5)
        print('down: ', poster)


def get_comment(movie_id):
    url = 'https://movie.douban.com/subject/' + movie_id
    req = requests.get(url)
    time.sleep(1.5)
    soup = BeautifulSoup(req.text, 'lxml')
    comments = soup.find('div', id="hot-comments").find_all('div', class_="comment")
    commentdata = []
    for comment in comments:
        commentuser = comment.h3.find('span', class_="comment-info").a.string # user
        commenttime = comment.h3.find('span', class_="comment-time")["title"] # time
        commentgrade = comment.h3.find('span', class_="rating")["title"] # 评分
        commentcontent = comment.p.span.string # content
        commentdata.append([commentuser, commenttime, commentgrade, commentcontent])
    return commentdata


def insert_str(moviedata):
    insert_content = "insert into blog_movies (title,rank,poster,averagegrade,director,casts,movie_id) values('%s',%d,'%s',%.1f,'%s','%s',%s);" % moviedata
    print(insert_content)
    c.execute(insert_content)


def insert_commment(moviedata, commentdata):
    print('get the cursor')
    cursor = c.execute("SELECT id from blog_movies where douban_id=%s;" % moviedata[-1])
    print('get movie_id')
    movie_id = [row[0] for row in cursor][0] # Movies 对象的id
    print('done,movie_id:', movie_id)

    for comment in commentdata:
        print('get comment')
        insert_comment = "insert into blog_commentmovie (user,time,onesgrade,content,whichmovie_id,isdelete) values('%s','%s','%s','%s',%d,'False');" % (comment[0].replace("'","''"),comment[1],comment[2],comment[3].replace("'","''"),movie_id)
        print('ok!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', insert_comment)
        c.execute(insert_comment)


conn = sqlite3.connect('..\db.sqlite3')
c = conn.cursor()

movies = get_data()['subjects'] # 获得 json 数据
for movie in movies:
    moviedata = data_detail(movies, movie) # 获得 movie 详细信息
    commentdata = get_comment(moviedata[-1]) # 获得 movie 详细页评论数据

    # download_pic(movie) # 下载图片
    # insert_str(moviedata) # 插入电影 index 信息到数据库的操作
    insert_commment(moviedata, commentdata) # 插入每一部电影评论到数据库的操作
    print('========================')

conn.commit()
conn.close()
