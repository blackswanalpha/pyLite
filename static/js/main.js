document.getElementById('randomNumberBtn').addEventListener('click', function() {
    fetch('/random_number')
        .then(response => response.json())
        .then(data => {
            document.getElementById('randomNumber').innerText = `Random Number: ${data.number}`;
        });
});

document.getElementById('reverseStringBtn').addEventListener('click', function() {
    const stringInput = document.getElementById('stringInput').value;
    fetch('/reverse_string', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ string: stringInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('reversedString').innerText = `Reversed String: ${data.reversed_string}`;
    });
});

document.getElementById('addUserBtn').addEventListener('click', function() {
    const userNameInput = document.getElementById('userNameInput').value;
    fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: userNameInput })
    })
    .then(response => response.json())
    .then(data => {
        alert(`User added with ID: ${data.id}`);
    });
});

document.getElementById('getUsersBtn').addEventListener('click', function() {
    fetch('/get_users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('userList');
            userList.innerHTML = '';
            data.users.forEach(user => {
                const li = document.createElement('li');
                li.innerText = `ID: ${user.id}, Name: ${user.name}`;
                userList.appendChild(li);
            });
        });
});
