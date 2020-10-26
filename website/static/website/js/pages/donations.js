document.addEventListener("DOMContentLoaded", function(event) { 
    
    /**
     * Enables or disables inputs fields depending on checkboxes
     */
    function listenFormInputs()  {
        document.querySelectorAll('input[name=sum_radio]').forEach(() => {
            this.onchange = () => {
                document.querySelector('#donation-custom-price').disabled = !document.querySelector('#donation-price-4').checked
            }
        })

        document.querySelector('#donation-is-anonymous').onclick = () => {
            document.querySelector('#donation-nickname').disabled = document.querySelector('#donation-is-anonymous').checked
            document.querySelector('#donation-nickname').value = ""
        }

        document.querySelector('#donation-is-gift').onclick = () => {
            document.querySelector('#donation-gift-nickname').disabled = !document.querySelector('#donation-is-gift').checked
            document.querySelector('#donation-gift-nickname').value = ""
        }
    }
    
    /**
     * Set form inputs with the values from the localStorage
     */
    function getLocalStorage() {
        if(localStorage.getItem("sum_radio")) {
            document.querySelector("input[name=sum_radio][value=\"" + localStorage.getItem("sum_radio") + "\"]").checked = true
        }
        if(localStorage.getItem("sum_radio") == "custom") {
            document.querySelector("input[name=sum_custom]").value = localStorage.getItem("sum_custom")
        }
        if(localStorage.getItem("is_anonymous") == "true") {
            document.querySelector("input[name=is_anonymous]").checked = true
            document.querySelector('input[name=pseudo]').disabled = true
        }else{
            document.querySelector("input[name=pseudo]").value = localStorage.getItem("pseudo")
        }
        if(localStorage.getItem("is_gift") == "true") {
            document.querySelector("input[name=is_gift]").checked = true
            document.querySelector('input[name=reciever]').disabled = false
            document.querySelector("input[name=reciever]").value = localStorage.getItem("reciever")
        }
        document.querySelector("textarea[name=message]").value = localStorage.getItem("message")
        document.querySelector("input[name=bonus_code]").value = localStorage.getItem("bonus_code")
    }

    /**
     * Delete localStorage & reset form
     */
    function clearLocalStorage() {
        if("{{ status }}" == "success") {
            localStorage.clear()
            document.querySelector("input[name=sum_radio][value=\"8\"]").checked = true
            document.querySelector("input[name=sum_custom]").value = ""
            document.querySelector("input[name=is_anonymous]").checked = false
            document.querySelector('input[name=pseudo]').disabled = false
            document.querySelector('input[name=pseudo]').value = ""
            document.querySelector("input[name=is_gift]").checked = false
            document.querySelector('input[name=reciever]').disabled = true
            document.querySelector("input[name=reciever]").value = ""
            document.querySelector("textarea[name=message]").value = ""
            document.querySelector("input[name=bonus_code]").value = ""
        }
    }

    /**
     * handler when the form is sent. Calls the validate function, set the final price in the "sum" element
     * and submits the form
     */
    function listenSubmit() {
        document.querySelector("#donation-form").addEventListener("submit", (evt) => {
            evt.preventDefault()

            if(!validate()) {
                return
            }
        
            if(document.querySelector("input[name=sum_radio]:checked").value == "custom") {
                document.querySelector("#donation-final-price").value = document.querySelector("input[name=sum_custom]").value
            }else {
                document.querySelector("#donation-final-price").value = document.querySelector("input[name=sum_radio]:checked").value
            }
        
            localStorage.setItem("sum_radio", document.querySelector("input[name=sum_radio]:checked").value)
            localStorage.setItem("sum_custom", document.querySelector("input[name=sum_custom]").value)
            localStorage.setItem("is_anonymous", document.querySelector("input[name=is_anonymous]").checked)
            localStorage.setItem("pseudo", document.querySelector("input[name=pseudo]").value)
            localStorage.setItem("is_gift", document.querySelector("input[name=is_gift]").checked)
            localStorage.setItem("reciever", document.querySelector("input[name=reciever]").value)
            localStorage.setItem("message", document.querySelector("textarea[name=message]").value)
            localStorage.setItem("bonus_code", document.querySelector("input[name=bonus_code]").value)
        
            console.log("form sent")
            document.querySelector("#donation-form").submit()
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
        if(document.querySelector("input[name=sum_radio]:checked").value == "custom" && document.querySelector("input[name=sum_custom]").value == "")
            returnValue.push(["label[for=donation-price-4]", "Le montant doit être indiqué"])
        
        if(!document.querySelector("input[name=is_anonymous]").checked && document.querySelector("input[name=pseudo]").value == "")
            returnValue.push(["input[name=pseudo]", "Le pseudo est requis"])
        
        if(document.querySelector("input[name=is_gift]").checked && document.querySelector("input[name=reciever]").value == "")
            returnValue.push(["input[name=reciever]", "Le pseudo du bénéficiaire est requis"])

        updateErrorMessage(returnValue)
        if(showAnimation) updateErrorAnimation(returnValue)
        if(returnValue.length == 0) return true
        return false
    }

    /**
     * Show error messages in span. Recieves the array from the validate function
     */
    function updateErrorMessage(messages) {
        document.querySelector(".donation-validation").innerHTML = "<ul>"
        messages.forEach(message => {
            document.querySelector(".donation-validation").innerHTML += "<li>" + message[1] + "</li>"
        })
        document.querySelector(".donation-validation").innerHTML += "</ul>"
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
        document.querySelector("input[name=pseudo]").oninput = () => {
            validate(false)
        }
        document.querySelector("input[name=is_anonymous]").onchange = () => {
            validate(false)
        }
        document.querySelector("input[name=reciever]").oninput = () => {
            validate(false)
        }
        document.querySelector("input[name=is_gift]").onchange = () => {
            validate(false)
        }
        document.querySelector("input[name=sum_custom]").onchange = () => {
            validate(false)
        }
    }

    /**
     * Close the success / fail modal and shows the form
     */
    function listenCloseModal() {
        document.querySelectorAll('.donation-terminated').forEach(button => {
            button.onclick = () => {
                document.querySelector('.transition-container .donation-fill').classList.add("active")
                document.querySelectorAll('.transition-container .donation-modal').forEach(modal => {
                    modal.classList.remove("active")
                })
            }
        })
    }

    listenFormInputs()
    getLocalStorage()
    clearLocalStorage()
    listenSubmit()
    listenUpdateErrorMessages()
    listenCloseModal()

});
