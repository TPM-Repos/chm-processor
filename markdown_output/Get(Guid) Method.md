Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Get(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) > [Get Method](topic6442.md) : Get(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The id of the task to get.

Glossary Item Box

Gets the task with the given id in the collection (or a null reference if the task doesn't exist). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Get( _
       ByVal _taskId_ As Guid _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim taskId As Guid
    Dim value As [ComponentTask](topic6407.md)
     
    value = instance.Get(taskId)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) Get( 
       Guid _taskId_
    )  
  
#### Parameters

 _taskId_
    The id of the task to get.

#### Return Value

The task with the given id if it's present in the collection, otherwise a null reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)   
[Overload List](topic6442.md)


