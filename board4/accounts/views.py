from django.shortcuts import render, redirect 
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 회원가입, 로그인
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 요청 보낸 사용자가 인증되었다(로그인했다)면 => 바로 돌려보내기
    # url(/accounts/signup)을 바로 쳤을 때 들어가지는걸 막는거임
    if request.user.is_authenticated:
        return redirect('board:index')
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board:index')
    else: # GET
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

@require_http_methods(['GET','POST'])
def login(request):
    # 요청 보낸 사용자가 인증되었다(로그인했다)면 => 바로 돌려보내기
    # url(/accounts/login)을 바로 쳤을 때 들어가지는걸 막는거임
    if request.user.is_authenticated:
        return redirect('board:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) #request.POST가 사용자가 넣은 id, password
        if form.is_valid():
            user = form.get_user()
            # 쿠키(팔찌) 세팅
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('board:index')