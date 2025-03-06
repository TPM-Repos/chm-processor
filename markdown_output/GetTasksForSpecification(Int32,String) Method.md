![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTasksForSpecification(Int32,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetTasksForSpecification Method](topic3385.md) : GetTasksForSpecification(Int32,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The numerical identifier of the specification for which to get reports.

_taskType_
    The type of task to retrieve.

Glossary Item Box

Gets all tasks for a specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetTasksForSpecification( _
       ByVal _specificationId_ As Integer, _
       ByVal _taskType_ As String _
    ) As [SpecificationTaskDetails()](topic11510.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim taskType As String
    Dim value() As [SpecificationTaskDetails](topic11510.md)
     
    value = instance.GetTasksForSpecification(specificationId, taskType)  
  
C#|   
---|---  
      
    
    public [SpecificationTaskDetails[]](topic11510.md) GetTasksForSpecification( 
       int _specificationId_ ,
       string _taskType_
    )  
  
#### Parameters

 _specificationId_
    The numerical identifier of the specification for which to get reports.
_taskType_
    The type of task to retrieve.

#### Return Value

An array of tasks, matching the specified type, for the specification.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3385.md)


