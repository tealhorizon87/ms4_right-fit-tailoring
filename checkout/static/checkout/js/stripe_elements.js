/*
  Core logic/payment flow for this comes from here:
  https://stripe.com/docs/payments/accept-a-payment
  CSS from here:
  https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
  base: {
    color: '#000',
    fontFamily: '"Josefin Sans", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};

var card = elements.create("card", {style: style});
var errorDiv = document.getElementById('card-errors');
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
  if (event.error) {
    var html = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

// Handle Form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);
  $("#loading-overlay").show();

  var saveInfo = Boolean($("#id-save-info").attr("checked"));
  var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
  var postData = {
    "csrfmiddlewaretoken": csrfToken,
    "client_secret": clientSecret,
    "save_info": saveInfo,
  };
  var url = "/checkout/cache_checkout_data/";

  $.post(url, postData).done(function() {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.address_line_1.value),
            line2: $.trim(form.address_line_2.value),
            city: $.trim(form.city.value),
            state: $.trim(form.county.value),
            country: $.trim(form.country.value),
          }
        }
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.address_line_1.value),
          line2: $.trim(form.address_line_2.value),
          city: $.trim(form.city.value),
          state: $.trim(form.county.value),
          postal_code: $.trim(form.postcode.value),
          country: $.trim(form.country.value),
        }
      }
    }).then(function(result) {
      if (result.error) {
        var html = `
          <span class="icon" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
        $("#loading-overlay").hide();
      } else {
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function() {
    location.reload();
  });
});
