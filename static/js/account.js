var account = {
    load: function() {
        this.getEID();
        this.myMoney();
        //this.parseDays(tools.getParam("day"));
        switch(tools.getParam("day")) {
            case "1": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64.7644";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 1.00000";
                break;
            };
            case "2": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64,8306";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99978";
                break;
            };
            case "3": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64,3804";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99983";
                break;
            };
            case "4": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 63,973";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99954";
                break;
            };
            case "5": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64,1617";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99955";
                break;
            };
            case "6": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 65,0539";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99912";
                break;
            };
            case "7": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64,8102";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99911";
                break;
            };
            case "8": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64,9737";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99934";
                break;
            };
            case "9": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 65,217";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD: 0.99902";
                break;
            };
            case "10": {
                document.getElementById("curr_day").innerHTML = "День: " + tools.getParam("day");
                document.getElementById("rate_dr").innerHTML = "Курс USD к RUB: 64.9940";
                document.getElementById("rate_eu").innerHTML = "Курс EL к USD:  0.99924";
                break;
            };
            case "11": {
                alert("Недоступно!");
                window.location.href = "/";
                break;
            };
            default: { alert("Недоступно!"); window.location.href = "/"; break; };
        }
    },
    myMoney: function() {
        $.ajax({
            type : 'POST',
            dataType : 'json',
            url  : '/myMoney',
            data : 'login=' + tools.getParam("login"),
            success: function(data){
                if(data != "err") document.getElementById("myaccount").innerHTML = "Счёт: " + data + " EL(EvaLute)";
            },
            error: function (res, errorThrown) {
                alert("error: " + res.responseText);
            }
        });
    },
    parseDays: function(day) {
        $.ajax({
            type : 'POST',
            dataType : 'json',
            url  : '/parseMyDays',
            data : 'day=' + day,
            success: function(data){
                if(data != "err") document.getElementById("curr_day").innerHTML = "День: " + data;
            },
            error: function (res, errorThrown) {
                if(res.responseText == "ok") {
                    document.getElementById("curr_day").innerHTML = "День: " + day;
                }
            }
        });
    },
    getEID: function() {
        //EvaluteID
        $.ajax({
            type : 'POST',
            dataType : 'json',
            url  : '/getEID',
            data : 'login=' + tools.getParam("login"),
            success: function(data){
                if(data != "err") document.getElementById("evakey").innerHTML = "Ваш Evakey — №A0F" + data;
            },
            error: function (res, errorThrown) {
                alert("error: " + res.responseText);
            }
        });
    },
}

window.onload = function() {
    account.load();
    
    document.getElementById("go_next").onclick = function() {
        var current_day = tools.getParam("day");
        window.location.href = "/account?login=scaleflake&pass=qwerty&day=" + (parseInt(tools.getParam("day")) + 1).toString();
    }
}