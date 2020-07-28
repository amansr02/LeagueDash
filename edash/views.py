from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import os
from datetime import datetime
from datetime import date

# Create your views here.

@login_required
def teams(request):
    x: PandaScore = PandaScore()
    teams = x.get_team_list()
    return render(request,'edash/teams.html',{'teams':teams,'nbar':'teams'})

@login_required
def match(request):
    if(request.method=='GET'):
        x: PandaScore = PandaScore()
        matches = x.get_match_list()
        print(matches[0]['id'])
        current_week = date.today().isocalendar()[1]
        upcoming_matches=[]
        for i in range(0,len(matches)):
            week = datetime.fromisoformat(matches[i]['scheduled_at'][0:-1]).isocalendar()[1]
            matches[i]['scheduled_at'] = datetime.fromisoformat(matches[i]['scheduled_at'][0:-1]).strftime("%A,%b %d %Y,%H:%M:%S")
            if(week==current_week):
                upcoming_matches.append(matches[i])
        return render(request,'edash/match.html',{'matches':matches,'nbar':'matches','upcoming_matches':upcoming_matches})
    else:
        pass

@login_required
def team_detail(request,team_id):
    if(request.method=='GET'):
        x: PandaScore = PandaScore()
        team = x.get_team_details(team_id)
        print(team[0]['id'])
        return render(request,'edash/team_detail.html',{'team':team[0],'nbar':'teams'})
    else:
        pass

class PandaScore:
    def __init__(self):
        self.url = "https://api.pandascore.co/lol/"
        self.params =  {'token': os.environ.get('PANDASCORE',''),'page':'1'}
        
    def get_player_list(self,team):
        pass

    def get_team_list(self):
        teams = requests.get(self.url+"series/2347/teams/",params=self.params)
        return teams.json()
    
    def get_match_list(self):
        matches = requests.get("https://api.pandascore.co/leagues/4198/matches/",params=self.params)
        return matches.json()

    def get_team_details(self,id):
        params = self.params
        params['filter[id]']=str(id)
        team = requests.get(self.url+"teams",params=params)
        return team.json()
