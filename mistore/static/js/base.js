$(document).ready(function () {
    $(function () {
        $("#id_search").autocomplete({
            source: $("#id_search").parent().parent().parent().data("product-names"),
            select: function (event, ui) { //item selected
            }
        });
    });


    $(function () {
        var likeButtons = document.querySelectorAll(".ajaxlike");
        likeButtons.forEach(a => {
            var data = $(a).data();
        var button = $(a);
        $.ajax({url: data.url, method: 'get'}).done(function (data) {
            button.html("<i class=\"fa fa-thumbs-up\" aria-hidden=\"true\"></i> " + data);
        });
    });
    });


    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
            }
        }
    });

    $(document).on('click', 'button.ajaxlike', function () {
        var data = $(this).data();
        var button = $(this);
        $.ajax({url: data.url, method: 'post'}).done(function (data) {
            button.html("<i class=\"fa fa-thumbs-up\" aria-hidden=\"true\"></i> " + data);
        });

        return false;
    });

    $(document).on('click', 'button.ajaxOrderDeactivate', function () {
        console.log("dick")
        var data = $(this).data();
        var order = $(this).parent().parent();
        console.log(data);
        $.ajax({url: data.url, method: 'post'}).done(function (data) {
            if (data == "OK")
                order.hide();
        });

        return false;
    });
});