function myFunction(event) {
    event.preventDefault();
    if(document.getElementById("search_bar").value.trim() === ""){
        swal("Error!", "Please enter a dish name", "error")
    } else {
        event.target.form.submit();
    }
}