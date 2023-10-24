from flask import Flask,render_template,request
flask1=Flask(__name__)

@flask1.route("/")

#route your webpage

def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	return render_template("index.html",visitors=visitors_count)



@flask1.route("/",methods=["POST"])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	text1=request.form["text"]
	url="https://covidstats-sdbd.onrender.com/?country="+text1
	return render_template("index.html",image=url,visitors=visitors_count)

if __name__=="__main__":
	flask1.run()

#add code for executing flask