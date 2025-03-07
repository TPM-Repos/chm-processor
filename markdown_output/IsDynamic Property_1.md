Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDynamic Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : IsDynamic Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether this property is dynamic. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsDynamic As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim value As Boolean
     
    value = instance.IsDynamic  
  
C#|   
---|---  
      
    
    public bool IsDynamic {get;}  
  
# Remarks

To switch a dynamic state of a property ensure [CanMakeDynamic](topic6641.md) is True use [SetIsDynamic](topic6639.md) to update the property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)


