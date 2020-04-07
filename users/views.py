from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView, DetailView, FormView
from .forms import StudentSignUpForm, MentorSignUpForm, CommentForm
from .models import Course, User, Comment
from django.utils.decorators import method_decorator
from .decorators import mentor_required, student_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic.edit import FormView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    try:
        if request.user.is_mentor:
            return redirect('mentor_profile')
        else:
            return redirect('student_profile')
    except:
        print("Trace")

    return render(request, 'home.html', {})

def teachers_list(request):
    return render(request, 'list-of-teachers.html', {})

def subscribers_list(request):
    return render(request, 'list-of-subscriber.html', {})

def about(request):
    try:
        if request.user.is_mentor:
            return redirect('mentor_profile')
        else:
            return redirect('student_profile')
    except:
        print("Trace")

    return render(request, 'about.html', {})
def contact(request):
    try:
        if request.user.is_mentor:
            return redirect('mentor_profile')
        else:
            return redirect('student_profile')
    except:
        print("Trace")

    return render(request, 'contact.html', {})


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/reg-student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login/')

class MentorSignUpView(CreateView):
    model = User
    form_class = MentorSignUpForm
    template_name = 'registration/reg-mentor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Mentor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class MentorListView(ListView):
    model = User
    context_object_name = 'mentors'
    template_name = 'list-of-teachers.html'

class CourseDetail(FormView, DetailView):
    model = Course
    form_class = CommentForm
    context_object_name = 'course'
    template_name = 'course_detail.html'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.author = self.request.user
        post_id = Course.objects.get(pk=self.kwargs['pk'])
        form.course = post_id
        form.save()
        return super(CourseDetail, self).form_valid(form)

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.get_object().pk})
    
    
    
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses_list.html'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        return Course.objects.filter(Q(title__icontains=search_query)|Q(author__username__icontains=search_query)|Q(price__icontains=search_query)|
                                     Q(body__icontains=search_query)
                                     )

class MentorProfile(DetailView):
    model = User
    context_object_name = 'mentors'
    template_name = 'mentor-detail.html'

class MentorsListView(ListView):
    model = User
    context_object_name = 'mentors'
    template_name = 'list-of-teachers.html'

class CourseLike(DetailView):
    def post(self, request, pk):
        like = get_object_or_404(Course, pk=pk)
        user = request.user
        if user.is_authenticated:
            if user in like.likes.all():
                like.likes.remove(user)
            else:
                like.likes.add(user)
        return redirect('course_detail', pk)

@method_decorator([login_required, mentor_required], name='dispatch')
class MentorProfileView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'account-mentor.html'
    
    def get_queryset(self):
        return self.request.user.courses.all()



@method_decorator([login_required, student_required], name='dispatch')
class StudentProfileView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'account-student.html'

    def get_queryset(self):
        return self.request.user.courses.all()


@method_decorator([login_required, mentor_required], name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    fields = ('title', 'body', 'language', 'price', 'phone_number', )
    template_name = 'course_add_form.html'

    def form_valid(self, form):
        course = form.save(commit=False)
        course.author = self.request.user
        course.save()
        return redirect('mentor_profile')


@method_decorator([login_required, mentor_required], name='dispatch')
class CourseUpdateView(UpdateView):
    model = Course
    fields = ('title', 'body', 'price', 'phone_number', )
    context_object_name = 'course'
    template_name = 'course_change_form.html'

    def get_queryset(self):
        return self.request.user.courses.all()

    def get_success_url(self):
        return reverse('course_change', kwargs={'pk': self.object.pk})


@method_decorator([login_required, mentor_required], name='dispatch')
class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_delete.html'
    success_url = reverse_lazy('mentor_profile')

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.courses.all()