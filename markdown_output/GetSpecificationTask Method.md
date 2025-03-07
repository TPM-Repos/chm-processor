Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : GetSpecificationTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskId_
    The id of the specification task to retrieve.

Glossary Item Box

Gets the specification task with the specified id. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSpecificationTask( _
       ByVal _taskId_ As Guid _
    ) As [SpecificationTaskDetails](topic11510.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskId As Guid
    Dim value As [SpecificationTaskDetails](topic11510.md)
     
    value = instance.GetSpecificationTask(taskId)  
  
C#|   
---|---  
      
    
    public [SpecificationTaskDetails](topic11510.md) GetSpecificationTask( 
       Guid _taskId_
    )  
  
#### Parameters

 _taskId_
    The id of the specification task to retrieve.

#### Return Value

The specification task for the specified id.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


