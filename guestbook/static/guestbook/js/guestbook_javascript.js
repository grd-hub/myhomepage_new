"use strict";
/* --- START jQuery / UI --- */
$(":radio").checkboxradio();
$("#filter_button").button();
/* --- END jQuery / UI ---*/


/* --- START collapsible JS --- */
const coll = document.getElementsByClassName("collapsible");
for (let i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    let content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
/* --- END collapsible JS --- */


/* --- START TOGGLE MENU --- */
$("#toggle_menu_btn").click(function(){
    $(".main_menu").toggle();
});
/* --- END TOGGLE MENU --- */