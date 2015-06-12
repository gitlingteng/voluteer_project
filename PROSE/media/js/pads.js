$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function OptionSort(a, b) {    
    return (a.innerHTML > b.innerHTML) ? 1 : -1;
};

$(document).ready(function(){
	window.setTimeout(loadMailNotifier, 1000);
});

function loadMailNotifier(){
	if ($('#mail-icon').length == 1){
		var retryTime = 60000;
		$.ajax({
			url: "/messages/messagecount/",
			type: 'post',
			dataType: 'json',
			success: function(data){
				var unread = data.all.sent;
				if (unread > 0){
					if (!($('#mail-notifier').length > 0)){
						$('body').prepend($('<span>').attr({'id':'mail-notifier', 'onclick':$('#mail-icon').attr('onclick')}).addClass('helper abs').html(unread).css({top: 0 , left: 0, display:'inline-block', cursor: 'pointer'}));
						$('#mail-notifier').position({
							'of': $('#mail-icon'),
							'my': 'left bottom',
							'at': 'center top',
							'offset': '-3 3',
							'collision': 'none none'
						});
					}else{
						$('#mail-notifier').html(unread);
					}
				}else{
					$('#mail-notifier').remove();
				}
				window.setTimeout(loadMailNotifier, retryTime);
			},
			error: function(){
			}
		});
	}
}

function makeMailDialog(msgType, url, buttonText, title, label, extraContent){
	var dialog = $("<div>").attr("title",title);
	dialog.append($('<label>').attr('for','mail-text').html('<h5>'+label+'</h5>'));
	dialog.append($("<textarea>").attr('id','mail-text').css('width','100%'));
	if(extraContent){
		dialog.append(extraContent);
	}
	dialog.dialog({
		autoOpen: true,
		modal: true,
		buttons: [
		    {
				id: "dialog-button",
				text: buttonText,
				click : function() {				
			    	if($('#mail-text').val() !=''){
			    		$.ajax({
				    		url: url,
				    		type: 'post',
				    		data: {'message-type': msgType, 'message': $('#mail-text').val()},
				    		dataType: 'html',
				    		success: function(data){
				    			dialog.remove();
				    		},
				    		error: function(){alert("There has been an error saving the message.");}
				    	});
			    	}else{
			    		dialog.find('label, textarea').effect("pulsate", { times:3 }, 500);
			    	}
				}
			}
		],
		close: function(event, ui){
			dialog.remove();
		}
	});
}
	