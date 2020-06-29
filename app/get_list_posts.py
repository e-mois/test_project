import json
import datetime

filename_posts = 'post.json'
filename_comments = 'comments.json'


def load_json(filename):
    with open(filename) as f:
        posts_list = json.load(f)
    return posts_list

def format_date(post_time):
    format = '%Y-%m-%dT%H:%M:%S'
    datetime_str = datetime.datetime.strptime(post_time, format)
    return datetime_str


def get_comments_count(post, comments_lists):
    count = 0
    for comment in comments_lists['comments']:
        if comment['post_id'] is post['id']:
            count += 1
    return count


def make_list_post(filename_posts, filename_comments):
    try:
        post_lists = load_json(filename_posts)
        comments_lists = load_json(filename_comments)

        return_posts_dict = {
            'posts': [],
            'posts_count': 0,
            'list_id': []
        }
        

        for post in post_lists['posts']:
            if post['deleted'] is False and format_date(post['date']) < datetime.datetime.now():
                return_posts_dict['posts'].append(
                    {
                        "id": post['id'], 
                        "title": post['title'],
                        "date": post['date'], 
                        "body": post['body'],
                        "comments_count": get_comments_count(post, comments_lists)
                    }
                )
                return_posts_dict['posts_count'] += 1
                return_posts_dict['list_id'].append(post['id'])

        return return_posts_dict

    except json.decoder.JSONDecodeError:
        print('Файл пуст')
    except FileNotFoundError:
        print('Не найден файл нужный файл')
    except ValueError:
        print('Ошибка')

def make_list_comments(filename_posts, filename_comments, post_id):
    
    list_posts = make_list_post(filename_posts, filename_comments)
    if post_id in list_posts['list_id']:    
        for post in list_posts['posts']:
            if post['id'] == post_id:
                if format_date(post['date']) > datetime.datetime.now():
                    return False
                else:
                    need_post = post
    else:
        return False

    comments_lists = load_json(filename_comments)
    comments = []
    for comment in comments_lists['comments']:
        if comment['post_id'] == post_id:
            comments.append(comment)

    return_post = {
        "id": post_id, 
        "title": need_post['title'],
        "date": need_post['date'], 
        "body": need_post['body'],
        "comments": comments, 
        "comments_count": len(comments)
    }
    return return_post


'''if __name__ == '__main__':
    make_list_comments(filename_posts, filename_comments, 2)'''

