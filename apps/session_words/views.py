from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
	if 'wordlist' not in request.session:
		request.session['wordlist'] = []
	return render(request, "session_words/index.html")

def process(request):
	time = strftime("%Y-%m-%d %H:%M %p", localtime())
	# print time
	print request.POST
	if request.method == 'POST':
		newWord = request.POST['newWord']
		color = request.POST['color']
		# size = request.POST['size']
		if "size" in request.POST:
			size = request.POST['size']
			# print size, "inside"
		else:
			size = ""
			# print size, "else"
		if 'wordlist' not in request.session:
			request.session['wordlist'] = []
		
		words = [{
			'word': newWord,
			'color': color,
			'size': size,
			'time':time
		}]

		request.session['wordlist'] += words
	# print request.session['wordlist']
	return redirect('/', words=request.session['wordlist'])


def clear(request):
	del request.session['wordlist']
	return redirect('/')

























	# print request.POST

	
	# if "newWord" in request.POST and "big" in request.POST:
	# 	request.session['newWord']= request.POST['newWord']
	# 	request.session['color']= request.POST['color']
	# 	request.session['big']= request.POST['big']

	# elif "newWord" in request.POST and not "big" in request.POST:
	# 	# print "NEWWORD"
	# 	request.session['newWord'] = request.POST['newWord']
	# 	request.session['color'] = request.POST['color']
	# 	request.session['big']= "16px"

	# elif "clear" in request.POST:
	# 	request.session['newWord'] = 0
	# 	request.session['color'] = 0
	# 	request.session['big'] = 0

	# context = [{
	# "newWord": request.session['newWord'],
	# "color": request.session['color'],
	# "big": request.session['big']
	# }]	

	# if not request.session["messages"]:
	# 	request.session["messages"] = []
	# elif request.session["messages"]:
	# 	request.session["messages"] += context

	
	# print "yo!", request.session["messages"]

	# return redirect("/")