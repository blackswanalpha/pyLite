const { app, BrowserWindow } = require('electron');
const path = require('path');
const axios = require('axios');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    });

    mainWindow.loadFile('../../templates/index.html');
}

// Example Axios usage to fetch posts
axios.get('http://127.0.0.1:5000/api/blog/posts/get')
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error('Error fetching posts:', error);
    });

// Example Axios usage to add a new post
axios.post('http://127.0.0.1:5000/api/blog/posts/add', {
    title: 'New Post',
    content: 'This is the content of the new post.'
})
.then(response => {
    console.log('Post created:', response.data);
})
.catch(error => {
    console.error('Error creating post:', error);
});

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
