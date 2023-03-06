from django.urls import re_path
from world.views import plaintext, json, db, dbs, fortunes, update

urlpatterns = [
    re_path(r'^plaintext$', plaintext),
    re_path(r'^json$', json),
    re_path(r'^db$', db),
    re_path(r'^dbs$', dbs),
    re_path(r'^fortunes$', fortunes),
    re_path(r'^update$', update),
]
