document.querySelector('.button_sale_record').addEventListener('click', function() {
    window.location.href = 'sale_record.html';
});

document.querySelector('.dropdown_Stock_class').addEventListener('click', function() {
    window.location.href = 'stock.html';
});

// เพิ่มสินค้าใหม่ popup

//  slider 
const slider = document.getElementById("myRange");
const output = document.getElementById("sliderValue");

// แสดงค่าเริ่มต้น
output.innerHTML = slider.value;

// อัพเดตค่าเมื่อมีการเลื่อน slider
slider.oninput = function() {
output.innerHTML = this.value;
}
// slider

let newItem = document.getElementById("new_item");
let newProduct = document.getElementById("newProductPopup");
let overlay = document.getElementById("overlay");
let cancelButton = document.getElementById("cancelButton");

newItem.addEventListener("click", function(){
    newProduct.style.display = 'block';
    overlay.style.display = 'block';
})

cancelButton.addEventListener("click", function(){
    newProduct.style.display = 'none';
    overlay.style.display = 'none';
})