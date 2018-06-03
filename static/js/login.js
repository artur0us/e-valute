window.onload = function() {
	document.getElementById("loginBtn").onclick = function() {
		doLogin();
	}
}

function doLogin() {
	var login = document.getElementById("user_login").value;
	var password = document.getElementById("user_pwd").value;
	$.ajax({
		type : 'POST',
		dataType : 'json',
		url  : 'localhost:666/checkLogin',
		data : 'login=' + login + '&pass=' + password,
		success: function(data){ 
			alert(data);
		},
		error: function (res, errorThrown) {
			if(res.responseText == "ok") {
				window.location.href = "/account?login=" + login + "&pass=" + password;
			} else {
				alert("Ошибка, проверьте правильность введённых данных!");
				window.location.href = "/login";
			}
		}
	});
}