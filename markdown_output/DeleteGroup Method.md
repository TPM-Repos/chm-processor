Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteGroup Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : DeleteGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupName_
    The name of the group to delete.

_creationUsername_
    The server's admin username.

_creationPassword_
    The server's admin password.

Glossary Item Box

Deletes a group from the server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub DeleteGroup( _
       ByVal _groupName_ As String, _
       ByVal _creationUsername_ As String, _
       ByVal _creationPassword_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim groupName As String
    Dim creationUsername As String
    Dim creationPassword As String
     
    instance.DeleteGroup(groupName, creationUsername, creationPassword)  
  
C#|   
---|---  
      
    
    public void DeleteGroup( 
       string _groupName_ ,
       string _creationUsername_ ,
       string _creationPassword_
    )  
  
#### Parameters

 _groupName_
    The name of the group to delete.
_creationUsername_
    The server's admin username.
_creationPassword_
    The server's admin password.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


