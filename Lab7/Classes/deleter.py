class Deleter:
    def __init__(self, local_users, local_posts, history_manager):
        self.local_users = local_users
        self.local_posts = local_posts
        self.history_manager = history_manager

    def delete_user(self, user_id):
        for user in self.local_users:
            if user.user_id == user_id:
                self.local_users.remove(user)
                self.history_manager.log("Видалити користувача", f"Видалено користувача з ID {user_id}")
                print(f"Користувача з ID {user_id} видалено.")
                return
        print(f"Користувача з ID {user_id} не знайдено в локальному сховищі.")

    def delete_post(self, post_id):
        for post in self.local_posts:
            if post.post_id == post_id:
                self.local_posts.remove(post)
                self.history_manager.log("Видалити пост", f"Видалено пост з ID {post_id}")
                print(f"Пост з ID {post_id} видалено.")
                return
        print(f"Пост з ID {post_id} не знайдено в локальному сховищі.")
