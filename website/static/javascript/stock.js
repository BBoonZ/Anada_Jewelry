document.querySelector('.button_sale_record').addEventListener('click', function() {
    window.location.href = '/recordsales/none';
});

document.querySelector('.dropdown_Stock_class').addEventListener('click', function() {
    window.location.href = 'stock.html';
});

// เพิ่มสินค้าใหม่ popup


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

document.getElementById('add-picture-button').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

// เมื่อมีการเลือกไฟล์ แสดงชื่อไฟล์ที่เลือกใน console
document.getElementById('fileInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        console.log('File selected: ' + file.name);
    } else {
        console.log('No file selected');
    }
});