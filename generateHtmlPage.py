def generateBioDescription(description):
  htmlContent = '''
  <div class="row">
      <div class="col-lg-4 col-md-4 col-sm-3 col-xs-1"></div>
      <div id="bioDescription" class="col-lg-6 col-md-4 col-sm-6 col-xs-10">
        <p>
          %s
        </p>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-3 col-xs-1"></div>
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
        <p>
          %s
        </p>
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
  '''%(description, youtubeLink, youtubeLink)

def generateFancyImage(mainImage, smallImage, description):
  htmlContent = '''
  <div class="photo">
    <a href="./static/photoGallery/%s" data-fancybox="images" data-caption="%s">
        <img src="./static/photoGallery/%s" height="150px" width="150px"/>
    </a>
  </div>
  '''%(mainImage, description, smallImage)

def generateContactDescripion(description):
  htmlContent = '''
  <div class="row">
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
      <div class="col-lg-4 col-md-6 col-sm-8 col-xs-12">
        <h2>%s</h2>
      </div>
      <div class="col-lg-4 col-md-3 col-sm-2 col-xs-0"></div>
    </div>
  <div class="row space">
  '''%(description)
  return htmlContent
