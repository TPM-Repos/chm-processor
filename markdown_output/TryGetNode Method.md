       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetNode Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11442.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacro Class](topic11429.md) : TryGetNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

_task_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function TryGetNode( _
       ByVal _name_ As String, _
       ByRef _task_ As [IFlowNode](topic6873.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacro](topic11429.md)
    Dim name As String
    Dim task As [IFlowNode](topic6873.md)
    Dim value As Boolean
     
    value = instance.TryGetNode(name, task)  
  
C#|   
---|---  
      
    
    public override bool TryGetNode( 
       string _name_ ,
       ref [IFlowNode](topic6873.md) _task_
    )  
  
#### Parameters

 _name_
    
_task_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[SpecificationMacro Members](topic11430.md)

©2024 DriveWorks Ltd. All Rights Reserved.
