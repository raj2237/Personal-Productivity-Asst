async function askAssistant(){
    let query = document.getElementById("query").value;
    let responsediv = document.getElementById("response");

    if(!query.trim()){
        responsediv.innerHTML = "<p>Please enter a question.</p>";
        return;
    }

    responsediv.innerHTML = "<p>Thinking...</p>";

    let response = await fetch("/query", {
        method: "POST",
        headers:  {"Content-Type":"application/json"},
        body : JSON.stringify({query: query})
    });

    let result = await response.json();
    responsediv.innerHTML = `<p>${result.response}<p>`

}