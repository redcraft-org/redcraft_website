document.addEventListener("DOMContentLoaded", function(event) { 
    function checkBrowserNotSupported() {
        let support = new Mooncake(function () {addSupport()});
    }

    function addSupport() {
        alert("Done");
        document.querySelector("body").style.fontFamily = "'Comic Neue', cursive";
    }

    checkBrowserNotSupported();
})