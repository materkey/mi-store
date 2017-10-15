# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.views.generic import UpdateView

from reviews.models import Review


class ReviewUpdate(UpdateView):
    model = Review
    template_name = 'reviews/edit_review.html'
    fields = 'text', 'deleted'

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.object.reviewed_product.pk})
