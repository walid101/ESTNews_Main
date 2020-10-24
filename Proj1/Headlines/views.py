from django.shortcuts import render
import random
from django.http import HttpResponse
from newsapi import NewsApiClient
def Headlines_view(request,*args, **kwargs):
    newsapi = NewsApiClient(api_key = "54c8a5ccbe69480fa3b3c01ecdbc7e54")
    #q = "movies" or "celebrity" or "animation" or "cartoon"
    topTechHeadlines = newsapi.get_top_headlines(language = "en", category = "technology", country = "us")
    topEntertainHeadlines = newsapi.get_top_headlines(language = "en", category = "entertainment", country = "us")
    topSportsHeadlines = newsapi.get_top_headlines( language = "en", category = "sports", country = "us", q = "sports")

    techArticles =  topTechHeadlines['articles']
    random.shuffle(techArticles)
    entArticles = topEntertainHeadlines['articles']
    random.shuffle(entArticles)
    sportsArticles = topSportsHeadlines['articles']
    random.shuffle(sportsArticles)

    techDesc = [] #this is the techArticle description
    techNews = [] #this is the tech Article news
    techImg = [] #this is the front image of the tech article
    techUrl = []

    entDesc = []
    entNews = []
    entImg = []
    entUrl = []

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

    for i in range(len(entArticles)):
        currArticleB =entArticles[i]
        entDesc.append(currArticleB['description'])
        entNews.append(currArticleB['title'])
        entImg.append(currArticleB['urlToImage'])
        entUrl.append(currArticleB['url'])

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
    entList = {
        "entNews":entNews,
        "entDesc":entDesc,
        "entImg":entImg,
        "entUrl":entUrl,
    }
    sportsList = {
        "sportsNews":sportsNews,
        "sportsDesc":sportsDesc,
        "sportsImg":sportsImg,
        "sportsUrl":sportsUrl,
    }
    masterList2 = {
        "techList":techList,
        "entList":entList,
        "sportsList":sportsList,
    }
    masterList = list(zip(techList, entList, sportsList))
    return render(request, "Headlines_main.html", context = masterList2)
# Create your views here.
