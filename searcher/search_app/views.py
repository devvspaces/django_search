from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline, TrigramSimilarity, TrigramWordSimilarity

from .models import Post


# Search view
def get_posts(request):
    context = dict()

    search = request.GET.get('search')
    if search:
        # For single field searches
        # posts = Post.objects.filter(title__search=search)

        # For multifield searches
        # vector = SearchVector('title', weight='A') +  SearchVector('description', 'body', weight='A')

        # Vectors with weight
        vector = SearchVector('title', weight='A') +  SearchVector('description', 'body', weight='D')

        query = SearchQuery(search)

        # Normal
        # posts = Post.objects.annotate(search=vector).filter(search=query)

        # Ranking method
        ranking = SearchRank(vector, query)

        # Add headline
        headline_description = SearchHeadline('description', search, highlight_all=True)
        headline_body = SearchHeadline('body', search, highlight_all=True)
        posts = Post.objects.annotate(rank=ranking).annotate(hdescription=headline_description).annotate(hbody=headline_body).filter(rank__gte=0.001).order_by('-rank')

        # Searching with TrigramSimilarity
        # posts = Post.objects.annotate(similarity=TrigramWordSimilarity(search, 'title')).filter(similarity__gte=0.3).order_by('-similarity')
    else:
        # Get all the data
        posts = Post.objects.all()

    context['posts'] = posts

    return render(request, 'search_app/index.html', context)