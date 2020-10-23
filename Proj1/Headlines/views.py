from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
def Headlines_view(request,*args, **kwargs):
    newsapi = NewsApiClient(api_key = "8e9afb8804be404fb277c28fb68d340c")
    topTechHeadlines = newsapi.get_top_headlines(language = "en", category = "technology", country = "us")
    topBusinessHeadlines = newsapi.get_top_headlines(language = "en", category = "business", country = "us")
    topSportsHeadlines = newsapi.get_top_headlines( language = "en", category = "sports", country = "us")

    techArticles = topTechHeadlines['articles']
    businessArticles = topBusinessHeadlines['articles']
    sportsArticles = topSportsHeadlines['articles']

    #myList = {
        #"Headline Name" : "Tesla Making Huge Strides!",
        #"Headline Date" : "March 1st, 2001"
    #}
    techDesc = [] #this is the techArticle description
    techNews = [] #this is the tech Article news
    techImg = [] #this is the front image of the tech article
    techUrl = []

    busDesc = []
    busNews = []
    busImg = []
    busUrl = []

    sportsDesc = []
    sportsNews = []
    sportsImg = []
    sportsUrl = []

    for i in range(len(techArticles)):
        currArticle = techArticles[i]
        techDesc.append(currArticle['description'])
        techNews.append(currArticle['title'])
        techImg.append(currArticle['urlToImage'])
        techUrl.append(currArticle['url'])

    for i in range(len(businessArticles)):
        currArticleB = businessArticles[i]
        busDesc.append(currArticleB['description'])
        busNews.append(currArticleB['title'])
        busImg.append(currArticleB['urlToImage'])
        busUrl.append(currArticleB['url'])

    for i in range(len(sportsArticles)):
        currArticleC = sportsArticles[i]
        sportsDesc.append(currArticleC['description'])
        sportsNews.append(currArticleC['title'])
        sportsImg.append(currArticleC['urlToImage'])
        sportsUrl.append(currArticleC['url'])

    #techList = list(zip(techNews, techDesc, techImg, techUrl))
    #busList = list(zip(busNews, busDesc, busImg, busUrl))
    #sportsList = list(zip(sportsNews, sportsDesc, sportsImg, sportsUrl))

    techList = {
        "techNews" : techNews,
        "techDesc" : techDesc,
        "techImg" : techImg,
        "techUrl" : techUrl,
    }
    busList = {
        "busNews":busNews,
        "busDesc":busDesc,
        "busImg":busImg,
        "busUrl":busUrl,
    }
    sportsList = {
        "sportsNews":sportsNews,
        "sportsDesc":sportsDesc,
        "sportsImg":sportsImg,
        "sportsUrl":sportsUrl,
    }
    masterList2 = {
        "techList":techList,
        "busList":busList,
        "sportsList":sportsList,
    }
    masterList = list(zip(techList, busList, sportsList))
    return render(request, "Headlines_main.html", context = masterList2)
# Create your views here.
