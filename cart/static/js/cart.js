$(document).ready(function () {
    // Initialize bag total variable outside of the function
    let bagTotal = 0;

    // Function to update bag total and grand total
    function updateTotals() {
        // Reset bag total to zero before recalculating
        bagTotal = 0;

        $('.input-group').each(function () {
            let itemId = $(this).find('input[type="number"]').attr('id'); // Get item ID
            if (itemId) {
                itemId = itemId.toString(); // Convert itemId to string
                const itemKeyParts = itemId.split('_');
                const productId = itemKeyParts[1]; // Extract product ID from itemId
                const sizeId = itemKeyParts[2]; // Extract size ID from itemId (if applicable)
                const quantity = parseInt($(this).find('input[type="number"]').val(), 10);
                const productPriceText = $('#price_' + productId + (sizeId ? '_' + sizeId : '')).text().replace('£', ''); // Construct correct selector for product price
                const productPrice = parseFloat(productPriceText);
                const subtotal = productPrice * quantity;

                // Update subtotal in HTML
                const subtotalElement = $('#subtotal_' + itemId); // Updated here
                if (subtotalElement.length > 0) {
                    subtotalElement.text('£' + subtotal.toFixed(2));
                } else {
                    console.error('Subtotal element not found for item ID:', itemId);
                }

                bagTotal += subtotal;
            } else {
                console.error('Item ID not found for input-group:', $(this));
            }
        });

        // Update bag total in HTML
        $('#bag-total').text('£' + bagTotal.toFixed(2));

        // Update grand total
        const delivery = 3.99; // Assuming delivery cost is fixed
        const grandTotal = bagTotal + delivery;

        // Update grand total in HTML
        $('#grand-total').text('£' + grandTotal.toFixed(2));
    }

    // Function to handle quantity adjustment
    $('.btn-quantity').click(function () {
        const action = $(this).data('action');
        const itemId = $(this).data('item-id');
        const quantityField = $(this).closest('.input-group').find('input[type="number"]');
        const currentQuantity = parseInt(quantityField.val(), 10);

        if (action === 'increase') {
            quantityField.val(currentQuantity + 1);
        } else if (action === 'decrease' && currentQuantity > 1) {
            quantityField.val(currentQuantity - 1);
        }

        updateTotals();
    });

    // Call updateTotals initially
    updateTotals();
});
