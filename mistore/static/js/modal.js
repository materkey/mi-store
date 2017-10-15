$(document).ready(function () {
    $(document).on('click', '.editReview', function (event) {
        if ($(event.target).hasClass('editReview')) {
            $('.modal').modal('show');
            $('.modal-title').html(this.dataset.modalTitle);
            $.get(this.dataset.href, function (data) {
                $('.modal-body').html(data);
            });
            event.preventDefault();
        }
    });

    $(document).on('submit', '[data-formtype="ajaxForm"]', function (event) {
        event.preventDefault();
        console.log("sucks 2.0");

        if ($(event.target).hasClass('deleteButton')) {
            setDeleteChecked(true);
            console.log("sucks");
        }
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            else $('.modal-body').html(data)
        });
        event.preventDefault();
    });

    function setDeleteChecked(checked) {
        var elm = $("div.deleteCheckbox input:checkbox");
        if (checked != elm.checked) {
            elm.click();
        }
    }
});