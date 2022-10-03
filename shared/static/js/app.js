
function showStockForm(event) {
  event.target.style.display = 'none';
  document
    .getElementById(`product_${event.target.value}_stock_form`)
    .style
    .display = 'initial';
}


function showButton(event) {
  document
    .getElementById(`product_${event.target.value}_stock_form`)
    .style
    .display = 'none'

  document
    .getElementById(`product_${event.target.value}_stock_button`)
    .style
    .display = 'initial';
}

function promptConfirmStock(event) {

}