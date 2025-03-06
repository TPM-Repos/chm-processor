       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateSpecificationTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : UpdateSpecificationTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to update.

Glossary Item Box

Updates the data in the specified specification task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateSpecificationTask( _
       ByVal _task_ As [SpecificationTaskDetails](topic11510.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim task As [SpecificationTaskDetails](topic11510.md)
    Dim value As Boolean
     
    value = instance.UpdateSpecificationTask(task)  
  
C#|   
---|---  
      
    
    public bool UpdateSpecificationTask( 
       [SpecificationTaskDetails](topic11510.md) _task_
    )  
  
#### Parameters

 _task_
    The task to update.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


