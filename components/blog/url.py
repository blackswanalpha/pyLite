from flask import Blueprint, jsonify, request

from components.blog.models import Post
from components.blog.service import CRUDService


# Create a Blueprint for the blog routes
blog_service = Blueprint('blog', __name__, url_prefix='/api/blog')

# Initialize the CRUD service for posts
post_service = CRUDService(Post)

# Routes
@blog_service.route('/posts/get', methods=['GET'])
def get_posts():
    posts = post_service.get_all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at
    } for post in posts])

@blog_service.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = post_service.get_by_id(post_id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at
    })

@blog_service.route('/posts/add', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = post_service.create(data)
    return jsonify({'message': 'Post created successfully', 'post': new_post.id}), 201

@blog_service.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    updated_post = post_service.update(post_id, data)
    return jsonify({'message': 'Post updated successfully'})

@blog_service.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post_service.delete(post_id)
    return jsonify({'message': 'Post deleted successfully'})
