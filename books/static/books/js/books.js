window.addEventListener('load', function() {
  maintainFilterSelection();
  bindBookOrderSelectChange();
});

function maintainFilterSelection () {
  // https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams

  // instantiate url search param object from provided query in url
  const params = new URLSearchParams(window.location.search);

  // if url order_by param is present
  if (params.has('order_by')){
    var selectElement = document.getElementById('books-order-by');

    // iterate through select options
    for (var i = selectElement.length - 1; i >= 0; i--) {

      // if current option value is the same as selected filter in url
      if (selectElement[i].value == params.get('order_by')){
        // set option as "selected" in current <select> element
        selectElement.value = params.get('order_by');
      }
    }
  }

}

function bindBookOrderSelectChange () {
  document.getElementById('books-order-by').addEventListener('change', event => {
    // Find selected option element
    var selectedOption = event.target[event.target.selectedIndex];

    // build url with selected filter
    const url = '/books?order_by=' + selectedOption.value;

    // Simulate redirect to books index action with selected filter
    window.location.replace(url);
  });

  return true;
}