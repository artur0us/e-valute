window.onload = function() {
	document.getElementById("regBtn").onclick = function() {
		doReg();
	}
}

function doReg() {
	var login = document.getElementById("user_login").value;
	var password = document.getElementById("user_pwd").value;
	var fullname = document.getElementById("user_names").value;
	var valute = document.getElementById("valute").value;
	$.ajax({
		type : 'POST',
		dataType : 'json',
		url  : '/doReg',
		data : 'login=' + login + '&pass=' + password + "&fullname=" + fullname + "&valute=" + valute,
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
}