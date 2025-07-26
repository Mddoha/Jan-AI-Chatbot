from config import OWNER_UID, CEO_ID, ADMIN_ID, OPERATOR_ID

def is_authorized_user(user_id):
    """
    ইউজার চেক করে: শুধুমাত্র owner, ceo, admin, operator অনুমোদিত।
    """
    authorized_ids = {OWNER_UID, CEO_ID, ADMIN_ID, OPERATOR_ID}
    return user_id in authorized_ids
