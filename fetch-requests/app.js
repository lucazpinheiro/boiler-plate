
// GET
async function getData(url, callback) {
  try {
    const response = await fetch(url, {
      method: 'Get',
    });
    const data = await response.json();
    callback(data);
  } catch (err) {
    // do something
  }
}

getData('https://jsonplaceholder.typicode.com/todos/1', (data) => console.log(data));

// POST
async function postData(url, callback) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      body: JSON.stringify({
        title: 'something',
        body: 'something else',
        userId: 100,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      }
    });
    const data = await response.json();
    callback(data);
  } catch (err) {
    // do something
  }
}

postData('https://jsonplaceholder.typicode.com/posts', (data) => console.log(data));

// PUT
async function updateData(url, id, callback) {
  try {
    const response = await fetch(`${url}${id}`, {
      method: 'PUT',
      body: JSON.stringify({
        id: 100,
        title: 'something',
        body: 'other thing',
        userId: 100,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      }
    });
    const data = await response.json();
    callback(data);
  } catch (err) {
    // do something
  }
}

updateData('https://jsonplaceholder.typicode.com/posts/', 100, (data) => console.log(data));

// DELETE
async function deleteData(url, id) {
  try {
    const response = await fetch(`${url}${id}`, {
      method: 'DELETE',
    });
  } catch (err) {
    // do something
  }
}


deleteData('https://jsonplaceholder.typicode.com/posts/', 100);
