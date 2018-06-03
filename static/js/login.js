var login = {
    doLogin: function() {
        var login = document.getElementById("user_login").value;
        var password = document.getElementById("user_pwd").value;
        $.ajax({
            type : 'POST',
            dataType : 'json',
            url  : '/checkLogin',
            data : 'login=' + login + '&pass=' + password,
            success: function(data){ 
                alert(data);
            },
            error: function (res, errorThrown) {
                if(res.responseText == "ok") {
                    window.location.href = "/account?login=" + login + "&pass=" + password + "&day=1";
                } else {
                    alert("Ошибка, проверьте правильность введённых данных!");
                    window.location.href = "/login";
                }
            }
        });
    },
}

window.onload = function() {
    document.getElementById("loginBtn").onclick = function() {
        login.doLogin();
    }
}