document.addEventListener("DOMContentLoaded", function(event) {

    /*********************************[ PAGES NAVIGATION ]************************************/

    /**
     * Detect when the "next" or "previous" buttons are pressed on the form
     * Updates the page page depending on the results from the select input
     */
    function listenCloseModal() {
        document.querySelector("#form-next-page").onclick = function() {
            document.querySelector(".transition-element.contact-from").classList.remove('active')
            document.querySelector(".transition-element.contact-details").classList.add('active')
            
            if(document.getElementsByName("client_type")[0].value == "player") {
                document.querySelector(".row.inputs-player").style.display = "flex"
                document.querySelector(".row.inputs-other").style.display = "none"
            }else if(document.getElementsByName("client_type")[0].value == "other") {
                document.querySelector(".row.inputs-player").style.display = "none"
                document.querySelector(".row.inputs-other").style.display = "flex"
            }
        }

        document.querySelector("#form-previous-page").onclick = function() {
            document.querySelector(".transition-element.contact-from").classList.add('active')
            document.querySelector(".transition-element.contact-details").classList.remove('active')
            document.querySelector(".contact-validation").innerHTML = ""
        }
    }

    function listenRestartModal() {
        document.querySelector("#form-restart").onclick = function() {
            document.querySelector(".transition-element.contact-failed").classList.remove("active")
            document.querySelector(".transition-element.contact-details").classList.add("active")
            document.querySelector(".contact-validation").innerHTML = ""
        }
    }

    listenRestartModal()
    listenCloseModal()

    /*********************************[ FORM VALIDATION ]************************************/

    /**
     * handler when the form is sent. Calls the validate function, set the final price in the "sum" element
     * and submits the form
     */
    function listenSubmit() {
        document.querySelector("#contact-form").addEventListener("submit", function(evt) {
            evt.preventDefault()

            if(!validate()) {
                return
            }

            sendRequest(evt.target)
            // document.querySelector("#contact-form").submit()
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

        if(document.getElementsByName("client_type")[0].value == "player") {

            // Nickname
            const pseudo = document.querySelector("input[name=pseudo]").value
            if(pseudo == "")
                returnValue.push(["input[name=pseudo]", "Le pseudo Minecraft est requis"])
            else if(pseudo.length < 4)
                returnValue.push(["input[name=pseudo]", "Le pseudo Minecraft est trop court"])
            else if(pseudo.match("^[a-zA-Z0-9_]*$") == null)
                returnValue.push(["input[name=pseudo]", "Le pseudo Minecraft contient des charactères invalides"])

            // Discord username
            const discord_username = document.querySelector("input[name=discord_username]").value
            if(!(discord_username === "") && discord_username.match("^.{3,32}#[0-9]{4}$") == null)
                returnValue.push(["input[name=discord_username]", "Le pseudo Discord ne respecte pas le format abc#0000"])

        }else if(document.getElementsByName("client_type")[0].value == "other") {

            // Email
            if(document.querySelector("input[name=email]").value == "")
                returnValue.push(["input[name=email]", "L'email est requis"])
        }

        // Message
        const message = document.querySelector("textarea[name=message]").value
        if(message == "")
            returnValue.push(["textarea[name=message]", "Le message est requis"])
        else if(message.length < 30)
        returnValue.push(["textarea[name=message]", "Le message est trop court"])
        
        updateErrorMessage(returnValue)
        if(showAnimation) updateErrorAnimation(returnValue)
        
        if(returnValue.length == 0) return true
        return false
    }

    /**
     * Show error messages in span. Recieves the array from the validate function
     */
    function updateErrorMessage(messages) {
        document.querySelector(".contact-validation").innerHTML = "<ul>"
        messages.forEach(message => {
            document.querySelector(".contact-validation").innerHTML += "<li>" + message[1] + "</li>"
        })
        document.querySelector(".contact-validation").innerHTML += "</ul>"
    }

    /**
     * Shows error animation on input fields who are not valid
     * Recieves the array from the validate function
     */
    function updateErrorAnimation(messages) {
        messages.forEach(message => {
            document.querySelector(message[0]).classList.add("input-failed")
            setTimeout(() => {
                document.querySelector(message[0]).classList.remove("input-failed")
            },1000)
        })
    }

    /**
     * Update the error messages if the inputs are changed
     */
    function listenUpdateErrorMessages() {
        document.querySelector("input[name=pseudo]").oninput = function() {
            validate(false)
        }
        document.querySelector("input[name=discord_username]").oninput = function() {
            validate(false)
        }
        document.querySelector("textarea[name=message]").oninput = function() {
            validate(false)
        }
    }

    listenSubmit()
    listenUpdateErrorMessages()

    /*********************************[ SENDING FORM ]************************************/
    var httpRequest;

    function sendRequest(form) {
        httpRequest = new XMLHttpRequest();
        if (!httpRequest)
            return false

        httpRequest.onreadystatechange = alertContents;
        httpRequest.open("POST", form.action)
        httpRequest.send(new FormData(form))
    }

    function alertContents() {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                // A switch is used here if more options are added in the future
                switch(JSON.parse(httpRequest.response).response) {
                    case 0:
                        requestSuccess()
                        break
                    default:
                        requestError(JSON.parse(httpRequest.response).error)
                }
            } else {
                requestError()
            }
            restartIconAnimation()
        }
    }

    /*********************************[ FORM RESPONSE ]************************************/

    function restartIconAnimation() {
        document.querySelector(".transition-element.active .checkmark").classList.remove("checkmark-animation")
        // setTimeout necessary in order to replay the css animation
        setTimeout(function() {
            document.querySelector(".transition-element.active .checkmark").classList.add("checkmark-animation")
        }, 0)
    }

    function requestSuccess(state) {
        document.querySelector(".transition-element.contact-details").classList.remove("active")
        document.querySelector(".transition-element.contact-success").classList.add("active")
    }

    function requestError(error) {
        document.querySelector("#contact-failed-error").innerText = error
        document.querySelector(".transition-element.contact-details").classList.remove("active")
        document.querySelector(".transition-element.contact-failed").classList.add("active")
    }
})