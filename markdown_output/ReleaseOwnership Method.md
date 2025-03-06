ReleaseOwnership Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : ReleaseOwnership Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupName_
    The name of the group to be released

Glossary Item Box

Orders the server to release ownership of the specified group providing that the group is not in use by this server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Sub ReleaseOwnership( _
       ByVal _groupName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim groupName As String
     
    instance.ReleaseOwnership(groupName)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public void ReleaseOwnership( 
       string _groupName_
    )  
  
#### Parameters

 _groupName_
    The name of the group to be released

# Remarks

This can be called on any server, but will only check if the group is in use if called on the owning server for the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


