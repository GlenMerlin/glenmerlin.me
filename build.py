import os
import re

def generate_html():
    with open('art_template.html', 'r') as file:
        html = file.read()
    contents = os.listdir('images')
    html+= """         <ul>
            """
    for item in contents:
        html += f"""<li>
              <a href="{getLink(item)}" target="_blank">
                <img src="images/{item}" class="gallery__img" />
              </a>
            </li>
            """
    html += """</ul>        
        </div>
      </div>
    </div>
  </body>
</html>
"""
    print(html)
    with open('art.html', 'w') as file:
        file.write(html)

def getLink(item):
    item = re.split("_", item, 1)
    match item[0]:
        case "artsbvg":
            return "https://bsky.app/profile/artsbvg.bsky.social"
        case "aussiekitten":
            return "https://bsky.app/profile/aussiekitten.com"
        case "dot":
            return "https://bsky.app/profile/artisticdot.bsky.social"
        case "fleur":
                return "https://bsky.app/profile/fleur.bsky.social"
        case "glen":
                return "https://bsky.app/profile/stardustfox.bsky.social" # * This is because I hard link to this specific image file frequently and don't want to change my muscle memory for automation
        case "hush":
                return "https://bsky.app/profile/hushmccloud.bsky.social"
        case "kibyts":
                return "https://bsky.app/profile/kibyts.bsky.social"
        case "kingterrae":
                return "https://bsky.app/profile/kingterrae.bsky.social"
        case "kirodog":
                return "https://bsky.app/profile/kiro.dog"
        case "mauzymice":
                return "https://bsky.app/profile/mauzymice.bsky.social"
        case "nashew":
                return "https://bsky.app/profile/nashew.bsky.social"
        case "petunia":
                return "https://bsky.app/profile/petuniabubbles.bsky.social"
        case "rainykitten":
                return "https://cara.app/rainyli"
        case "redmoon":
            return "https://bsky.app/profile/xredmoon.com"
        case "shlimaz":
            return "https://bsky.app/profile/shlimaz.bsky.social"
        case "ssnowstarr":
            return "https://bsky.app/profile/ssnowstarr.bsky.social"
        case "wackyanimal":
            return "https://bsky.app/profile/wackyanimal.bsky.social"
        case "zapderg":
            return "https://bsky.app/profile/magiczapdragon.bsky.social"        
        case _:    
            return "https://example.com"
    
generate_html()