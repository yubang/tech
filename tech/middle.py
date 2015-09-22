# coding:UTF-8


from django.shortcuts import redirect
import re


class PowerCheck(object):
    def process_request(self, request):
        if re.search(r'^/admin', request.path) and 'admin' not in request.session:
            if request.path != '/admin/account':
                return redirect('/admin/account')
