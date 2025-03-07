Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) : DeleteComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component to delete.

Glossary Item Box

Uncaptures the specified component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub DeleteComponent( _
       ByVal _componentId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim componentId As Guid
     
    instance.DeleteComponent(componentId)  
  
C#|   
---|---  
      
    
    public void DeleteComponent( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)


