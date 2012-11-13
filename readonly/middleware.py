#!/usr/bin/env python
# encoding: utf-8
from django.conf import settings
from django.contrib.auth import logout


class ReadOnlyMiddleware:

    def process_request(self, request):
        if getattr(settings, 'READ_ONLY', False):
            if request.user.is_authenticated():
                logout(request)
            if request.method == 'POST':
                request.POST = {}
            request.read_only = True
        return None
