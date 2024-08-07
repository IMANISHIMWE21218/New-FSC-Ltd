from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import CompanyInfo, TestimonialInfo,  OurProjects, Partner, TeamMember, Tag, Blog
from django.db.models import Count


# Create your views here.
def index(request):
    company_info = CompanyInfo.objects.first()
    testimonials = TestimonialInfo.objects.all()
    projects = OurProjects.objects.all()
    partners = Partner.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'fsc/index.html', {
        'company_info': company_info,
        'testimonials': testimonials,
        'projects': projects,
        'partners': partners,
        'team_members': team_members
    })

def projectsingle(request, id):
    company_info = CompanyInfo.objects.first()
    project = get_object_or_404(OurProjects, id=id)
    previous_project = OurProjects.objects.filter(id__lt=project.id).order_by('-id').first()
    next_project = OurProjects.objects.filter(id__gt=project.id).order_by('id').first()
    context = {
        'company_info': company_info,
        'project': project,
        'previous_project': previous_project,
        'next_project': next_project,
    }
    return render(request, 'fsc/project-single.html', context)



def about(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'fsc/about.html', {'company_info': company_info})


from django.shortcuts import render
from .models import Blog, CompanyInfo

def blog(request):
    company_info = CompanyInfo.objects.first()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6)  # Show 6 blogs per page.

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    categories = Blog.objects.values('category').annotate(count=Count('category')).order_by('category')
    recent_posts = Blog.objects.order_by('-date')[:3]
    tags = tags = Tag.objects.all()[:6]

    return render(request, 'fsc/blog.html', {'company_info': company_info, 'blogs': blogs, 'categories': categories , 'recent_posts': recent_posts, 'tags': tags })

def blogsingle(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    company_info = CompanyInfo.objects.first()
     # Get the previous and next posts
    previous_post = Blog.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = Blog.objects.filter(pk__gt=post.pk).order_by('pk').first()
    return render(request, 'fsc/blog-single.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'company_info': company_info
    })


def contact(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'fsc/contact.html',  {'company_info': company_info})

def agroforestry(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'fsc/agroforestry.html', {'company_info': company_info})

def biogasGeneration(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'fsc/BiogasGeneration.html', {'company_info': company_info})


def career(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'fsc/career.html',  {'company_info': company_info})


def OrganicManureProduction(request):
    company_info = CompanyInfo.objects.first()

    return render(request, 'fsc/OrganicManureProduction.html', {'company_info': company_info})


def RainwaterHarvesting(request):
    company_info = CompanyInfo.objects.first()

    return render(request, 'fsc/RainwaterHarvesting.html', {'company_info': company_info})

def RuralDevelopmentSolutions(request):
    company_info = CompanyInfo.objects.first()

    return render(request, 'fsc/RuralDevelopmentSolutions.html', {'company_info': company_info})

def WasteManagement(request):
    company_info = CompanyInfo.objects.first()

    return render(request, 'fsc/WasteManagement.html', {'company_info': company_info})

def services(request):
    company_info = CompanyInfo.objects.first()

    return render(request, 'fsc/services-s2.html', {'company_info': company_info})




