document.addEventListener("DOMContentLoaded", function(event) { 
    function checkBrowserNotSupported() {
        let support = new Konami(function () {addSupport()})
    }

    function addSupport() {
        alert("support ajouté !") // Maybe use something else than an alert(), like a popin for example
        document.querySelector("body").style.fontFamily = "'Comic Neue', cursive";
    }

    checkBrowserNotSupported()
});