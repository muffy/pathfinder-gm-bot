import os

from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
"""
<html><head>
<title>Encounter bot</title>
<link rel="shortcut icon" href="/static/encounter-bot.ico">
<link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
<style type="text/css">
.jumbotron {
    background: #532f8c;
        color: white;
padding-bottom: 80px
}
.jumbotron .btn-primary {
    background: #845ac7;
        border-color: #845ac7
}
.jumbotron .btn-primary:hover {
    background: #7646c1
}
.jumbotron p {
    color: #d9ccee;
        max-width: 75%;
margin: 1em auto 2em
}
.navbar+.jumbotron {
    margin-top: -20px
}
.jumbotron .lang-logo {
    display: block;
background: #b01302;
border-radius: 50%;
overflow: hidden;
width: 100px;
height: 100px;
margin: auto;
border: 2px solid white
}
.jumbotron .lang-logo img {
    max-width: 100%
}


</style>
</head>
<body>


<div class="jumbotron text-center">
<a href="/" class="lang-logo">
<img src="/static/encounter-bot.png">
</a>
<h1>Encounter bot for Slack</h1>
<a type="button" class="btn btn-large btn-primary" href="https://slack.com/oauth/authorize?scope=bot&amp;client_id=None">
Add to Slack
</a>
</div>
<div class="container">
</div>




</body></html>
"""