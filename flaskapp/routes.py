from flaskapp import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    projects = {
        "Narrowband IoT Kit" : {
            "image" : "work-1.jpg",
            "category" : "IoT",
            "date" : "18 Sep. 2018",
            "url" : "https://youtu.be/MC9VRoRNm_o",
            "type" : "youtube"
        },
        "MAURICE":{
            "image" : "capstone1.jpg",
            "category" : "IoT",
            "date" : "3 May 2018",
            "url" : "http://ece4012y2018.ece.gatech.edu/spring/sd18sS4/",
            "type" : "website"
        },
        "CO2 Near Me":{
            "image" : "co2.png",
            "category" : "IoT",
            "date" : "24 May 2020",
            "url" : "https://github.com/kevinlwebb/CO2-Near-Me",
            "type" : "github"
        }
    }

    blogs = {
        "AT&T EGC 2019" : {
            "image" : "egc.jpeg",
            "category" : "Conference",
            "url" : "https://www.linkedin.com/pulse/egc-conference-2019-kevin-webb/",
            "description" : "AT&T Employee Group Conference, an annual event where employees listened to and engaged with company and community leaders on the topics of Diversity and Inclusion.",
            "author" : "Kevin Webb",
            "aimage" : "testimonial-2.jpg"
        },
        "More To Come" : {
            "image" : "post-3.jpg",
            "category" : "Code",
            "url" : "#",
            "description" : "...",
            "author" : "Kevin Webb",
            "aimage" : "testimonial-2.jpg"
        },
        "More To Come Again" : {
            "image" : "post-2.jpg",
            "category" : "Music",
            "url" : "#",
            "description" : "...",
            "author" : "Kevin Webb",
            "aimage" : "testimonial-2.jpg"
        }
    }
    return render_template('home.html', projects = projects, blogs = blogs)