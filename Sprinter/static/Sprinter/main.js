// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var create_btn = document.getElementById("create");

var update_btns = document.querySelectorAll(".edit");

update_btns.forEach((btn) => {
    btn.addEventListener("click", function () {
        modal.style.display = "block";
        document.getElementById("storyForm").action = "story/"+btn.dataset.story_id+"/update_story";
        document.getElementById('title').value = btn.dataset.title;
        document.getElementById('story').value = btn.dataset.story;
        document.getElementById('criteria').value = btn.dataset.criteria;
        document.getElementById('money').value = btn.dataset.business_value;
        document.getElementById('time').value = btn.dataset.estimation;
        document.getElementById("story_value").value = btn.dataset.business_value / btn.dataset.estimation;
        document.getElementById("submitBtn").innerHTML = "Update";
    });
});

[document.getElementById("money"), document.getElementById('time')].forEach((field) => {
    field.addEventListener('input', function () {
        document.getElementById("story_value").value = document.getElementById('money').value / document.getElementById('time').value
    });
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
create_btn.onclick = function () {
    modal.style.display = "block";
    document.getElementById("submitBtn").innerHTML = "Create";

}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    document.getElementById("storyForm").reset();
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        document.getElementById("storyForm").reset();
        modal.style.display = "none";
    }
}