document.addEventListener("DOMContentLoaded", function () {

    // ===== PRODUCT DATA =====
    // ===== LOAD DATA FROM LOCAL STORAGE =====
let products = JSON.parse(localStorage.getItem("products")) || [
  { id: 1, name: "Laptop", price: 50000, stock: 5, category: "electronics" },
  { id: 2, name: "Mouse", price: 1000, stock: 10, category: "electronics" },
  { id: 3, name: "T-Shirt", price: 800, stock: 2, category: "clothing" },
  { id: 4, name: "Book", price: 500, stock: 0, category: "books" }
];


function saveData() {
  localStorage.setItem("products", JSON.stringify(products));
}


    // ===== SHOW PRODUCTS =====
    function renderProducts(list) {
        let grid = document.getElementById("productGrid");
        grid.innerHTML = "";

        if (list.length === 0) {
            grid.innerHTML = "<p>No products found</p>";
            return;
        }

        list.forEach(p => {
            let div = document.createElement("div");
            div.className = "card";

            div.innerHTML = `
            <h3>${p.name}</h3>
            <p>Price: ₹${p.price}</p>
            <p>Stock: ${p.stock}</p>
            <p>Category: ${p.category}</p>

          <!-- delete button -->
           <button onclick="deleteProduct(${p.id})">Delete</button>
        `;

            grid.appendChild(div);
        });
    }

    // ===== FILTER =====
    // ===== FILTER + SORT FUNCTION =====
    function getFilteredProducts() {

        let search = document.getElementById("searchInput").value.toLowerCase();
        let category = document.getElementById("categoryFilter").value;
        let lowStock = document.getElementById("lowStockFilter").checked;
        let sort = document.getElementById("sortBy").value;

        let result = products.filter(p =>
            p.name.toLowerCase().includes(search) &&
            (category === "all" || p.category === category) &&
            (!lowStock || p.stock < 5)
        );

        // ===== SORTING =====

        if (sort === "low") {
            // price low to high
            result.sort((a, b) => a.price - b.price);
        }

        else if (sort === "high") {
            // price high to low
            result.sort((a, b) => b.price - a.price);
        }

        else if (sort === "az") {
            // name A-Z
            result.sort((a, b) => a.name.localeCompare(b.name));
        }

        else if (sort === "za") {
            // name Z-A
            result.sort((a, b) => b.name.localeCompare(a.name));
        }

        return result;
    }

    document.getElementById("sortBy").onchange = updateUI;


    // ===== UPDATE UI =====
    function updateUI() {

        let data = getFilteredProducts();

        renderProducts(data);

        // analytics bhi update karo
        updateAnalytics();
    }

    // ===== EVENTS =====
    document.getElementById("searchInput").oninput = updateUI;
    document.getElementById("categoryFilter").onchange = updateUI;
    document.getElementById("lowStockFilter").onchange = updateUI;

    // hide loading
    document.getElementById("loading").style.display = "none";


    
    // ===== INITIAL LOAD =====
async function init() {


  // wait for fake API
  let data = await fetchProducts();

  // loading hide
  document.getElementById("loading").style.display = "none";

  // UI show
  renderProducts(data);
  updateAnalytics();
}

// call init
init();

    // ===== ANALYTICS FUNCTION =====
    function updateAnalytics() {

        // total products
        document.getElementById("totalProducts").innerText = products.length;

        let totalValue = 0;
        let outOfStock = 0;

        // loop through products
        products.forEach(p => {

            // total value = price * stock
            totalValue += p.price * p.stock;

            // check out of stock
            if (p.stock === 0) {
                outOfStock++;
            }
        });

        // update UI
        document.getElementById("totalValue").innerText = "₹" + totalValue;
        document.getElementById("outOfStock").innerText = outOfStock;
    }

    // ===== ADD PRODUCT =====
    function addProduct() {

        // get data from form
        let name = document.getElementById("name").value;
        let price = Number(document.getElementById("price").value);
        let stock = Number(document.getElementById("stock").value);
        let category = document.getElementById("category").value;

        // ===== VALIDATION =====
        if (!name || price <= 0 || stock < 0 || !category) {
            alert("Please enter valid data");
            return;
         
        }

        // ===== NEW PRODUCT OBJECT =====
        let newProduct = {
            id: Date.now(),  // unique id
            name,
            price,
            stock,
            category
        };

        // array me add
        products.push(newProduct);
        // save to local storage
        saveData();
        // UI update
        updateUI();

        // ===== CLEAR FORM =====
        document.getElementById("name").value = "";
        document.getElementById("price").value = "";
        document.getElementById("stock").value = "";
        document.getElementById("category").value = "";
    }

    // make addProduct global so that it can be called from HTML
    window.addProduct = addProduct;

    // ===== DELETE PRODUCT =====
function deleteProduct(id) {

  products = products.filter(p => p.id !== id);

  saveData();  

  updateUI();
}
// make deleteProduct global so that it can be called from HTML
window.deleteProduct = deleteProduct;

// ===== SIMULATE API =====
function fetchProducts() {
  return new Promise(resolve => {

    // 1.5 sec delay
    setTimeout(() => {
      resolve(products);
    }, 1500);

  });
}

});