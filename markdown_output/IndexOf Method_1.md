Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexOf Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) : IndexOf Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task whose index to retrieve.

Glossary Item Box

Gets the index of the given task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IndexOf( _
       ByVal _task_ As [Task](topic11629.md) _
    ) As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim task As [Task](topic11629.md)
    Dim value As Integer
     
    value = instance.IndexOf(task)  
  
C#|   
---|---  
      
    
    public int IndexOf( 
       [Task](topic11629.md) _task_
    )  
  
#### Parameters

 _task_
    The task whose index to retrieve.

#### Return Value

The index of the given task, or -1 if the task is not in this collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)


