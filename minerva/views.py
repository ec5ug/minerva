from django.shortcuts import render
from oauth_app.models import UserInfo
from oauth_app.forms import RegistrationForm
from datetime import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user
        if len(UserInfo.objects.filter(user=username)) == 0:
            current_date = datetime.today().date()
            form = RegistrationForm()
            return render(request, 'index.html', {'form': form})
    return render(request, 'index.html')
