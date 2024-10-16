

// Get the select element by its ID
const selectElement = document.getElementById("product-type");

// ตั้งค่า default ของประเภทสินค้า
const selectedProduct = selectElement.getAttribute("data-selected-product");

// Set the value of the select element based on the data attribute
selectElement.value = selectedProduct;

console.log("Selected product:", selectedProduct);

// เพิ่มลดจำนวน
function decrement() {
    var input = document.getElementById('quantity');
    var value = parseInt(input.value);
    if (value > 1) {
        input.value = value - 1;
    }
}

function increment() {
    var input = document.getElementById('quantity');
    var value = parseInt(input.value);
    input.value = value + 1;
}

function closePopup() {
    window.parent.closePopup();
}

// ปิดหน้าต่าง edit popup
function closeEdit() {
    closePopup();
    window.parent.location.reload();
}

// เปิดหน้าเลือกไฟล์ของ edit popup
document.getElementById('change-picture-button').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const imagePreview = document.getElementById('imagePreview');
            imagePreview.src = e.target.result; // Update the image src to the new image
        };

        reader.readAsDataURL(file);
    }
});