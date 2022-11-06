from config import APP_URL, LOG
from lib.comments import Comments


def test_get_all_comments(login_as_admin):
    LOG.info("test_get_all_comments")
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.debug(response.json())

    assert response.ok


def test_create_comment(login_as_admin):
    LOG.info("test_create_comment")
    create_the_comment = Comments().create_comment(APP_URL, login_as_admin, "First Comment")
    response_data = create_the_comment.json()
    LOG.debug(response_data)

    assert response_data["comment_text"] == "First Comment"
    assert create_the_comment.ok


def test_update_comment(login_as_admin):
    comment_id = Comments().get_comment_id(APP_URL, login_as_admin)
    update_the_comment = Comments().update_the_comment(APP_URL, login_as_admin, comment_id,
                                                       message="My First updated comment", likes=6)
    response_data = update_the_comment.json()
    LOG.debug(response_data)

    assert response_data["comment_text"] == "My First updated comment"
    assert response_data["likes"] == 6
    assert update_the_comment.ok


def test_delete_comment(login_as_admin):
    comment_id = Comments().get_comment_id(APP_URL, login_as_admin)
    delete_the_comment = Comments().delete_comment(APP_URL, login_as_admin, comment_id)
    response_data = delete_the_comment.json()
    LOG.debug(response_data)

    assert response_data["detail"] == f"Deleted comment {comment_id}"
    assert delete_the_comment.ok
