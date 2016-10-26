document.getElementById("submit").onclick = function(e) {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    console.log('grant_type=password&username='
           + username + '&password='
           + password
           + '&client_id=K3mguv60CF2T8Oq7icUff2PQLLKjNDUrgvEUuQpx')
    fetch("/o/token/", {
        method: 'POST',
        headers: {'Content-type': 'application/x-www-form-urlencoded'},
        body: 'grant_type=password&username='
               + username + '&password='
               + password
               + '&client_id=K3mguv60CF2T8Oq7icUff2PQLLKjNDUrgvEUuQpx'
    }).then(function(response) {
        console.log(response);
        if (response.ok) {
            response.json().then(function(data) {
                console.log(data);
                localStorage.setItem("access_token", data["access_token"]);
                setCookie("access_token", data["access_token"], {'domain': 'dd.com'});
                setCookie("token_type", data["token_type"]);
                console.log(getCookie("access_token"));
            });
        } else {
            alert("BAD");
        }
    })
}
