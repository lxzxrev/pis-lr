var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var postContainer = e.target.parentElement;
        if (postContainer.classList.contains("folded")) {
            postContainer.classList.remove("folded");
            e.target.innerHTML = "свернуть";
        } else {
            postContainer.classList.add("folded");
            e.target.innerHTML = "развернуть";
        }
    });
}