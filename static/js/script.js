function validate_form(e) {
    var form = e.target;
    var data = $('#signupform').serialize();
    var error = $('#signupform').find('.error')
    $.ajax({
        url: '/user/signup',
        type: 'POST',
        data: data,
        dataType: "json",
        success: (resp) => {
            window.location.href = '/dashboard/'
        },
        error: (resp) => {
            console.log(resp);
            error.text(resp.responseJSON.error).removeClass('error--hidden');
        }
    })
    e.preventDefault();
}

function login(e) {
    var form = e.target;
    var data = $('#login_form').serialize();
    var error = $('#login_form').find('.error')
    $.ajax({
        url: '/user/login',
        type: 'POST',
        data: data,
        dataType: "json",
        success: (resp) => {
            window.location.href = '/dashboard/'
        },
        error: (resp) => {
            console.log(resp);
            error.text(resp.responseJSON.error).removeClass('error--hidden');
        }
    })
    e.preventDefault();
}