_T_
    The type of the task to add.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTask<T>(String,Double,Double) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskSequence Class](topic11713.md) > [CreateTask Method](topic11720.md) : CreateTask<T>(String,Double,Double) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the task

_left_
    The left position of the task.

_top_
    The top position of the task.

Glossary Item Box

Creates and adds a new task to the task sequence. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTask(Of T As [Task](topic11629.md))( _
       ByVal _title_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequence](topic11713.md)
    Dim title As String
    Dim left As Double
    Dim top As Double
    Dim value As T
     
    value = instance.CreateTask(Of T)(title, left, top)  
  
C#|   
---|---  
      
    
    public T CreateTask<T>( 
       string _title_ ,
       double _left_ ,
       double _top_
    )
    where T: [Task](topic11629.md)  
  
#### Parameters

 _title_
    The title of the task
 _left_
    The left position of the task.
_top_
    The top position of the task.

#### Type Parameters

_T_
    The type of the task to add.

#### Return Value

The newly created task.

# Exceptions

Exception| Description  
---|---  
System.ArgumentOutOfRangeException| The type specified in for the type parameter T isn't defined in a extension library.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequence Class](topic11713.md)   
[TaskSequence Members](topic11714.md)   
[Overload List](topic11720.md)


