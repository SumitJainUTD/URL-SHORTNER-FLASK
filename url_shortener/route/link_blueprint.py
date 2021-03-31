from flask import Blueprint, render_template, request, redirect
from url_shortener.models.link import LinkModel
from datetime import datetime

short = Blueprint("short", __name__)


@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = LinkModel.find_by_short_url(short_url)
    if link:
        link.visits += 1
        link.commit_to_db()
        return redirect(link.original_url)
    else:
        return render_template('404.html'), 404


@short.route('/')
def index():
    return render_template('index.html')


@short.route("/add_link", methods=['POST'])
def add_link():
    original_url=request.form['original_url']
    link = LinkModel.find_by_original_url(original_url)
    if link:
        return render_template("link_added.html", original_url=original_url, new_link=link.short_url)
    else:
        short_url = LinkModel.get_short_url();
        print("short_url" + str(short_url))
        new_link = LinkModel(original_url, short_url)
        new_link.save_to_db()
        return render_template("link_added.html", original_url=original_url, new_link=short_url)
        # short_url, 201

@short.route('/stats')
def get_stats():
    links = LinkModel.get_all_links()
    return render_template("stats.html", links=links)


@short.errorhandler(404)
def page_not_found():
    return '', 404


# class Link():
#
#     def post(self, original_url):
#         link = LinkModel.find_by_original_url(original_url)
#         if link:
#             return link.short_url, 200
#         else:
#             dt = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")
#             short_url = LinkModel.get_short_url;
#             new_link = LinkModel(original_url, short_url, dt)
#             new_link.save_to_db()
#             return short_url, 201


# class LinkList(Resource):
#
#     def get(self):
#         temp_links = []
#         for u in LinkModel.get_all_links():
#             temp_links.append(u.json())
#         return {'links': temp_links}
