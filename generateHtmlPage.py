
global topOfPage
topOfPage = '''
<!DOCTYPE html>
<html lang=eng>

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width = device-width, initial-scale = 1">
  <title>Greg Murray</title>

  <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.0.47/jquery.fancybox.min.css" />
  <link rel="stylesheet" type="text/css" href="./static/styles.css">
  <link rel="icon" href="./static/icon.png">
</head>

<body>
  <div class="hidden-xs">
    <div class="arrow" id="upArrow">
      <span class="glyphicon glyphicon-chevron-up navArrow"></span>
    </div>
    <div class="arrow" id="downArrow">
      <span class="glyphicon glyphicon-chevron-down navArrow"></span>
    </div>
  </div>
  <div class="hidden-lg hidden-md hidden-sm">
    <!-- mobile nav bar -->
    <div class="btn-group btn-group-lg mobile-top">
      <button id="mobileNavButton" type="button" class="btn btn-default">
      <span class="glyphicon glyphicon-align-justify colorWhite" aria-hidden="true"></span>
      </button>
        <div class="dropdown-menu dropdown-menu-left" id="mobileDrop">
          <div class="closeMobile">
            <span class="glyphicon glyphicon-menu-up" id="closeMobileDrop"></span>
          </div>
          <div class="dropdown-item" id="mobileAboutMe">My Work</div>
          <div class="dropdown-item" id="mobileProjects">My Projects</div>
          <div class="dropdown-item" id="mobileTravel">My Travel</div>
          <div class="dropdown-item" id="mobileContact">Contact</div>
        </div>
    </div>
  </div>
  <!-- background picture -->
  <a href="#top"></a>
  <div class="row">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="topPic">
      <div class="picture hidden-xs">
        <div id="nameSmall">I'm Greg,</div>
          <div id="nameSmall">welcome to my site.</div>
          <div class="topButtonContainers">
            <a href="./static/Greg_Murray.pdf" target="_blank" class="btn btn-info topButton resumeButton">Resume</a>
            <a href="mailto:greg.murray20@gmail.com" class="btn btn-info topButton contactButton">Contact</a>
          </div>
      </div>
      <div class="mobilePic hidden-lg hidden-md hidden-sm">
        <div id="nameSmall">I'm Greg,</div>
          <div id="nameSmall">welcome to my site.</div>
          <div class="topButtonContainers">
            <a href="./static/Greg_Murray.pdf" target="_blank" class="btn btn-info topButton resumeButton">Resume</a>
            <a href="mailto:greg.murray20@gmail.com" class="btn btn-info topButton contactButton">Contact</a>
          </div>
      </div>
    </div>
  </div>

  <!-- WORK EXPERIENCE -->
  <a href="#work"></a>
  <div id="work"></div>
  <div class="background1">
    
    <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h1>A little about me</h1>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>

    <!-- my picture -->
    <div class="row">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <div id="about-image"></div>
      </div>
    </div>
'''

global topProject
topProject = '''
<a href="#projects"></a>
  <div id="projects"></div>
  <div class="background2">
    <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h1>My Projects</h1>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
'''

global topTravel
topTravel = '''
<a href="#travel"></a>
  <div id="travel"></div>
  <div class="background1">
    <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h1>Travel</h1>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
'''

global topContact
topContact = '''
</div>
          <div class="col-lg-1 col-md-1 hidden-sm hidden-xs"></div>
          </div>
        </div>
  </div>

  <!-- My contact -->
  <a href="#contact"></a>
  <div id="contact"></div>
  <div class="background2">
    <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h1>My Contact Info</h1>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
'''

global bottomOfPage
bottomOfPage = '''
<div class="row space">
      <div class="col-lg-3 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-6 col-md-6 col-sm-8 col-xs-12 photoContainer standardTextAlignCenter">
        <a href="./static/Greg_Murray.pdf" target="_blank"><img class="bottomImg" src="./static/images/resumeIcon.png"/></a>
        <a href="mailto:greg.murray20@gmail.com"> <img class="bottomImg" src="./static/images/emailIcon.svg"/></a>
        <a href="http://www.linkedin.com/in/gmurray20" target="_blank"><img class="bottomImg" src="./static/images/linkedInIcon.png"/></a>
      </div>
      <div class="col-lg-3 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
  </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.0.47/jquery.fancybox.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script src="./static/main.js"></script>
</body>
</html>
'''

def generateBioDescription(description):
  htmlContent = '''
  <div class="row">
      <div class="col-lg-3 col-md-4 col-sm-3 col-xs-1"></div>
      <div id="bioDescription" class="col-lg-6 col-md-4 col-sm-6 col-xs-10">
          %s
      </div>
      <div class="col-lg-3 col-md-4 col-sm-3 col-xs-1"></div>
    </div>

    <div class="row space"></div>
  ''' %(description)
  return htmlContent

def generateSectionHeader(title):
  htmlContent = '''
  <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h1>%s</h1>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
  '''%(title)
  return htmlContent

def generateArticle(link, imageUrl):
  htmlContent = '''
  <div class="row space standardTextAlignCenter">
      <a href="%s" target="_blank">
        <img class="articleLink hidden-xs" src="./static/images/%s" width=410px; height=310px;/>
        <img class="articleLink hidden-lg hidden-md hidden-sm" src="./static/images/%s" width=300px; height=225px;/>
      </a>
    </div>
    <div class="row space"></div>
  '''%(link, imageUrl, imageUrl)
  return htmlContent

def generateRightWork(link, imageUrl, title, position, location, description):
  htmlContent = '''
        <div class="row">
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
      <div class="col-lg-3 col-md-3 col-sm-4 col-xs-12">
        <a href="%s" target="_blank">
        <div class="aboutMe" style="background-image: url('./static/images/%s');"></div>
        </a>  
      </div>
      <div class="col-lg-5 col-md-5 col-sm-6 hidden-xs">
        <h3>%s</h3>
        <div id="subtitle">%s</div>
        <div id="location">%s</div>
          %s
      </div>
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
    </div>
    <div class="row space hidden-lg hidden-md hidden-sm"></div>
    <div class="row hidden-lg hidden-md hidden-sm">
      <div class="col-xs-1"></div>
      <div class="col-xs-10">
        <h3 class="standardTextAlignCenter">%s</h3>
        <div class="standardTextAlignCenter" id="subtitle">%s</div>
        <div class="standardTextAlignCenter" id="location">%s</div>
        <p>
          %s
        </p>
      </div>
      <div class="col-xs-1"></div>
    </div>
  ''' %(link, imageUrl, title, position, location, description, title, position, location, description)
  return htmlContent

def generateLeftWork(link, imageUrl, title, position, location, description):
  htmlContent = '''
    <div class="row">
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
      <div class="col-lg-5 col-md-5 col-sm-6 hidden-xs">
        <h3>%s</h3>
        <div id="subtitle">%s</div>
        <div id="location">%s</div>
          %s
      </div>
      <div class="col-lg-3 col-md-3 col-sm-4 col-xs-12">
        <div class="hidden-xs" style="float:left;">
          <a href="%s" target="_blank">
          <div class="aboutMe" style="background-image: url('./static/images/%s');"></div>
          </a>
        </div>
        <div class="hidden-lg hidden-md hidden-sm">
          <a href="%s" target="_blank">
          <div class="aboutMe" style="background-image: url('./static/images/%s');"></div>
          </a>
        </div>  
      </div>
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
    </div>
    <div class="row space hidden-lg hidden-md hidden-sm"></div>
    <div class="row hidden-lg hidden-md hidden-sm">
      <div class="col-xs-1"></div>
      <div class="col-xs-10">
        <h3  class="standardTextAlignCenter">%s</h3>
        <div class="standardTextAlignCenter" id="subtitle">%s</div>
        <div class="standardTextAlignCenter" id="location">%s</div>
        <p>
          %s
        </p>
      </div>
      <div class="col-xs-1"></div>
    </div>
  ''' %(title, position, location, description, link, imageUrl, link, imageUrl, title, position, location, description)
  return htmlContent

def generateTopTravel(description, youtubeLink):
  htmlContent = '''
  <div class="row">
      <div class="col-lg-3 col-md-3 col-sm-2 col-xs-1"></div>
      <div class="col-lg-6 col-md-6 col-sm-8 col-xs-10">
        <h3 id="travelDescription">
          %s
        </h3>
      </div>
      <div class="col-lg-3 col-md-3 col-sm-2 col-xs-1"></div>
    </div>
    <div class="row standardTextAlignCenter">
      <iframe class="hidden-xs" width="560" height="315" src="%s" frameborder="1" allowfullscreen></iframe>
      <iframe class="hidden-lg hidden-md hidden-sm" width="280" height="160" src="%s" frameborder="0" allowfullscreen></iframe>
    </div>
    <div class="row" style="text-align:center">
      <div id="location">Video credit to Jenna Smith</h2>
    </div>
    <div class="row">
      <div class="col-lg-1 col-md-1 hidden-sm hidden-xs"></div>
      <div class="col-lg-10 col-md-10 col-sm-12 col-xs-12 photoContainer">
  '''%(description, youtubeLink, youtubeLink)
  return htmlContent

def generateFancyImage(mainImage, smallImage, description):
  htmlContent = '''
  <div class="photo">
    <a href="./static/photoGallery/%s" data-fancybox="images" data-caption="%s" class="round">
        <img src="./static/photoGallery/%s" height="150px" width="150px" class="round"/>
    </a>
  </div>
  '''%(mainImage, description, smallImage)
  return htmlContent

def generateContactDescripion(description):
  htmlContent = '''
  <div class="row">
    <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
      <h2>%s</h2>
    </div>
    <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
  </div>
  <div class="row space"></div>
  '''%(description)
  return htmlContent

def generateBusinessCard():
  htmlContent = '''
  <div class="row">
    <div class="col-lg-2 col-md-2 col-sm-1 col-xs-0"></div>
    <div class="col-lg-8 col-md-8 col-sm-10 col-xs-12">
      <img src="./static/images/businessCard.png" class="hidden-xs" style="border-radius: 5px; max-width:100%;">
      <img src="./static/images/businessCardMobile.png" class="hidden-lg hidden-md hidden-sm" style="border-radius: 5px; max-width:100%;">
    </div>
    <div class="col-lg-2 col-md-2 col-sm-1 col-xs-0"></div>
  </div>
  '''
  return htmlContent
