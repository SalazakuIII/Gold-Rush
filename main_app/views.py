from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    if "gold_src" not in request.session:
        request.session["gold_amt"] = 0
        request.session["activity_log"] = []
        request.session.save()
        return redirect("/display")

def display(request):
    return render(request, "index.html")

def process(request):
    timestamp = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
    if request.POST["gold_src"] == 'Farm':
        change_amt = random.randint(10, 20)
        action_msg = f"<p class='activity_log gain'> Earned {change_amt} gold from the Farm! ({timestamp})</p>"
        print("CHANGE AMT: ", change_amt, " on ", timestamp)
    elif request.POST["gold_src"] == 'Cave':
        change_amt = random.randint(5, 10)
        action_msg = f"<p class='activity_log', 'gain'> Earned {change_amt} gold from the Cave! ({timestamp})</p>"
        print("CHANGE AMT: ", change_amt, " on ", timestamp)
    elif request.POST["gold_src"] == 'House':
        change_amt = random.randint(2, 5)
        action_msg = f"<p class='activity_log gain'> Earned {change_amt} gold from the House! ({timestamp})</p>"
        print("CHANGE AMT: ", change_amt, " on ", timestamp)
    elif request.POST["gold_src"] == 'Casino':
        change_amt = random.randint(-50, 50)
        if change_amt > 0:
            action_msg = f"<p class='activity_log' class='gain'> Entered a casino and won {change_amt} while gambling!!! ({timestamp})</p>"
            print("CHANGE AMT: ", change_amt, " on ", timestamp)
        elif change_amt == 0:
            action_msg = f"<p class='activity_log neutral'> Entered a casino and broke-even gambling!!! ({timestamp})</p>"
            print("CHANGE AMT: ", change_amt, " on ", timestamp)
        elif change_amt < 0:
            action_msg = f"<p class='activity_log loss'> Entered a casino and lost {change_amt} while gambling!!! ({timestamp})</p>"
            print("CHANGE AMT: ", change_amt, " on ", timestamp)
        

    request.session["gold_amt"] += change_amt
    request.session["activity_log"].append(action_msg)
    request.session.save()

    return redirect("/display")

def delete_session_data(request):
    del request.session["gold_amt"]
    del request.session["activity_log"]
    request.session.save()
    print("Reset Initiated | Gold Count Reset")
    return redirect("/")