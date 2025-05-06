// Load all movies when the page loads
document.addEventListener('DOMContentLoaded', function () {
    fetchMovies();
});

// Fetch movies from the backend
function fetchMovies() {
    fetch('/movies')
        .then(response => response.json())
        .then(data => {
            const movieList = document.getElementById('movie-list');
            movieList.innerHTML = '';              data.forEach(movie => {
                const movieItem = document.createElement('li');
                movieItem.textContent = `${movie[1]} - ${movie[2]} (${movie[3]})`; // movie[1] - title, movie[2] - genre, movie[3] - release_year
                
                // Create a delete button for each movie
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteMovie(movie[0]); // movie[0] is the ID
                
                movieItem.appendChild(deleteButton);
                movieList.appendChild(movieItem);
            });
        })
        .catch(error => console.log('Error fetching data:', error));
}

// Add a new movie
document.getElementById('add-movie-form').addEventListener('submit', function (event) {
    event.preventDefault();
    
    const title = document.getElementById('title').value;
    const genre = document.getElementById('genre').value;
    const releaseYear = document.getElementById('release-year').value;

    fetch('/movies', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            genre: genre,
            release_year: releaseYear
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert("Movie added!");
        fetchMovies();      })
    .catch(error => console.error('Error:', error));
});

// Delete a movie
function deleteMovie(id) {
    fetch(`/movies/${id}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        alert('Movie deleted!');
        fetchMovies();      })
    .catch(error => console.error('Error:', error));
}
