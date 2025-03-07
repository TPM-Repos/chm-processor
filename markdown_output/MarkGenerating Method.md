Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkGenerating Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : MarkGenerating Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component

Glossary Item Box

Marks the specified component as being in the process of being generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MarkGenerating( _
       ByVal _componentId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
     
    instance.MarkGenerating(componentId)  
  
C#|   
---|---  
      
    
    public void MarkGenerating( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


