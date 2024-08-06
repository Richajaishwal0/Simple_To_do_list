// document.addEventListener('DOMContentLoaded', additems())
const dataInput = document.getElementById('dataInput');
const dataList = document.getElementById('dataList');
const values = [];
function addItems(){
    const value = dataInput.value;
    if (value) {
        // Store the value in the list
        values.push(value);

        // Clear the input field
        dataInput.value = '';

        // Update the displayed list
        updateDataList();
    }
};

function updateDataList() {
    // Clear the current list
    dataList.innerHTML = '';

    // Add each value as a list item
    values.forEach((value, index) => {
        const listItem = document.createElement('li');
        listItem.textContent = `${index + 1}. ${value}`;
        dataList.appendChild(listItem);
    });
}
