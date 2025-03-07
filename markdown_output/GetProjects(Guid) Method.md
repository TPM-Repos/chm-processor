Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjects(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [GetProjects Method](topic3212.md) : GetProjects(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_permissionId_
    The permission to check for, generally one of the values from [DriveWorks.Security.StandardProjectPermissions](topic10695.md).

Glossary Item Box

Gets all registered projects on which the logged-on user holds the specified permission. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetProjects( _
       ByVal _permissionId_ As Guid _
    ) As [ProjectDetails()](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim permissionId As Guid
    Dim value() As [ProjectDetails](topic4330.md)
     
    value = instance.GetProjects(permissionId)  
  
C#|   
---|---  
      
    
    public [ProjectDetails[]](topic4330.md) GetProjects( 
       Guid _permissionId_
    )  
  
#### Parameters

 _permissionId_
    The permission to check for, generally one of the values from [DriveWorks.Security.StandardProjectPermissions](topic10695.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3212.md)


