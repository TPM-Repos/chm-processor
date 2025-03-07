Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteSpecificationTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : DeleteSpecificationTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The unique identifier of the task to delete.

Glossary Item Box

Deletes the specification task with the specified unique identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteSpecificationTask( _
       ByVal _taskId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskId As Guid
    Dim value As Boolean
     
    value = instance.DeleteSpecificationTask(taskId)  
  
C#|   
---|---  
      
    
    public bool DeleteSpecificationTask( 
       Guid _taskId_
    )  
  
#### Parameters

 _taskId_
    The unique identifier of the task to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


