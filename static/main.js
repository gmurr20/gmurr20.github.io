$("#upArrow").click(function() {
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

$("#downArrow").click(function() {
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

$("#mobileAboutMe").click(function() {
	var work = $("#work").offset().top;
	scrolling(work);
});
$("#mobileProjects").click(function() {
	var work = $("#projects").offset().top;
	scrolling(work);
});
$("#mobileTravel").click(function() {
	var work = $("#travel").offset().top;
	scrolling(work);
});
$("#mobileContact").click(function() {
	var work = $("#contact").offset().top;
	scrolling(work);
});
function scrolling(top) {
    $('html, body').animate({
        scrollTop: top
	}, 800);
}

function set_body_height() {
    $("#topPic").height($(window).height());
  }
$(document).ready(function() {
	$(window).bind('resize', set_body_height);
	set_body_height();
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


