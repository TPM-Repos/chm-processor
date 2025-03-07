Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureCollection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) : EnsureCollection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_location_
    The location of the task collection.

Glossary Item Box

Ensures that a task collection for the given location has been created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function EnsureCollection( _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ComponentTaskCollection](topic6466.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ComponentTaskCollection](topic6466.md)
     
    value = instance.EnsureCollection(location)  
  
C#|   
---|---  
      
    
    protected abstract [ComponentTaskCollection](topic6466.md) EnsureCollection( 
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    )  
  
#### Parameters

 _location_
    The location of the task collection.

#### Return Value

A task collection for the given location.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)


