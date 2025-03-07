Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkGenerated Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : MarkGenerated Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component

Glossary Item Box

Marks the specified component as being generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MarkGenerated( _
       ByVal _componentId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
     
    instance.MarkGenerated(componentId)  
  
C#|   
---|---  
      
    
    public void MarkGenerated( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component

# Remarks

Marking a component as having been generated automatically clears the generating and failed fields.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


