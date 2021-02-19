from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
class OrdersPageView(LoginRequiredMixin ,TemplateView):
    template_name = "orders/purchase.html"

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY

        return context

@login_required(login_url='account_login')
def charge(request):

    # get the permission.
    permission = Permission.objects.get(codename="special_status")

    # get the current user.
    current_user = request.user

    # Add user's permission set.
    current_user.user_permissions.add(permission)

    if request.method == "POST":
        charge = stripe.Charge.create(amount=450, currency='inr', description='Purchase all books', source=request.POST['stripeToken'])
    
    return render(request, 'orders/charge.html')