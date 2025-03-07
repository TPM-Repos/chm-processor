Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkSpecificationTaskFailed Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : MarkSpecificationTaskFailed Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The unique identifier of the task to mark.

_failedCount_
    The number of times the task has failed.

Glossary Item Box

Attempts to mark the specified specification task as having failed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function MarkSpecificationTaskFailed( _
       ByVal _taskId_ As Guid, _
       ByVal _failedCount_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskId As Guid
    Dim failedCount As Integer
    Dim value As Boolean
     
    value = instance.MarkSpecificationTaskFailed(taskId, failedCount)  
  
C#|   
---|---  
      
    
    public bool MarkSpecificationTaskFailed( 
       Guid _taskId_ ,
       int _failedCount_
    )  
  
#### Parameters

 _taskId_
    The unique identifier of the task to mark.
_failedCount_
    The number of times the task has failed.

# Remarks

This will mark the task as not being completed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


