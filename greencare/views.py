from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from greencare.forms import commentsForm, ServiceDealsForm
from greencare.models import Ourteam, ContactDetails, News, ServicesDeals, TermsAndConditions, Service, Experience


def index(request):
    contactus = ContactDetails.objects.all()
    news = News.objects.all()[:3]
    return render(request, 'greencare/index.html', {
        'contactus': contactus,
        'news': news,
    })


def about(request):
    global r, team2
    team = Ourteam.objects.all()

    for c in team:
        r = c.position

    if r is not '':
        team2 = 'team2'
    contactus = ContactDetails.objects.all()
    return render(request, 'greencare/about.html', {
        'contactus': contactus,
        'team': team,
        'team2': team2,
    })


def services(request):
    contactus = ContactDetails.objects.all()
    servicedeals = ServicesDeals.objects.filter()
    termsandconditions = TermsAndConditions.objects.all()
    services = Service.objects.all()
    return render(request, 'greencare/services.html', {
        'contactus': contactus,
        'webdevdeals': servicedeals,
        'termsandconditions': termsandconditions,
        'services': services,
    })


def service_detail(request, slug):
    #global termsAndConditions
    service = get_object_or_404(Service, slug=slug)
    form = ServiceDealsForm()

    try:
        termsAndConditions = TermsAndConditions.objects.get(nameofservice=service)
        #print('SERVICE NAME: ', service)
        #print("TERMS AND CONDITIONS: ", termsAndConditions.termsconditions)
    except:
        #Still redirect to the service details page
        return render(request, 'greencare/service_details.html',
                      {
                          'form': form,
                          'service': service,
                      })

    if request.method == 'POST':
        form = ServiceDealsForm(request.POST)

        if form.is_valid():
            # Create a new user object but avoid saving it yet
            add_fee = form.save(commit=False)
            add_fee.save()
            #return redirect('services/', slug)
            return render(request, 'greencare/service_details.html', {
                'form': form,
                'termsAndConditions': termsAndConditions,
                'service': service,
                'success': 'success',
            })
            # return HttpResponse('Your Details Have been Submitted')
        else:

            return render(request, 'greencare/service_details.html', {
                'form': form,
                'termsAndConditions': termsAndConditions,
                'service': service,
            })


    return render(request, 'greencare/service_details.html',
                  {
                      'form': form,
                      'service': service,
                      'termsAndConditions': termsAndConditions,
                  })


def contactus(request):
    contactus = ContactDetails.objects.all()

    if request.method == 'POST':
        addCommentForm = commentsForm(request.POST)
        if addCommentForm.is_valid():
            # Create a new user object but avoid saving it yet
            add_comment = addCommentForm.save(commit=False)
            add_comment.save()

            # return redirect('adminresults')
            return HttpResponse('Thank You For Your Message!')
        else:
            form = commentsForm()
            return render(request, 'greencare/contact.html',
                          {
                              'contactus': contactus,
                              'form': form,
                          })

    form = commentsForm()
    return render(request, 'greencare/contact.html', {
        'contactus': contactus,
        'form': form,
    })


def newslist(request):
    news = News.objects.all()
    return render(request, 'greencare/newslist.html',
                  {
                      'news': news,
                  })


def newsdetail(request, news_id):
    news = News.objects.all()

    try:
        newsdetail = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("News does not exist!")
    return render(request, 'greencare/newsdetail.html',
                  {
                      'newsdetail': newsdetail,
                  })


def agriculturehome(request):
    experience = Experience.objects.all()
    return render(request, 'agriculture/index.html', {
        'experience': experience,
    })
