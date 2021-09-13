# Documentation

## User

### **User Register**

##### URL: `http://heypixel.herokuapp.com/api/register/`

##### Method: `POST`

#### Required fields: `username`,  `password`,  `password2`,  `email`, `first_name`, `last_name`

#### Notes: email has to be a valid email and password has to be min 8 and max 10 alphanumeric characters

##### Status code: `201 Created`

```json
{
  "message": "Register was successfully!",
}
```

#### Error Response `404`

```json
{
  "error": "Error message 404";
}
```

### **User Login**

#### URL: `http://heypixel.herokuapp.com/api/login/`

#### Method: `POST`

#### Required fields: `username`, `password`

#### Status code: `200 OK`

```json
{
    "refresh": "string",
    "access": "string"
}
```

#### Status code: `404 Error`

```json
{
  "error": "Error message 404";
}
```

### **User Logout**

#### URL: `http://heypixel.herokuapp.com/api/logout/`

#### Method: `POST`

#### Status code: `205 Reset Content`

```json
{
    "message": "Logout was successfully!"
}
```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Change password**

#### URL: `heypixel.herokuapp.com/api/change_password/{id}/`

#### Method: `PUT`

#### Required fields: `old_password`, `password`, `password2`

#### Notes: Authentication credentials are required.

#### Status code: `200 OK`

```json
{}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

## Profiles

### **Get all profiles**

#### URL: `http://heypixel.herokuapp.com/api/profiles/`

#### Method: `GET`

#### Status code: `200 OK`

```json
[
    {
        "id": integer,
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "string"
    },
    {
        "id": integer,
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "string"
    },

]

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

### **Get detail of a profile**

#### URL: `http://heypixel.herokuapp.com/api/profiles/{id}`

#### Method: `GET`

#### Status code: `200 OK`

```json
[
    {
        "id": integer,
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "string"
    }

]

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

### **Update profile**

#### URL: `http://heypixel.herokuapp.com/api/update_profile/{id}/`

#### Method: `PUT`

#### Required fields: `username`, `first_name`, `last_name`, `email`

#### Notes: first_name and last_name are required. Authentication credentials are required.

#### Status code: `200 OK`

```py
{}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

---

## Posts

### **Created a post**

#### URL: `http://heypixel.herokuapp.com/api/posts/`

#### Method: `POST`

#### Required fields: `body`, `created_on`, `author`, `image`

#### Status code: `201 Created`

```py
{
  'message': 'Post was created successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

### **Update a post**

#### URL: `http://heypixel.herokuapp.com/api/posts/{id}/`

#### Method: `PUT`

#### Required fields: `body`, `created_on`, `author`, `image`

#### Status code: `200 OK`

```py
{
  'message': 'Post was updated successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

### **Delete a post**

#### URL: `http://heypixel.herokuapp.com/api/posts/{id}/`

#### Method: `DEL`

#### Status code: `204 No content`

```py
{
  'message': 'Post was deleted successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Get all post**

#### URL: `http://heypixel.herokuapp.com/api/posts/`

#### Method: `GET`

#### Status code: `200 OK`

```json
[
  {
    "id": integer,
    "body": "string",
    "created_on": "string",
    "author": integer,
    "image": "string",
    "comments": [
      "string or empty list is there is not comments for this post"
    ],
    "likes": [
      integer or empty list is there is not comments for this post
    ]
}
]
```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Get one post**

#### URL: `http://heypixel.herokuapp.com/api/posts/{id}`

#### Method: `GET`

#### Status code: `200 OK`

```json
[
  {
    "id": integer,
    "body": "string",
    "created_on": "string",
    "author": integer,
    "image": "string",
    "comments": [
      "string or empty list is there is not comments for this post"
    ],
    "likes": [
      integer or empty list is there is not comments for this post
    ]
  }
]
```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


---

## Comments

### **Get all comments**

#### URL: `http://heypixel.herokuapp.com/api/comments/`

#### Method: `GET`

#### Success Response `200 OK`

```json
[
  {
    "id": integer,
    "body_comment": "string",
    "created_on": "string",
    "post": integer,
    "author": 1integer
  },
]
```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Created a comment**

#### URL: `http://heypixel.herokuapp.com/api/comments/`

#### Method: `POST`

#### Required fields: `body_comment`, `created_on`, `post`, `author`

#### Status code: `201 Created`

```py
{
  'message': 'Comment was created successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Update a comment**

#### URL: `http://heypixel.herokuapp.com/api/comments/{id}/`

#### Method: `PUT`

#### Required fields: `body`, `created_on`, `author`, `image`

#### Status code: `200 OK`

```py
{
  'message': 'Comment was updated successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

### **Delete a comment**

#### URL: `http://heypixel.herokuapp.com/api/comments/{id}/`

#### Method: `DEL`

#### Status code: `204 No content`

```py
{
  'message': 'Comment was deleted successfully!'
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```

---

### **Give a like**

#### URL: `http://heypixel.herokuapp.com/api/likes/`

#### Method: `POST`

#### Required fields: `like_post`, `author`

#### Status code: `201 Created`

```json
{
    "id": integer,
    "like_post": integer,
    "author": integer
}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


### **Remove a like**

#### URL: `http://heypixel.herokuapp.com/api/likes/{id}/`

#### Method: `DEL`

#### Status code: `204 No content`

```py

{}

```

#### Error Response `404`

```json
{
  "error": "Error message 404"
}
```


---

## Search and filter

### Search the content of a post by keyword

#### URL: `http://heypixel.herokuapp.com/api/posts/?body=keyword`

#### Method: `GET`

#### Status code: `200 OK`

```json
[
    {
        "id": integer,
        "body": "string",
        "created_on": "string",
        "author": "string",
        "image": "string",
        "comments": [
            "string",
        ],
        "likes": [
            integer,
        ]
    }
]
```

#### Error Response `404`

```js
{
  "error": "Search not found"
}
```