function confirmDelete(event) {
  var message = 'Atención: Esto va a borrar todos los productos y Ordenes de Stock asociadas a el, está seguro que desea continuar?';
  if(!confirm(message)) {
    event.preventDefault()
  }
}

JsBarcode(".barcode").init();
