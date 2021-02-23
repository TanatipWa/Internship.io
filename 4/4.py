from flask_restful import Api, Resource
from flask import Flask, jsonify
import json

from bs4 import *
import requests as rq

URL = "https://theinternship.io/"
r2 = rq.get(URL)
soup2 = BeautifulSoup(r2.text, "html.parser")

logoLinks = []
decCompanys = []

tmpLogoLink = soup2.select('img[src^="company/"]')

for img in tmpLogoLink:
    logoLinks.append(img['src'])

tmpDecCompany = soup2.find_all("span", {"class": "list-company"})

for i in tmpDecCompany:
    decCompanys.append(i.text)

numCompany = len(logoLinks)  # แก้ปัญหา company ใหม่ๆ img ลิงค์ไม่ตรงกับ เก่าๆ
for i in range(numCompany):
    minIndex = decCompanys.index(min(decCompanys[i:numCompany], key=len))
    decCompanys[i], decCompanys[minIndex] = decCompanys[minIndex], decCompanys[i]

    logoLinks[i], logoLinks[minIndex] = logoLinks[minIndex], logoLinks[i]

# debug
for l in logoLinks:
    print(l)

# -------------------------------------------------
app = Flask(__name__)
api = Api(app)

imgDict = {}
imgDict["companies"] = []

for l in logoLinks:
    imgDict["companies"].append({"logo": URL + l})

#imgJson = json.dumps(imgDict)


class urlLogo(Resource):
    def get(self):
        return jsonify(imgDict)


api.add_resource(urlLogo, "/companies")

if __name__ == "__main__":
    app.run(debug=True)