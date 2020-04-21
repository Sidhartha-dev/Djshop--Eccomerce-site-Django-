//console.log("working");
//find the cart from lstorage
if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
  document.getElementById("cart").innerHTML = Object.keys(cart).length;
  updateCart(cart);
}

//if click in add to cart then increment the item
$(".cart").click(function () {
  //console.log("clicked");
  var idstr = this.id.toString();
  //console.log(idstr);
  if (cart[idstr] != undefined) {
    cart[idstr] = cart[idstr] + 1;
  } else {
    cart[idstr] = 1;
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
  popStr = popStr + "<h5>Popover Info</h5>";
  var i = 1;
  for (var item in cart) {
    popStr = popStr + "<b>" + i + "</b>";
    popStr =
      popStr +
      document.getElementById("name" + item) +
      "Qty:" +
      cart["item"] +
      "<br>";
    i = i + 1;
  }
  console.log("popStr");
  document.getElementById("popcart").setAttribute("data-content", popStr);
  $("#popcart").popover("show");
}

function updateCart(cart) {
  for (var item in cart) {
    document.getElementById("div" + item).innerHTML =
      "<button id='minus" +
      item +
      "' class='btn btn-warning rounded-pill shadow minus'>-</button> <span id='val" +
      item +
      "''>" +
      cart[item] +
      "</span> <button id='plus" +
      item +
      "' class='btn btn-primary rounded-pill shadow plus'> + </button>";
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML = Object.keys(cart).length;
  console.log(cart);
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
  cart["pr" + a] = cart["pr" + a] - 1;
  cart["pr" + a] = Math.max(0, cart["pr" + a]);
  document.getElementById("valpr" + a).innerHTML = cart["pr" + a];
  updateCart(cart);
});

$(".divpr").on("click", "button.plus", function () {
  //console.log("plus clicked");
  a = this.id.slice(6);
  //console.log(a);
  cart["pr" + a] = cart["pr" + a] + 1;
  document.getElementById("valpr" + a).innerHTML = cart["pr" + a];
  updateCart(cart);
});
