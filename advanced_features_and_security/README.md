# Permissions and Groups Setup

## Custom Permissions
- **can_view_book**: Allows viewing book details.
- **can_create_book**: Allows creating new book entries.
- **can_edit_book**: Allows editing existing book entries.
- **can_delete_book**: Allows deleting book entries.

## Groups and Their Permissions
- **Editors**: Can create and edit book entries.
- **Viewers**: Can view book entries.
- **Admins**: Can view, create, edit, and delete book entries.

## How to Assign Permissions
- Permissions are assigned to groups through the Django admin interface or via the `setup_groups` management command.