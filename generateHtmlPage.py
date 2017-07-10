# Html_file= open("index1.html","w")

htmlContent = ''' <!DOCTYPE html>
<html lang=eng>

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width = device-width, initial-scale = 1">
  <title>Greg Murray</title>

  <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.0.47/jquery.fancybox.min.css" />
  <link rel="stylesheet" type="text/css" href="./static/styles.css">
  <link rel="icon" href="./icon.png">
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
      <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="background-color: #fff;">
      <span class="glyphicon glyphicon-align-justify" aria-hidden="true"></span>
      </button>
        <div class="dropdown-menu dropdown-menu-left" id="mobileDrop">
          <div class="dropdown-item" id="mobileAboutMe">My Work</div>
          <div class="dropdown-divider"></div>
          <div class="dropdown-item" id="mobileProjects">My Projects</div>
          <div class="dropdown-divider"></div>
          <div class="dropdown-item" id="mobileTravel">My Travel</div>
          <div class="dropdown-divider"></div>
          <div class="dropdown-item" id="mobileContact">Contact</div>
        </div>
    </div>
  </div>
  <!-- background picture -->
  <a href="#top"></a>
  <div class="row">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="topPic">
      <div class="picture">
        <div id="nameSmall">I'm Greg,</div>
          <div id="nameSmall">welcome to my site.</div>
          <div style="text-align:center; position:relative; top:42%;">
            <a href="./static/Greg_Murray.pdf" target="_blank" class="action-button shadow animate blue" style="color: #FFF; text-decoration: none;">Resume</a>
            <a href="mailto:greg.murray20@gmail.com" class="action-button shadow animate green" style="color: #FFF; text-decoration: none;">Contact</a>
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

def generateRightWork(link, imageUrl, title, position, location, description):
  htmlContent = '''
    <div class="row">
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
      <div class="col-lg-3 col-md-3 col-sm-4 col-xs-12">
        <a href="%s" target="_blank">
        <div class="aboutMe" style="background-image: url('%s');"></div>
        </a>  
      </div>
      <div class="col-lg-5 col-md-5 col-sm-6 hidden-xs">
        <h3>%s</h3>
        <div id="subtitle">%s</div>
        <div id="location">%s</div>
        <p>
          %s 
        </p>
      </div>
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
    </div>
    <div class="row space hidden-lg hidden-md hidden-sm"></div>
    <div class="row hidden-lg hidden-md hidden-sm">
      <div class="col-xs-1"></div>
      <div class="col-xs-10">
        <h3  style="text-align:center;">%s</h3>
        <div style="text-align:center;" id="subtitle">%s</div>
        <div style="text-align:center;" id="location">%s</div>
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
        <p>
          %s
        </p>
      </div>
      <div class="col-lg-3 col-md-3 col-sm-4 col-xs-12">
        <div class="hidden-xs" style="float:left;">
          <a href="%s" target="_blank">
          <div class="aboutMe" style="background-image: url('%s');"></div>
          </a>
        </div>
        <div class="hidden-lg hidden-md hidden-sm">
          <a href="%s" target="_blank">
          <div class="aboutMe" style="background-image: url('%s');"></div>
          </a>
        </div>  
      </div>
      <div class="col-lg-2 col-md-2 col-sm-1 hidden-xs"></div>
    </div>
    <div class="row space hidden-lg hidden-md hidden-sm"></div>
    <div class="row hidden-lg hidden-md hidden-sm">
      <div class="col-xs-1"></div>
      <div class="col-xs-10">
        <h3  style="text-align:center;">Echelon Consulting</h3>
        <div style="text-align:center;" id="subtitle">%s</div>
        <div style="text-align:center;" id="location">%s</div>
        <p>
          %s
        </p>
      </div>
      <div class="col-xs-1"></div>
    </div>
  ''' %(title, position, location, description, link, imageUrl, link, imageUrl, position, location, description)
  return htmlContent
