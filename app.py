from flask import Flask,render_template,request
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/show1")
def show1():
    return render_template("show1.html")
@app.route("/show2")
def show2():
    return render_template("show2.html")
@app.route("/show3")
def show3():
    return render_template("show3.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/design1")
def design1():
    return render_template("design1.html")

@app.route("/design2")
def design2():
    return render_template("design2.html")

@app.route("/design3")
def design3():
    return render_template("design3.html")

@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/form2")
def form2():
    return render_template("form2.html")


@app.route("/form3")
def form3():
    return render_template("form3.html")

@app.route('/upload', methods=["GET","POST"])
def upload():
   if request.method == "POST":
       name = request.form.get("fname")
       lname = request.form.get("lname")
       schoolname = request.form.get("schoolname")
       collegename = request.form.get("collegename")
       phonenumber = request.form.get("phonenumber")
       email = request.form.get("email")
       skill1 = request.form.get("skill1")
       skill2 = request.form.get("skill2")
       skill3 = request.form.get("skill3")
       skill4 = request.form.get("skill4")
       about = request.form.get("about")
       
       
       key = uuid.uuid1()
       img = request.files["dp"]
       img.save(f"static/images/{img.filename}")
       img_new_name = f"{key}{img.filename}"
       os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")

       return render_template("Design1.html",dname = name,dlname = lastname,dsch = school,
       img = img_new_name, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,
       ds4 = skill4,dabout = about,ddp=dp)

@app.route('/upload2', methods=["GET","POST"])
def upload2():
    #  name , date of birth, height, education, reliion, grand father, grand mother, mother father, brother, sister, address

   if request.method == "POST":
       fullname = request.form.get("fullname")
       dob = request.form.get("dob")
       height = request.form.get("height")
       hq = request.form.get("hq")
       religion = request.form.get("religion")
       grandfather = request.form.get("grandfather")
       grandmother = request.form.get("grandmother")
       father = request.form.get("father")
       mother = request.form.get("mother")
       brother = request.form.get("brother")
       sister = request.form.get("sister")
       address = request.form.get("address")

    #    key = uuid.uuid1()
    #     #Image Uploading Method
    #    img = request.files["dp"]
    #    img.save(f"static/images/{img.filename}")
    #    img_new_name = f"{key}{img.filename}"
    #    os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")

       return render_template("design2.html",dbfullname = fullname,dbdob = dob,dbheight = height, 
       dbhq = hq,dbreligion = religion,dbgrandfather=grandfather,dbgrandmother=grandmother,
       dbfather=father,dbmother=mother,dbbrother=brother,dbsister=sister,bdaddress=address,)

@app.route('/upload3', methods=["GET","POST"])
def upload3():
    if request.method== "POST":
        # // fullname,dob, cnumber, email, religion, father, mother, sex,nationality, maritalstatus,address
        fullname = request.form.get("fullname")
        dob = request.form.get("dob")
        religion = request.form.get("religion")
        father = request.form.get("father")
        mother = request.form.get("mother")
        address = request.form.get("address")
        cnumber = request.form.get("cnumber")
        email = request.form.get("email")
        sex = request.form.get("sex")
        nationality = request.form.get("nationality")
        maritalstatus = request.form.get("maritalstatus")

        # 10the details
        # / schoolname,passingyear, boardname,percentage
        schoolname = request.form.get("schoolname")
        passingyear = request.form.get("passingyear")
        boardname= request.form.get("boardname")
        percentage = request.form.get("percentage")

        # 12th details
        cschoolname = request.form.get("cschoolname")
        cstream = request.form.get("cstream")
        cpassingyear = request.form.get("cpassingyear")
        cboardname= request.form.get("cboardname")
        cpercentage = request.form.get("cpercentage")

        # skill
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4= request.form.get("skill4")

        # hobies
        hoby1 = request.form.get("hoby1")
        hoby2 = request.form.get("hoby2")
        hoby3 = request.form.get("hoby3")

        place = request.form.get("place")
        date=datetime.today().strftime('%d-%m-%Y')
       
    
    return render_template("design3.html",dbfullname=fullname,dbdob=dob,dbreligion=religion,dbfather=father,dbmother=mother,dbaddress=address,dbcnumber=cnumber,
dbemail=email,dbsex=sex,dbnationality=nationality,dbmaritalstatus=maritalstatus,dbschoolname=schoolname,dbpassingyear=passingyear,
dbboardname=boardname,dbpercentage=percentage,dbcshoolname=cschoolname,dbcstream=cstream,dbcpassingyear=cpassingyear,
dbcboardname=cboardname,dbcpercentage=percentage,dbskill1=skill1,dbskill2=skill2,dbskill3=skill3,dbskill4=skill4,dbhoby1=hoby1,
dbhoby2=hoby2,dbhoby3=hoby3,dbplace=place,dbdate=date)

if __name__ == ("__main__"):
    app.run(debug=True,host=8000)
