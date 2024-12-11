const axios = require('axios');

// Function to fetch and display blog posts
function fetchPosts() {
  axios.get('http://localhost:5000/api/blog/posts')
    .then(response => {
      const posts = response.data;
      const postsContainer = document.getElementById('posts');
      postsContainer.innerHTML = '';

      posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'post';

        const titleElement = document.createElement('h2');
        titleElement.textContent = post.title;

        const contentElement = document.createElement('p');
        contentElement.textContent = post.content;

        postElement.appendChild(titleElement);
        postElement.appendChild(contentElement);

        postsContainer.appendChild(postElement);
      });
    })
    .catch(error => {
      console.error('There was an error fetching the posts!', error);
    });
}

// Fetch posts when the window loads
window.onload = fetchPosts;
