document.addEventListener("DOMContentLoaded", function(event) { 
    function checkBrowserNotSupported() {

        var ua = window.navigator.userAgent;
        var msie = ua.indexOf("MSIE ");
    
        // If Internet Explorer, return version number
        if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./))  
        {
            // alert(parseInt(ua.substring(msie + 5, ua.indexOf(".", msie))));
            showBanner()
        }
        else  // If another browser, return 0
        {
            // alert('otherbrowser');
            showBanner()
        }
    
        return false;
    }

    function showBanner() {
        // Is it a great idea to have the html source in text format ?...
        document.querySelector("#scroller").appendChild(
            createElementFromHTML("" +
            "<div class=\"container\" style=\"position: sticky; bottom: 1rem;\">" +
            "<div class=\"alert alert-primary\" role=\"alert\">" +
            "Internet Explorer n'est pas supporté par le site web. Pour son bon fonctionnement, veuillez utiliser un navigateur plus respectable !" +
            "</div>" +
            "</div>"))
        let support = new Konami(() => {toggleSupport()})
    }

    // Reference : https://stackoverflow.com/questions/494143/creating-a-new-dom-element-from-an-html-string-using-built-in-dom-methods-or-pro
    function createElementFromHTML(htmlString) {
        var div = document.createElement('div')
        div.innerHTML = htmlString.trim()
        // Change this to div.childNodes to support multiple top-level nodes
        return div.firstChild; 
    }

    function toggleSupport() {
        addSupport()
    }

    function removeSupport() {

    }

    function addSupport() {
        alert("support ajouté !")
        document.querySelector("body").style.fontFamily = "'Comic Neue', cursive";
    }

    checkBrowserNotSupported()
});