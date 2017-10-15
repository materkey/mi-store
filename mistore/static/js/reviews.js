$(document).ready(function () {
    function updateComments() {
        $.get($('#pReviews').data('url-reviews'), function (data) {
            $(".updatingReviews").hide("slow", function () {
                $('#pReviews').replaceWith(data);
            });

        });
    };

    window.setTimeout(updateComments, 1000);
    window.setInterval(updateComments, 120000);

    $(document).on('click', '.updateReviews', function (event) {
        var urlReviews = $('#pReviews').data('url-reviews');
        $("#pReviews").hide("fast", function () {
            $(".updatingReviews").show("fast", function () {
                $.get(urlReviews, function (data) {
                    $(".updatingReviews").hide("slow", function () {
                        console.log(data);
                        $('#pReviews').replaceWith(data);
                    });

                });
            });
        });
        event.preventDefault();

    });
});