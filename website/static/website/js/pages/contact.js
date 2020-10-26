document.addEventListener("DOMContentLoaded", function(event) {


    function listenSubmit() {
        document.querySelector("#contact-form").addEventListener("submit", (evt) => {
            evt.preventDefault()

            if(!validate()) {
                return
            }

            document.querySelector("#contact-form").submit()
        })
    }

    /**
     *   Validate form
     *   true -> no error
     *   array -> error messages
     *   By default, the function calls updateErrorMessage and updateErrorAnimation
     *   If showAnimation is false, updateErrorAnimation is not called
     *
     *   Return either true for no error
     *   either an array if there are errors
     *   [["errorMessage","element"],["errorMessage","element"],...]
     */
        function validate(showAnimation = true) {
        var returnValue = []
        if(document.querySelector("input[name=pseudo]").value == "")
            returnValue.push(["input[name=pseudo]", "Le pseudo est requis"])
        
        if(document.querySelector("textarea[name=message]").value == "")
            returnValue.push(["textarea[name=message]", "Le message est requis"])
        
        updateErrorMessage(returnValue)
        if(showAnimation) updateErrorAnimation(returnValue)
        if(returnValue.length == 0) return true
        return false
    }

    // Show error message if validation is false
    function updateErrorMessage(messages) {
        document.querySelector(".contact-validation").innerHTML = "<ul>"
        messages.forEach(message => {
            document.querySelector(".contact-validation").innerHTML += "<li>" + message[1] + "</li>"
        })
        document.querySelector(".contact-validation").innerHTML += "</ul>"
    }

    // Show error animation if validation is false
    function updateErrorAnimation(messages) {
        messages.forEach(message => {
            document.querySelector(message[0]).classList.add("input-failed")
            setTimeout(() => {
                document.querySelector(message[0]).classList.remove("input-failed")
            },1000)
        })
    }

    // Update error messages if input is changed
    function listenUpdateErrorMessages() {
        document.querySelector("input[name=pseudo]").oninput = () => {
            validate(false)
        }
        document.querySelector("textarea[name=message]").onchange = () => {
            validate(false)
        }
    }

    listenSubmit();
    listenUpdateErrorMessages();

})