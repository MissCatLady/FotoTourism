{% macro info(imglink, fotoid, date, city, email, caption, ID) -%}
	<div class=section><div class='col span_1_of_2'><img style='width:100%'; src={{ imglink }}></div><div class='col span_1_of_2'><div class='right'><p><div class='info_label'>PhotoID: </div>{{ fotoid }}</p><p><div class='info_label'>Date: </div>{{ date }}</p><p><div class=info_label>City: </div>{{ city }}</p><p><div class='info_label'>Email: </div>{{ email }}</p><p><div class='info_label'>Caption: </div>{{ caption }}</p><a href='/submissions/deny/{{ID}}' class='button deny'>Deny</a><a href='/submissions/approve/{{ ID }}' class='button approve'>Approve</a></div>
{%- endmacro %}

$(document).ready(function() {
	/* get info from database */
	{% if submissions %} 
		{% for entry in submissions %} 
			{% if entry.imgtype %}
				$(".container").append("{{info('http://instagram.com/p/' + entry.imgtype + '/media/?size=l', entry.imgtype, entry.date, entry.city, entry.email, entry.caption, entry.fotoid)}}");
			{% else %}
/* after file addition duplicate code is changed */
				$(".container").append("{{info('http://instagram.com/p/' + entry.fotoid + '/media/?size=l', entry.fotoid, entry.date, entry.city, entry.email, entry.caption, entry.fotoid)}}");
			{% endif %}
		{% endfor %} 
	{% endif %} 

});
