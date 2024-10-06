//  slider 
const slider = document.getElementById("myRange");
const output = document.getElementById("sliderValue");

// แสดงค่าเริ่มต้น
output.innerHTML = slider.value;

// อัพเดตค่าเมื่อมีการเลื่อน slider
slider.oninput = function() {
output.innerHTML = this.value;
}

let createButton = document.getElementById("createButton");
let newProduct = document.getElementById("newProductPopup");
let overlay = document.getElementById("overlay");
let cancelButton = document.getElementById("cancelButton");

createButton.addEventListener("click", function(){
    newProduct.style.display = 'block';
    overlay.style.display = 'block';
})

cancelButton.addEventListener("click", function(){
    newProduct.style.display = 'none';
    overlay.style.display = 'none';
})