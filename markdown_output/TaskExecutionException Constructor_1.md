       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TaskExecutionException Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TaskExecutionException Class](topic11683.md) : TaskExecutionException Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskName_
    

_inner_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _taskName_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim taskName As String
    Dim inner As Exception
     
    Dim instance As New [TaskExecutionException](topic11683.md)(taskName, inner)  
  
C#|   
---|---  
      
    
    public TaskExecutionException( 
       string _taskName_ ,
       Exception _inner_
    )  
  
#### Parameters

 _taskName_
    
_inner_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskExecutionException Class](topic11683.md)   
[TaskExecutionException Members](topic11684.md)


