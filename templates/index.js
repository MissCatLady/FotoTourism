{% macro picture(imglink, imgid) -%}
	<li><a href='#{{ imgid }}' rel='modal:open'><img style='width:100%'; src='{{ imglink }}'></a></li><div class='modal' id='{{ imgid }}'><img style='width:100%'; src='{{ imglink }}'></div>
{%- endmacro %}

var count = 0;

$(document).ready(function() {

	$(".container").append("<ul>");
	{% if images %}
		{% for img in images%}
		count = count + 1;
			$(".container").append("{{ picture('http://instagram.com/p/' + img.imgtype + '/media/?size=l', img.imgtype) }}");
		{% endfor %}
	{% endif %}

//whitespace placeholder for now
	var white = 'http://www.scri8e.com/white.jpg';
	console.log(count)
	if (count%3==1) {
		$(".container").append("<li><img src=" + white +"></li>");
		count = count + 1;
	} 
	if (count%3==2) {
		$(".container").append("<li><img src=" + white +"></li>");
	}

	$(".container").append("</ul>")


});