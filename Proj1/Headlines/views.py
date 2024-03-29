from django.shortcuts import render
import random
from django.http import HttpResponse
from newsapi import NewsApiClient
def Headlines_view(request,*args, **kwargs):
    newsapi = NewsApiClient(api_key = "71e591475a7246dfa7c6aa3915c9798a")
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
        currArticleB = entArticles[i]
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

    #if(techList['techImg'][0] == None):
     #   hold = techList['techImg'][0]
      #  techList['techImg'][0] = techList['techImg'][1]
       # techList['techImg'][1] = hold
    #if (sportsList['sportsImg'][0] == None):
     #   holdB = sportsList['sportsImg'][0]
      #  sportsList['sportsImg'][0] = sportsList['sportsImg'][1]
       # sportsList['sportsImg'][1] = holdB
    #if (entList['entImg'][0] == None):
     #   holdC = entList['entImg'][0]
      #  entList['entImg'][0] = entList['entImg'][1]
       # entList['entImg'][1] = holdC
    masterList2 = {
        "techList":techList,
        "entList":entList,
        "sportsList":sportsList,
    }
    masterList = list(zip(techList, entList, sportsList))
    return render(request, "Headlines_main.html", context = masterList2)
# Create your views here.
