function auto_resize(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight)+"px";
	element.focus();
    element.select();
}