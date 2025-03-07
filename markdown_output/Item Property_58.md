Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_location_
    The sequence location of the task collection to retrieve.

Glossary Item Box

Gets the [ComponentTaskCollection](topic6466.md) for the tasks with the specified location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ComponentTaskCollection](topic6466.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ComponentTaskCollection](topic6466.md)
     
    value = instance.Item(location)  
  
C#|   
---|---  
      
    
    public [ComponentTaskCollection](topic6466.md) this[ 
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    ]; {get;}  
  
#### Parameters

 _location_
    The sequence location of the task collection to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)


