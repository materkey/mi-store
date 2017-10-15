# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView

from reviews.models import Review

class ReviewUpdate(UpdateView):
    model = Review
    template_name = 'reviews/edit_review.html'
    fields = 'text', 'deleted'

    def form_valid(self, form):
        super(ReviewUpdate, self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        # return self.request.META['HTTP_REFERER']
        return reverse('products:details', kwargs={'pk': self.object.reviewed_product.pk})
