/**
 * Created by daniil on 05.03.17.
 */
$(document).ready(function () {
        $("#btn-signup").click(function () {
            $('#signup').modal('show');
        });
    });

$(document).ready(function () {
        $("#btn-login").click(function () {
            $('#login').modal('show');
        });
    });


window.onload = function () {
    document.getElementById("password").onchange = validatePassword;
    document.getElementById("password_confirmation").onchange = validatePassword;
}
function validatePassword(){
var pass2=document.getElementById("password_confirmation").value;
var pass1=document.getElementById("password").value;
if(pass1 != pass2)
    document.getElementById("password_confirmation").setCustomValidity("Пароли не совпадают");
else
    document.getElementById("password").setCustomValidity(''); // пустая строка означает отсутствие ошибок
}


