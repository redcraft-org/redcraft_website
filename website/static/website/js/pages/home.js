document.addEventListener("DOMContentLoaded", function(event) { 


    let serverLinkAnimation = null;

    document.querySelector('.link-server').onclick = function() {
        clearTimeout(serverLinkAnimation);
        var copyText = document.getElementById("link-server-copy");
        copyText.select();
        copyText.setSelectionRange(0, 99999);
        document.execCommand("copy");
        // Animate "ip copied"
        document.querySelector('.before-click').classList.add("copied");
        document.querySelector('.ip-copied').classList.add("copied");

        serverLinkAnimation = setTimeout(function() {
            // Reset "ip copied"
            document.querySelector('.before-click').classList.remove("copied");
            document.querySelector('.ip-copied').classList.remove("copied");
        }, 5000);
    }

    // Call sal library
    sal({
        threshold: 0.5
    });

    function resizeServerDetails() {
        var arr = Array();
        document.querySelectorAll(".server-active").forEach(function(e, i) {
            arr[i] = e.clientHeight;
        });
        
        if(arr.length > 0 ) {    
            var max = arr.reduce(function (a, b) {
                return Math.max(a, b);
            });
            document.querySelector(".server-active-container").style.height = max + "px";
        }
    }
    resizeServerDetails();
    window.addEventListener('resize', resizeServerDetails);

})