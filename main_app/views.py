from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.db.models import Avg

from .models import Comment, Parts, Review


@login_required
def home(request):
    parts = Parts.objects.all()
    return render(request, 'home.html', {'parts': parts})



@login_required
def part_detail(request, pk):
    part = get_object_or_404(Parts, pk=pk) # in here i used get_object_or_404 instead of object.get() because it returnes 404 page not founf if there was no part found instead of 500 server error
     
    # calculate average rating
    avg_rating = part.reviews.aggregate(average=Avg('rating'))['average']
    
    context = {
        'part': part,
        'avg_rating': avg_rating,  
    }
    return render(request, 'part_detail.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


@login_required
@require_POST
def add_review(request, pk):
    part = get_object_or_404(Parts, pk=pk)
    rating = int(request.POST.get('rating'))
    review, created = Review.objects.update_or_create(
        part=part,
        user=request.user,
        defaults={'rating': rating}
    )
    return redirect('part_detail', pk=pk)

@login_required
@require_POST
def add_comment(request, pk):
    part = get_object_or_404(Parts, pk=pk)
    comment_text = request.POST.get('comment_text')
    if comment_text:
        Comment.objects.create(part=part, user=request.user, comment_text=comment_text)
    return redirect('part_detail', pk=pk)

@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == 'POST':
        comment.comment_text = request.POST.get('comment_text')
        comment.save()
        return redirect('part_detail', pk=comment.part.pk)
    return render(request, 'update_comment.html', {'comment': comment})

@login_required
@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    part_pk = comment.part.pk
    comment.delete()
    return redirect('part_detail', pk=part_pk)
