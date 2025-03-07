Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecificationTasks(String,Boolean,Boolean,Boolean,Boolean,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetSpecificationTasks Method](topic3382.md) : GetSpecificationTasks(String,Boolean,Boolean,Boolean,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskType_
    The type of task to retrieve/

_descending_
    True to retrieve tasks in reverse chronological order of when their parent specifications were created.

_includeComplete_
    True to include complete tasks, otherwise false.

_includeInComplete_
    True to include incomplete tasks, otherwise false.

_includeFailed_
    True to include failed tasks, otherwise false.

_includeMissingSpecifications_
    True to include tasks that have no registered specification information.

Glossary Item Box

Gets all of the specification tasks of the given type matching the specified criteria. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetSpecificationTasks( _
       ByVal _taskType_ As String, _
       ByVal _descending_ As Boolean, _
       ByVal _includeComplete_ As Boolean, _
       ByVal _includeInComplete_ As Boolean, _
       ByVal _includeFailed_ As Boolean, _
       ByVal _includeMissingSpecifications_ As Boolean _
    ) As IEnumerable(Of SpecificationTaskDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim taskType As String
    Dim descending As Boolean
    Dim includeComplete As Boolean
    Dim includeInComplete As Boolean
    Dim includeFailed As Boolean
    Dim includeMissingSpecifications As Boolean
    Dim value As IEnumerable(Of SpecificationTaskDetails)
     
    value = instance.GetSpecificationTasks(taskType, descending, includeComplete, includeInComplete, includeFailed, includeMissingSpecifications)  
  
C#|   
---|---  
      
    
    public IEnumerable<SpecificationTaskDetails> GetSpecificationTasks( 
       string _taskType_ ,
       bool _descending_ ,
       bool _includeComplete_ ,
       bool _includeInComplete_ ,
       bool _includeFailed_ ,
       bool _includeMissingSpecifications_
    )  
  
#### Parameters

 _taskType_
    The type of task to retrieve/
_descending_
    True to retrieve tasks in reverse chronological order of when their parent specifications were created.
_includeComplete_
    True to include complete tasks, otherwise false.
_includeInComplete_
    True to include incomplete tasks, otherwise false.
_includeFailed_
    True to include failed tasks, otherwise false.
_includeMissingSpecifications_
    True to include tasks that have no registered specification information.

#### Return Value

Returns an enumerable of specification tasks that match the specified criteria.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3382.md)


