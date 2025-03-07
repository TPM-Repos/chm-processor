Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PermissionId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [TeamProjectPermission Class](topic10729.md) : PermissionId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifier of the permission granted to the team on the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property PermissionId As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TeamProjectPermission](topic10729.md)
    Dim value As Guid
     
    value = instance.PermissionId  
  
C#|   
---|---  
      
    
    public Guid PermissionId {get;}  
  
# Remarks

This is generally one of the values from [StandardProjectPermissions](topic10695.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TeamProjectPermission Class](topic10729.md)   
[TeamProjectPermission Members](topic10730.md)


