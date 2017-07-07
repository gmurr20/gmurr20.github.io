$("#navBar").click(function() {
	var links = ['top', 'aboutMe', 'project', 'travel', 'contact'];
	var scrollTop = $(window).scrollTop();
	console.log(scrollTop);

	// 0-620 top section
	//620-1900
	//1900-2700
});

function set_body_height() { // set body height = window height
    $("#topPic").height($(window).height());
  }
  $(document).ready(function() {
    $(window).bind('resize', set_body_height);
    set_body_height();
  });