var running = false;
$("#upArrow").on('click', function(e) {
	if(running) {
		e.preventDefault();
		return;
	}
	running = true;
	var scrollTop = $(window).scrollTop() - 50;
	var top= 0;
	var work = $("#work").offset().top;
	var projects = $("#projects").offset().top;
	var travel = $("#travel").offset().top;
	var contact = $("#contact").offset().top;
	if(scrollTop < work) {
		scrolling(top);
	}
	else if(scrollTop < projects) {
		scrolling(work);
	}
	else if(scrollTop < travel) {
		scrolling(projects);
	}
	else {
		scrolling(travel);
	}
});

$("#downArrow").on('click', function(e) {
	if(running) {
		e.preventDefault();
		return;
	}
	running = true;
	var scrollTop = $(window).scrollTop() + 50;
	var work = $("#work").offset().top;
	var projects = $("#projects").offset().top;
	var travel = $("#travel").offset().top;
	var contact = $("#contact").offset().top;
	if(scrollTop < work) {
		scrolling(work);
	}
	else if(scrollTop < projects) {
		scrolling(projects);
	}
	else if(scrollTop < travel) {
		scrolling(travel);
	}
	else {
		scrolling(contact);
	}
});

$("#mobileAboutMe").on("click touchstart", function() {
	var work = $("#work").offset().top;
	scrolling(work);
});
$("#mobileProjects").on("click touchstart",function() {
	var work = $("#projects").offset().top;
	scrolling(work);
});
$("#mobileTravel").on("click touchstart",function() {
	var work = $("#travel").offset().top;
	scrolling(work);
});
$("#mobileContact").on("click touchstart",function() {
	var work = $("#contact").offset().top;
	scrolling(work);
});
function scrolling(top) {
    $('html, body').animate({
        scrollTop: top
	}, 800);

	setTimeout(function() {
		running = false;
	}, 800);
}

$(document).ready(function() {
	$(window).bind('resize', function() {
		if($(window).width() > 800 || Math.abs($(window).height()-$("#topPic").height()) > 100) {
			$("#topPic").height($(window).height());
		}
		
	});
	$("#topPic").height($(window).height());
	$("#mobileDrop").width($(window).width());
});

var isToggling = false;
$(document.body).on("click touchstart", function(event) {
	if($("#mobileDrop").is(":visible") && !isToggling) {
		isToggling = true;
		$("#mobileDrop").slideToggle( function() {
			isToggling = false;
		});

	}
});
$("#mobileNavButton").on("click", function(e) {
	isToggling = true;
	$("#mobileDrop").slideToggle(function() {
			isToggling = false;
		});
	e.stopPropagation();
});


//google analytics
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-104751062-1', 'auto');
  ga('send', 'pageview');


