##########
Name: "check-dir-permission"
Author: "BHARAT SUNEJA"
Description: "Check directory permission"
Options:
    path: "Destination path (Ex. c:\\)"
##########
(get-acl {{ path }}).access | ft IdentityReference,FileSystemRights,AccessControlType,IsInherited,InheritanceFlags -auto