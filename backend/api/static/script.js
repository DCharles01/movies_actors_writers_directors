document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");

    const dataTable = document.getElementById("dataTable");

    function filterData(searchTerm) {
        const rows = dataTable.querySelectorAll("tr");

        // iterate over rows
        rows.forEach(row => {
            const cells = row.getElementsByTagName("td");
            let rowVisible = false;

            Array.from(cells).forEach(cell => {
                if (cell.textContent.toLowerCase().includes(searchTerm.toLowerCase())) {
                    rowVisible = true;
                }
            });
            row.style.display = rowVisible ? "": "none";
        });
    }
    searchInput.addEventListener("input",
        function () {
            const searchTerm = searchInput.value.trim();
            filterData(searchTerm);
        });
});
// master search
function search() {
    var query = document.getElementById('search_query').value;
    var endpoint = "/movies/search?search_query=" + encodeURIComponent(query);

    // fetch(endpoint, {method: "POST"})
    //     .then(response => response.text())
    //     .then(data => {
    //         // convert data to json from clint side
    //         try {
    //             var jsonData = JSON.parse(data);
    //             displayResults(jsonData);
    //         } catch (error) {
    //             console.error('Error parsing JSON:', error)
    //             document.getElementById('result').textContent = 'Error parsing JSON';
    //         }
            
    //     })
        fetch(endpoint, {method: "POST"})
            .then(response => response.json())
            .then(data => {
                displayResults(data.results);
            })
        .catch(error => {
            console.error("Error: ", error);
        });

}


// display results
function displayResults(results) {
    var resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = "";

    if (Array.isArray(results) && results.length > 0) {
        var ul = document.createElement('ul');
        // var p = document.createElement('p');
        // p.textContent = "Yute from Scarborough";
        results.forEach(result => {
            var li = document.createElement('li');
            li.textContent = JSON.stringify(result);
            ul.appendChild(li);
        });
        resultsContainer.appendChild(ul);
    } else {
        resultsContainer.textContent = "No results found";
    }
}

// table results search



