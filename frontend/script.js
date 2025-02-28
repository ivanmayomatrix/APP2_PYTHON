async function register() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  document.getElementById("message").textContent = data.message;
  if (response.ok) {
    window.location.href = "login.html";
  }
}

async function login() {
  console.log("login");
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  document.getElementById("message").textContent = data.message;
  if (response.ok) {
    window.location.href = "index.html";
  }
}

async function loadProducts() {
  const response = await fetch("http://127.0.0.1:5000/products");
  const products = await response.json();
  const list = document.getElementById("product-list");
  products.forEach((product) => {
    const item = document.createElement("li");
    item.textContent = `${product.name} - $${product.price}`;
    list.appendChild(item);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("product-list")) {
    loadProducts();
  }
});
