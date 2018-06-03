var account = {
	load: function() {
		$.ajax({
			type : 'POST',     // тип запроса
			dataType : 'json', // тип загружаемых данных
			url  : '/getUserData',    // URL по которому должен обрабатываться запрос, см. @app.route('/ajax'...
			data : 'login=' + tools.getParam("login"),
			success: function(data){
				console.log("Result: " + data)
				document.getElementById("account_id").innerHTML = "Межбанковский счёт №" + data[4].toString();
				document.getElementById("user_login").innerHTML = data[0];
				document.getElementById("allmoney_count").value = data[1];
				document.getElementById("expiration_date").value = data[3];
				document.getElementById("current_val").value = data[2];
			},
			error: function (res, errorThrown) {
				alert("Упс, что-то пошло не так... Возможно, сейчас проходят технические работы, просим Вас немного подождать.");
				window.location.href = "/";
			}
		});
	},
	open_account: function() {
		document.getElementById("hello_block").style.display = "none";
		document.getElementById("myaccount_block").style.display = "block";
		this.load();
	},
	giveMeMoney: function() {
		$.ajax({
			type : 'POST',     // тип запроса
			dataType : 'json', // тип загружаемых данных
			url  : '/sendMoney',    // URL по которому должен обрабатываться запрос, см. @app.route('/ajax'...
			data : 'login=' + tools.getParam("login"),
			success: function(data){
				if(data == "ok") {
					alert("Получено 150,00 единиц на счёт");
					window.location.href = window.location.href;
				} else {
					alert("Ошибка.");
					window.location.href = window.location.href;
				}
			},
			error: function (res, errorThrown) {
				console.log(res.responseText);
				if(res.responseText == "ok") {
					alert("Получено 150,00 единиц на счёт");
					window.location.href = window.location.href;
				} else {
					alert("Упс, что-то пошло не так... Возможно, сейчас проходят технические работы, просим Вас немного подождать.");
					window.location.href = "/";
				}
			}
		});
	},
	changeValute: function(convertingVal) {
		$.ajax({
			type : 'POST',     // тип запроса
			dataType : 'json', // тип загружаемых данных
			url  : '/changeValute',    // URL по которому должен обрабатываться запрос, см. @app.route('/ajax'...
			data : 'login=' + tools.getParam("login"),
			success: function(data){
				if(data == "ok") {
					alert("Ваши средства были сконвертированы " + convertingVal);
					window.location.href = window.location.href;
				} else {
					alert("Ошибка.");
					window.location.href = window.location.href;
				}
			},
			error: function (res, errorThrown) {
				if(res.responseText == "ok") {
					alert("Ваши средства были только что сконвертированы " + convertingVal);
					window.location.href = window.location.href;
				} else {
					alert("Упс, что-то пошло не так... Возможно, сейчас проходят технические работы, просим Вас немного подождать.");
					window.location.href = "/";
				}
			}
		});
	},
}

window.onload = function() {
	document.getElementById("open_myaccount_block_btn").onclick = function() {
		account.open_account();
	}
	document.getElementById("giveMeMoney").onclick = function() {
		account.giveMeMoney();
	}
	document.getElementById("change_valute").onclick = function() {
		if(document.getElementById("current_val").value == "USD") {
			account.changeValute("из USD в RUB");
		} else {
			account.changeValute("из RUB в USD");
		}
	}
}