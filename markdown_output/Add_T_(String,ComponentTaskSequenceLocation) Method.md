_T_
    The type of the task to create.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add<T>(String,ComponentTaskSequenceLocation) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) > [Add Method](topic6435.md) : Add<T>(String,ComponentTaskSequenceLocation) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the task to create.

_location_
    The location of the task.

Glossary Item Box

Adds a new task to the collection and returns the newly created task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add(Of T)( _
       ByVal _name_ As String, _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim name As String
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ComponentTask](topic6407.md)
     
    value = instance.Add(Of T)(name, location)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) Add<T>( 
       string _name_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    )  
  
#### Parameters

 _name_
    The name of the task to create.
_location_
    The location of the task.

#### Type Parameters

_T_
    The type of the task to create.

#### Return Value

The newly created task, or a null reference (Nothing in VB) if the creation of the task fails.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)   
[Overload List](topic6435.md)


