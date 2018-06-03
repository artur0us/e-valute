var reg = {
    doReg: function() {
        var login = document.getElementById("user_login").value;
        var password = document.getElementById("user_pwd").value;
        var fullname = document.getElementById("user_names").value;
        var email = document.getElementById("user_mail").value;
        var phone = document.getElementById("user_phone").value;
        $.ajax({
            type : 'POST',
            dataType : 'json',
            url  : '/doReg',
            data : 'login=' + login + '&pass=' + password + "&fullname=" + fullname + "&email=" + email + "&phone=" + phone,
            success: function(data){ 
                alert(data);
            },
            error: function (res, errorThrown) {
                if(res.responseText == "ok") {
                    alert("Вы успешно зарегистрированы!")
                    window.location.href = "/login";
                } else if(res.responseText == "user_err") {
                    alert("Данный логин занят, выберите другой.");
                    window.location.href = "/reg";
                } else {
                    alert("Ошибка в базе данных, извините.");
                    window.location.href = "/";
                }
            }
        });
    },
}

window.onload = function() {
    document.getElementById("regBtn").onclick = function() {
        reg.doReg();
    }
}