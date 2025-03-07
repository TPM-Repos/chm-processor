Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskRef Class](topic13149.md) : GetTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

Gets the task from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTask( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [Task](topic11629.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskRef](topic13149.md)
    Dim project As [Project](topic3859.md)
    Dim value As [Task](topic11629.md)
     
    value = instance.GetTask(project)  
  
C#|   
---|---  
      
    
    public [Task](topic11629.md) GetTask( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskRef Class](topic13149.md)   
[TaskRef Members](topic13150.md)


