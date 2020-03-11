$(function() {
	var simplemde = new SimpleMDE({
		element: document.getElementById("comment-form"),
		autoDownloadFontAwesome:false,
		insertTexts: {
		horizontalRule: ["", "\n\n-----\n\n"],
		image: ["![Photo of Alt](http://", ")"],
		link: ["[Link description](http://", ")"],
		table: ["", "\n\n| Column 1 | Column 2 | Column 3 |\n| -------- | -------- | -------- |\n| Text     | Text      | Text     |\n\n"],
	    },
		toolbar: [{
			name: "bold",
			action: SimpleMDE.toggleBold,
			className: "fa fa-bold",
			title: "Bold",
			"default": !0
		}, {
			name: "italic",
			action: SimpleMDE.toggleItalic,
			className: "fa fa-italic",
			title: "Italic",
			"default": !0
		}, {
			name: "quote",
			action: SimpleMDE.toggleBlockquote,
			className: "fa fa-quote-left",
			title: "Quote",
			"default": !0
		}, {
			name: "code",
			action: SimpleMDE.toggleCodeBlock,
			className: "fa fa-code",
			title: "Code"
		}, {
			name: "link",
			action: SimpleMDE.drawLink,
			className: "fa fa-link",
			title: "Insert link",
			"default": !0
		}, {
			name: "image",
			action: SimpleMDE.drawImage,
			className: "fa fa-picture-o",
			title: "Insert picture",
			"default": !0
		}, {
			name: "table",
			action: SimpleMDE.drawTable,
			className: "fa fa-table",
            title: "Insert Table"
		}, {
			name: "preview",
			action: SimpleMDE.togglePreview,
			className: "fa fa-eye no-disable",
			title: "Preview",
			"default": !0
		}],
	});
	$(".editor-statusbar").append("<span class='float-left text-info ml-0 hidden' id='rep-to'></span>");
	$("#editor-footer").append("<button type='button' class='btn btn-danger btn-sm float-right mr-4 f-16 hidden' id='no-rep'>Cancel reply</button>");

	var emoji_tag = $("#emoji-list img");
	emoji_tag.click(function() {
		var e = $(this).data('emoji');
		simplemde.value(simplemde.value()+e);
	});

//    点击回复
	$(".rep-btn").click(function(){
	    simplemde.value('')
	    var u = $(this).data('repuser')
	    var i = $(this).data('repid')
	    sessionStorage.setItem('rep_id',i);
	    $("#rep-to").text("Reply @"+u).removeClass('hidden');
		$("#no-rep").removeClass('hidden');
		$(".rep-btn").css("color", "#868e96");
		$(this).css("color", "red");
		$('html, body').animate({
			scrollTop: $($.attr(this, 'href')).offset().top - 55
		}, 500);
	});

//    点击取消回复
	$("#no-rep").click(function(){
	    simplemde.value('')
	    sessionStorage.removeItem('rep_id');
	    $("#rep-to").text('').addClass('hidden');
		$("#no-rep").addClass('hidden');
		$(".rep-btn").css("color", "#868e96");
	});

//    点击提交评论
    $("#push-com").click(function() {
        var content = simplemde.value();
        if (content.length == 0) {
            alert("Comment content cannot be empty!");
            return;
        }
        var base_t = sessionStorage.getItem('base_t');
        var now_t = Date.parse(new Date());
        if (base_t) {
            var tt = now_t - base_t;
            if (tt < 40000) {
                alert('The time between two comments must be greater than 40 seconds.' + (40 - parseInt(tt/1000)) + 'second');
                return;
            } else {
                sessionStorage.setItem('base_t', now_t);
            }
        } else {
            sessionStorage.setItem('base_t', now_t)
        };
        var csrf = $(this).data('csrf');
        var article_id = $(this).data('article-id');
        var URL = $(this).data('ajax-url');
        var rep_id = sessionStorage.getItem('rep_id');
        $.ajaxSetup({
            data: {
                'csrfmiddlewaretoken': csrf
            }
        });
        $.ajax({
            type: 'post',
            url: URL,
            data: {
                'rep_id': rep_id,
                'content': content,
                'article_id': article_id
            },
            dataType: 'json',
            success: function(ret) {
                simplemde.value('')
                sessionStorage.removeItem('rep_id');
                sessionStorage.setItem('new_point', ret.new_point);
                window.location.reload();
            },
            error: function(ret) {
                alert(ret.msg);
            }
        });
    });

//    Navigate to new comment after submitting a comment
    if(sessionStorage.getItem('new_point')){
        var top = $(sessionStorage.getItem('new_point')).offset().top-100;
        $('body,html').animate({scrollTop:top}, 200);
        window.location.hash = sessionStorage.getItem('new_point');
        sessionStorage.removeItem('new_point');
    };
    sessionStorage.removeItem('rep_id');

    $(".comment-body a").attr("target","_blank");
})