from services.user import get_current_user
from services.post import create_post
from database.storage import posts

def show_menu(current_user: str) -> None:
    print("\nWelcome to the bitter, where you can write posts!")
    print(f"You are signed in as: {current_user}")
    print("1. Create post")
    print("2. Look at all posts")
    print("3. Find user's posts")
    print("4. Exit")



def main() -> None:
    current_user = get_current_user()
    while True:
        show_menu(current_user)
        choice = input('What do you want to do?').strip()
        if choice in ('1', 'create post'):
            content = input("Write your post here: ").strip()
            if create_post(current_user, content):
                print("Your post was created")
            else:
                print("Could not create post. Check the post length.")
        elif choice in ('2', 'look at all posts'):
            for post in posts:
                print(f"{post['author']}: {post['content']}")
        elif choice in ('4', 'exit'):
            break

main()
