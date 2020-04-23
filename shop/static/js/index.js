//console.log("working");
//find the cart from lstorage
if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  updateCart(cart);
}

//if click in add to cart then increment the item
//$(".cart").click(function () {
//console.log("clicked");
$(".divpr").on("click", "button.cart", function () {
  var idstr = this.id.toString();
  //console.log(idstr);
  if (cart[idstr] != undefined) {
    qty = cart[idstr] + 1;
  } else {
    qty = 1;
    name = document.getElementById("name" + idstr).innerHTML;
    cart[idstr] = [qty, name];
  }
  updateCart(cart);
  //console.log(cart);
});

//add cart popover
$("#popcart").popover();
updatePopover(cart);
function updatePopover(cart) {
  console.log("update pop");
  var popStr = "";
  popStr = popStr + "<h5>Cart Info</h5><div class='mx-2 my-2'>";
  var i = 1;
  for (var item in cart) {
    popStr = popStr + "<b>" + i + "</b>";
    popStr =
      popStr +
      document.getElementById("name" + item).innerHTML.slice(0, 18) +
      "...Qty:" +
      cart[item][0] +
      "<br>";
    i = i + 1;
  }

  popStr =
    popStr +
    "</div><a href='/shop/checkout'><button class='btn btn-suceess rounded-pill shadow mt-5' id='checkout'>Checkout</button></a><button class='btn btn-danger rounded-pill shadow mt-5' onclick='clearCart' id='clearCart'>Remove cart</button>";
  console.log("popStr");
  document.getElementById("popcart").setAttribute("data-content", popStr);
  $("#popcart").popover("show");
}

function clearCart() {
  cart = JSON.parse(localStorage.getItem("cart"));
  for (var item in cart) {
    document.getElementById("div" + item).innerHTML =
      '<button id="' +
      item +
      '" class="btn-success rounded-pill cart"><i class="fa fa-shopping-cart text-warning"></i>Add To Cart</button>';
  }
  localStorage.clear();
  cart = {};
  updateCart(cart);
}
function updateCart(cart) {
  var sum = 0;
  for (var item in cart) {
    sum = sum + cart[item][0];
    document.getElementById("div" + item).innerHTML =
      "<button id='minus" +
      item +
      "' class='btn btn-warning rounded-pill shadow minus'>-</button> <span id='val" +
      item +
      "''>" +
      cart[item][0] +
      "</span> <button id='plus" +
      item +
      "' class='btn btn-primary rounded-pill shadow plus'> + </button>";
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML = sum;
  console.log(cart);
  updatePopover(cart);
}

// $("#popcart").popover();
// updatePopover();
// function updatePopover(cart) {
//   console.log("update pop");
//   var popStr = "";
//   popStr = popStr + "<h5>Popover Info</h5>";
//   var i = 1;
//   for (var item in cart) {
//     popStr = popStr + "<b>" + i + "</b>";
//     popStr =
//       popStr +
//       document.getElementById("name" + item) +
//       "Qty:" +
//       cart["item"] +
//       "<br>";
//     i = i + 1;
//   }
// }

//= plas minas button working trick
$(".divpr").on("click", "button.minus", function () {
  //console.log("minus mio");
  a = this.id.slice(7);
  //console.log(a);
  cart["pr" + a][0] = cart["pr" + a][0] - 1;
  cart["pr" + a][0] = Math.max(0, cart["pr" + a][0]);
  document.getElementById("valpr" + a).innerHTML = cart["pr" + a][0];
  updateCart(cart);
});

$(".divpr").on("click", "button.plus", function () {
  //console.log("plus clicked");
  a = this.id.slice(6);
  //console.log(a);
  cart["pr" + a][0] = cart["pr" + a][0] + 1;
  document.getElementById("valpr" + a).innerHTML = cart["pr" + a][0];
  updateCart(cart);
});
