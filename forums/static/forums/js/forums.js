    $('a.post-edit').on('click', function (e) {
        e.preventDefault();

        var link = $(this);
        var post_id = link.attr('id').split('-')[2];
        var post_body = '#post-body-' + post_id;

        $.ajaxQueue({
            'url': link.attr('href'),
            'dataType': 'html',
            'success': function (html) {
                $(post_body).replaceWith(html);
            },
            'error': function () {
                alert('Unable to retrieve post form.');
            }
        });
    });
