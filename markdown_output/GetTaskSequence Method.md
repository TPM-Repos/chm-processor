Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTaskSequence Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskSequenceRef Class](topic13159.md) : GetTaskSequence Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

Gets the task sequence from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetTaskSequence( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [TaskSequence](topic11713.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TaskSequenceRef](topic13159.md)
    Dim project As [Project](topic3859.md)
    Dim value As [TaskSequence](topic11713.md)
     
    value = instance.GetTaskSequence(project)  
  
C#|   
---|---  
      
    
    public abstract [TaskSequence](topic11713.md) GetTaskSequence( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TaskSequenceRef Class](topic13159.md)   
[TaskSequenceRef Members](topic13160.md)


